# Generated by Django 2.1 on 2018-08-26 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180826_1113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': ('产品',), 'verbose_name_plural': '产品'},
        ),
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True, verbose_name='显示'),
        ),
        migrations.AlterField(
            model_name='product',
            name='hot',
            field=models.BooleanField(default=True, verbose_name='热门'),
        ),
    ]