# Generated by Django 3.0.4 on 2020-10-20 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20200922_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='free',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
