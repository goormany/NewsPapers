# Generated by Django 3.2.2 on 2021-06-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0021_auto_20210616_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]