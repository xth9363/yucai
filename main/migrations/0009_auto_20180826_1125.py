# Generated by Django 2.1 on 2018-08-26 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_otherimages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': '新闻', 'verbose_name_plural': '新闻'},
        ),
        migrations.AlterModelOptions(
            name='otherimages',
            options={'verbose_name': '其他图片', 'verbose_name_plural': '其他图片'},
        ),
        migrations.AlterModelOptions(
            name='othertext',
            options={'verbose_name': '其他文本', 'verbose_name_plural': '其他文本'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '产品', 'verbose_name_plural': '产品'},
        ),
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateField(default=None, verbose_name='日期'),
            preserve_default=False,
        ),
    ]