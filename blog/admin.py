from django.contrib import admin
from blog.models import *


class AdminUser(admin.ModelAdmin):
    # fields = ('username', 'sex', 'mobile', 'email', 'birth', 'qq', 'image', 'profile')
    # exclude = ('name', 'sex', 'mobile')

    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'sex', 'birth', 'qq', 'mobile', 'email', 'image', 'profile',
                       'is_staff', 'is_active')
            }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('marriage', 'occupation', 'home_province', 'home_city', 'school', 'profession',
                       'school_date', 'company', 'position', 'work_date'),
        }),
    )

    list_display = ('username', 'sex', 'birth', 'qq', 'mobile', 'email')
    list_display_links = ('username', 'sex', 'birth', 'qq', 'mobile', 'email')
    list_filter = ('username', 'id')
    # inlines
    # list_editable = ()


class AdminArticle(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'user_id', 'desc', 'content', 'category_id', 'tag_id',  'channel', 'is_recommend')
            }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('read_count', 'reprint_count', 'collect_count')
        }),
    )

    list_display = ('title', 'user_id', 'desc', 'publish_date', 'category_id', 'channel', 'is_recommend')
    list_display_links = ('title', 'user_id', 'desc', 'publish_date', 'category_id', 'channel', 'is_recommend')
    list_filter = ('title', 'user_id')

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js'
        )


class AdminArticleTag(admin.ModelAdmin):
    fields = ('tag', )
    list_display = ('tag',)
    list_display_links = ('tag',)
    list_filter = ('tag',)


class AdminArticleCategory(admin.ModelAdmin):
    fields = ('category', 'user_id')
    list_display = ('category', 'user_id')
    list_display_links = ('category', 'user_id')
    list_filter = ('category', 'user_id')


class AdminArticleComment(admin.ModelAdmin):
    fields = ('content', 'article_id', 'user_id', 'p_id')
    list_display = ('content', 'publish_date', 'article_id', 'user_id', 'p_id')
    list_display_links = ('content', 'publish_date', 'article_id', 'user_id', 'p_id')
    list_filter = ('article_id', 'user_id')


class AdminUserFans(admin.ModelAdmin):
    fields = ('user_id', 'fans_id')
    list_display = ('user_id', 'fans_id')
    list_display_links = ('user_id', 'fans_id')
    list_filter = ('user_id', 'fans_id')


class AdminUserExt(admin.ModelAdmin):
    fields = ('user_id', 'guest_id', 'is_message', 'message')
    list_display = ('user_id', 'guest_id', 'is_message', 'message')
    list_display_links = ('user_id', 'guest_id', 'is_message', 'message')
    list_filter = ('user_id', 'guest_id')


class AdminUserCollectArticle(admin.ModelAdmin):
    fields = ('user_id', 'article_id')
    list_display = ('user_id', 'article_id')
    list_display_links = ('user_id', 'article_id')
    list_filter = ('user_id', 'article_id')


class AdminAd(admin.ModelAdmin):
    fields = ('title', 'desc', 'image_url', 'link_url', 'click_count')
    list_display = ('title', 'desc', 'image_url', 'link_url', 'publish_date', 'click_count')
    list_display_links = ('title', 'desc', 'image_url', 'link_url', 'publish_date', 'click_count')
    list_filter = ('title',)


class AdminLink(admin.ModelAdmin):
    fields = ('title', 'desc', 'link_url', 'click_count')
    list_display = ('title', 'desc', 'link_url', 'publish_date', 'click_count')
    list_display_links = ('title', 'desc', 'link_url', 'publish_date', 'click_count')
    list_filter = ('title',)


admin.site.register(User, AdminUser)
admin.site.register(UserExt, AdminUserExt)
admin.site.register(UserFans, AdminUserFans)
admin.site.register(UserCollectArticle, AdminUserCollectArticle)

admin.site.register(Article, AdminArticle)
admin.site.register(ArticleTag, AdminArticleTag)
admin.site.register(ArticleCategory, AdminArticleCategory)
admin.site.register(ArticleComment, AdminArticleComment)

admin.site.register(Ad, AdminAd)
admin.site.register(Link, AdminLink)




