from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

from blog.models import Ad
from blog.models import Article
from blog.models import ArticleCategory
from blog.models import ArticleTag
from blog.models import Link
from django.db import connection
import logging

from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_GET


def global_settings(request):

    return {
            'SITE_NAME': settings.SITE_NAME,
            'SITE_DESC': settings.SITE_DESC,
            }


def log():
    logger = logging.getLogger('blog.views')
    try:
        open('abc.txt', 'r')
    except Exception as e:
        logger.error(e)


@require_GET
@cache_page(60 * 15, key_prefix='index')
def index(request):
    category_list = ArticleCategory.objects.all()

    article_list = Article.objects.all()

    ad_list = Ad.objects.all()

    read_list = article_list.order_by('-read_count')[:6]

    con = connection.cursor()
    con.execute('''SELECT
                    a.title,
                    COUNT(*) com_count
                FROM
                    blog_articlecomment c
                JOIN blog_article a ON c.article_id_id = a.id
                GROUP BY
                    c.article_id_id order by com_count desc;''')
    article_comment_list = con.fetchall()

    comment_list = []
    [comment_list.append(comment[0]) for comment in article_comment_list]

    tag_list = ArticleTag.objects.all()

    link_list = Link.objects.all()

    recommend_list = article_list.values('title').filter()[:6]

    con = connection.cursor()
    con.execute('''select distinct date_format(publish_date,"%Y-%m") pub_date from blog_article;''')
    article_pub_list = con.fetchall()

    logger = logging.getLogger('blog.views')
    paginator = Paginator(article_list, 5)

    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    except Exception as e:
        logger.error(e)

    return render(request, 'index.html', locals())


def tagArticle(request):
    tag = request.GET.get('tag', None)
    article_list = Article.objects.filter(tag_id__tag=tag)

    category_list = ArticleCategory.objects.all()

    ad_list = Ad.objects.all()

    read_list = article_list.order_by('-read_count')[:6]

    con = connection.cursor()
    con.execute('''SELECT
                    a.title,
                    COUNT(*) com_count
                FROM
                    blog_articlecomment c
                JOIN blog_article a ON c.article_id_id = a.id
                GROUP BY
                    c.article_id_id order by com_count desc;''')
    article_comment_list = con.fetchall()

    comment_list = []
    [comment_list.append(comment[0]) for comment in article_comment_list]

    tag_list = ArticleTag.objects.all()

    link_list = Link.objects.all()

    recommend_list = article_list.values('title').filter()[:6]

    con = connection.cursor()
    con.execute('''select distinct date_format(publish_date,"%Y-%m") pub_date from blog_article;''')
    article_pub_list = con.fetchall()

    logger = logging.getLogger('blog.views')
    paginator = Paginator(article_list, 5)

    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    except Exception as e:
        logger.error(e)

    return render(request, 'tagArticle.html', locals())




