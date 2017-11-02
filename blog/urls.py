from django.conf.urls import url
from django.conf import settings
from blog.views import index
from blog.views import tagArticle
from django.views import static

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^uploads/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^tagarticle/.*$', tagArticle, name='tagArticle')
]
