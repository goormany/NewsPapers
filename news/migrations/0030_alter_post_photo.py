# Generated by Django 3.2.2 on 2021-06-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0029_alter_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, default='/photos/def/1.jpg/', upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
