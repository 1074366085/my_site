from django.db import models


# Create your models here.
class Article(models.Model):
    slug = models.SlugField('唯一标识', unique=True, max_length=255, default='slug_input_default(请修改)')
    author = models.CharField(max_length=255, verbose_name='作者')
    title = models.CharField(max_length=200, verbose_name='标题')
    excerpt = models.TextField('摘要', default='请输入文章摘要...')
    fb_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    content = models.TextField(verbose_name='内容', default='请输入文章内容...')
