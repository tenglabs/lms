# Generated by Django 3.0.4 on 2020-09-22 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_lesson_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cover_image',
            field=models.ImageField(null=True, upload_to='cover'),
        ),
    ]
