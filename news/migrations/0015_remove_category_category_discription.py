# Generated by Django 3.2.2 on 2021-06-14 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_alter_category_category_discription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_discription',
        ),
    ]