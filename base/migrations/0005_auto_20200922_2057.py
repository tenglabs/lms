# Generated by Django 3.0.4 on 2020-09-22 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20200922_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='ci_res',
            new_name='cover_image',
        ),
    ]
