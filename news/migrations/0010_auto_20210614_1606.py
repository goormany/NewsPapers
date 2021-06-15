# Generated by Django 3.2.2 on 2021-06-14 13:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0009_auto_20210612_2039'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.RemoveField(
            model_name='category',
            name='subscriber',
        ),
        migrations.AddField(
            model_name='category',
            name='category_subscriber',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Подписчик категории'),
        ),
    ]