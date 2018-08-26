from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=32, verbose_name="产品名")
    details = models.TextField(verbose_name="产品说明")
    font = models.ImageField(verbose_name="产品封面", upload_to='products')
    more_details = RichTextUploadingField(verbose_name="产品详细说明", null=True, blank=True)
    active = models.BooleanField(default=True, verbose_name="显示")
    hot = models.BooleanField(default=True, verbose_name="热门")

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'


class News(models.Model):
    title = models.CharField(max_length=64, verbose_name="标题")
    font = models.ImageField(verbose_name="产品封面", upload_to='news')
    content = models.TextField(verbose_name="新闻短内容")
    more_content = RichTextUploadingField(verbose_name="新闻详细内容", null=True, blank=True)
    date = models.DateField(verbose_name="日期")
    active = models.BooleanField(default=True, verbose_name="显示")
    key_word = models.CharField(max_length=32, verbose_name="关键词", null=True, blank=True)

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻'


class OtherText(models.Model):
    name = models.CharField(max_length=32, verbose_name="所用位置")
    content = models.TextField(verbose_name="内容",null=True,blank=True)
    code = models.IntegerField(default=0,verbose_name="编号",unique=True)

    class Meta:
        verbose_name = '其他文本'
        verbose_name_plural = '其他文本'


class OtherRichText(models.Model):
    name = models.CharField(max_length=32, verbose_name="所用位置")
    content = RichTextUploadingField(verbose_name="内容",null=True,blank=True)
    code = models.IntegerField(default=0,verbose_name="编号",unique=True)

    class Meta:
        verbose_name = '其他富文本'
        verbose_name_plural = '其他富文本'


class OtherImages(models.Model):
    name = models.CharField(max_length=32, verbose_name="所用位置")
    content = models.ImageField(verbose_name="图片", upload_to='other')
    code = models.IntegerField(default=0,verbose_name="编号",unique=True)

    class Meta:
        verbose_name = '其他图片'
        verbose_name_plural = '其他图片'
