# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    sex_choices = (
        ('0', '女'),
        ('1', '男'),
        ('2', '未知'),
    )
    marriage_choices = (
        ('0', '未婚'),
        ('1', '已婚'),
        ('2', '离异'),
    )

    occupation_choices = (
        ('0', '士'),
        ('1', '农'),
        ('2', '工'),
        ('3', '商'),
    )

    province_choices = (
        ('0', '北京市'),
        ('1', '天津市'),
        ('2', '上海市'),
        ('3', '重庆市'),
        ('4', '河北省'),
        ('5', '山西省'),
        ('6', '陕西省'),
        ('7', '山东省'),
        ('8', '河南省'),
        ('9', '辽宁省'),
        ('10', '吉林省'),
        ('11', '黑龙江省'),
        ('12', '江苏省'),
        ('13', '浙江省'),
        ('14', '安徽省'),
        ('15', '江西省'),
        ('16', '福建省'),
        ('17', '湖北省'),
        ('19', '湖南省'),
        ('20', '四川省'),
        ('21', '贵州省'),
        ('22', '云南省'),
        ('23', '广东省'),
        ('24', '青海省'),
        ('25', '海南省'),
        ('26', '甘肃省'),
        ('27', '台湾省'),
        ('28', '广西壮族自治区'),
        ('29', '内蒙古自治区'),
        ('30', '新疆维吾尔自治区'),
        ('31', '西藏自治区'),
        ('32', '宁夏回族自治区'),
        ('33', '香港特别行政区'),
        ('34', '澳门特别行政区'),
    )

    city_choices = (
        ('0', '石家庄'),
        ('1', '张家口'),
        ('2', '唐山'),
        ('3', '秦皇岛'),
        ('4', '邯郸'),
        ('5', '邢台'),
        ('6', '保定'),
        ('7', '承德'),
        ('8', '沧州'),
        ('9', '廊坊'),
        ('10', '衡水'),
        ('11', '太原'),
        ('12', '大同'),
        ('13', '阳泉'),
        ('14', '长治'),
        ('15', '晋城'),
        ('16', '朔州'),
        ('17', '晋中'),
        ('18', '运城'),
        ('19', '忻州'),
        ('20', '临汾'),
        ('21', '吕梁'),
        ('22', '呼和浩特'),
        ('23', '包头'),
        ('24', '乌海'),
        ('25', '赤峰'),
        ('26', '通辽'),
        ('27', '鄂尔多斯'),
        ('28', '呼伦贝尔'),
        ('29', '巴彦淖尔'),
        ('30', '乌兰察布'),
        ('31', '兴安'),
        ('32', '锡林郭勒'),
        ('33', '阿拉善'),
        ('34', '南京'),
        ('35', '无锡'),
        ('36', '苏州'),
        ('37', '常州'),
        ('38', '镇江'),
        ('39', '南通'),
        ('40', '泰州'),
        ('41', '扬州'),
        ('42', '盐城'),
        ('43', '淮安'),
        ('44', '宿迁'),
        ('45', '连云港'),
        ('46', '徐州'),
        ('47', '杭州'),
        ('48', '宁波'),
        ('49', '温州'),
        ('50', '嘉兴'),
        ('51', '湖州'),
        ('52', '绍兴'),
        ('53', '金华'),
        ('54', '衢州'),
        ('55', '舟山'),
        ('56', '台州'),
        ('57', '丽水'),
    )

    # name = models.CharField('姓名', max_length=64)
    # email = models.EmailField('邮件', null=True, blank=True)
    # join_date = models.DateTimeField('加入博客时间')

    sex = models.CharField('性别', max_length=1, choices=sex_choices)
    birth = models.DateField('生日', null=True, blank=True)
    mobile = models.CharField('手机', max_length=11, unique=True, null=True, blank=True)
    qq = models.CharField('QQ', max_length=12, unique=True, null=True, blank=True)
    image = models.ImageField('头像', max_length=200, upload_to='image/avatar/%Y/%m/%d',
                              default='image/avatar/default.jpg', null=True, blank=True)
    profile = models.TextField('个人简介', null=True, blank=True)

    marriage = models.CharField('婚姻状况', max_length=1, choices=marriage_choices, null=True, blank=True)
    occupation = models.CharField('职业', max_length=1, choices=occupation_choices, null=True, blank=True)
    home_province = models.CharField('省', max_length=2, choices=province_choices, null=True, blank=True)
    home_city = models.CharField('市', max_length=3, choices=city_choices, null=True, blank=True)

    last_log_in_date = models.DateTimeField('上次登录时间', auto_now=True)

    school = models.CharField('学校', max_length=32, null=True, blank=True)
    profession = models.CharField('专业', max_length=32, null=True, blank=True)
    school_date = models.DateField('入学时间', null=True, blank=True)

    company = models.CharField('公司', max_length=32, null=True, blank=True)
    position = models.CharField('职位', max_length=32, null=True, blank=True)
    work_date = models.DateField('入职时间', null=True, blank=True)

    # collect_articles = models.ManyToManyField(Article, verbose_name='收藏文章')

    def __str__(self):
        return str(self.id) + '(' + self.username + ')'

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']


class ArticleCategory(models.Model):
    category = models.CharField('分类', max_length=10)
    user_id = models.ForeignKey(User, verbose_name='用户ID')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['id']


class ArticleTag(models.Model):
    tag = models.CharField('标签', max_length=32)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['id']


class Article(models.Model):
    channel_choices = (
        ('0', '新闻'),
        ('1', '体育'),
        ('2', '财经'),
        ('3', '娱乐'),
        ('4', '科技'),
        ('5', '博客'),
        ('6', '图片'),
        ('7', '育儿'),
        ('8', '文史'),
        ('9', '女性'),
    )

    title = models.CharField('题目', max_length=64)
    desc = models.CharField('描述', max_length=128)
    content = models.TextField('内容')
    publish_date = models.DateTimeField('发表时间', auto_now_add=True)
    is_recommend = models.BooleanField('是否推荐', default=False)
    read_count = models.IntegerField('阅读次数', default=0)
    collect_count = models.IntegerField('收藏次数', default=0)
    reprint_count = models.IntegerField('转载', default=0)

    channel = models.CharField('频道', max_length=2, choices=channel_choices, default='4')

    user_id = models.ForeignKey(User, verbose_name='用户')
    category_id = models.ForeignKey(ArticleCategory, verbose_name='分类')
    tag_id = models.ManyToManyField(ArticleTag, verbose_name='标签')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-publish_date']


class ArticleComment(models.Model):
    content = models.CharField('内容', max_length=64)
    publish_date = models.DateTimeField('评论时间', auto_now_add=True)
    article_id = models.ForeignKey(Article, verbose_name='文章ID')
    user_id = models.ForeignKey(User, verbose_name='用户ID')
    p_id = models.ForeignKey('self', null=True, blank=True, verbose_name='父级评论')

    def __str__(self):
        return self.content[:10] + '...'

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-publish_date']


class UserCollectArticle(models.Model):
    user_id = models.ForeignKey(User, verbose_name='用户ID')
    article_id = models.ForeignKey(Article, verbose_name='文章ID')

    def __str__(self):
        return str(self.user_id) + '收藏文章:' + str(self.article_id)

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name
        ordering = ['id']


class UserFans(models.Model):
    user_id = models.ForeignKey(User, verbose_name='用户ID', related_name='userfans_user')
    fans_id = models.ForeignKey(User, verbose_name='粉丝ID', related_name='userfans_fans')

    def __str__(self):
        return str(self.user_id) + '粉丝:' + str(self.fans_id)

    class Meta:
        verbose_name = '粉丝'
        verbose_name_plural = verbose_name
        ordering = ['id']


class UserExt(models.Model):
    user_id = models.ForeignKey(User, verbose_name='用户ID', related_name='userext_user')
    guest_id = models.ForeignKey(User, verbose_name='访客ID', related_name='userext_guest')
    is_message = models.BooleanField('是否留言', default=False)
    message = models.TextField('留言', blank=True)

    def __str__(self):
        if self.is_message:
            return str(self.guest_id) + '留言:' + self.message
        else:
            return str(self.guest_id) + '来访'

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name
        ordering = ['id']


class Ad(models.Model):
    title = models.CharField('标题', max_length=32)
    desc = models.CharField('描述', max_length=64)
    image_url = models.ImageField('图片地址', upload_to='image/ad/%Y/%m/%d', default='image/ad/default.jpg')
    link_url = models.URLField('链接地址')
    publish_date = models.DateTimeField('发表时间', auto_now_add=True)
    click_count = models.IntegerField('点击次数', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name
        ordering = ['-click_count']


class Link(models.Model):
    title = models.CharField('标题', max_length=32)
    desc = models.CharField('描述', max_length=64)
    link_url = models.CharField('链接地址', max_length=64)
    publish_date = models.DateTimeField('发表时间', auto_now_add=True)
    click_count = models.IntegerField('使用次数', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['-click_count']
