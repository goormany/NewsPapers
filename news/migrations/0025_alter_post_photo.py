# Generated by Django 3.2.2 on 2021-06-17 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0024_alter_post_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='photos/def/placeholder.png', upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]