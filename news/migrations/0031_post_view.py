# Generated by Django 3.2.2 on 2021-06-18 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0030_alter_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
