# Generated by Django 2.1 on 2018-08-26 12:17

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20180826_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherrichtext',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='othertext',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='内容'),
        ),
    ]
