# Generated by Django 3.2.2 on 2021-07-15 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0039_auto_20210715_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category_id_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category_id_ru',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text_ru',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_ru',
        ),
    ]
