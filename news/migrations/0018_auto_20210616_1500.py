# Generated by Django 3.2.2 on 2021-06-16 12:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0017_alter_category_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='data_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='-', upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='post',
            name='public',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]