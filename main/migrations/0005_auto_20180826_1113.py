# Generated by Django 2.1 on 2018-08-26 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product_hot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='show',
            new_name='active',
        ),
        migrations.AlterField(
            model_name='product',
            name='hot',
            field=models.BooleanField(default=True),
        ),
    ]
