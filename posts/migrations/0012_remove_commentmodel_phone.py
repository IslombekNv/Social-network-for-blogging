# Generated by Django 3.2.4 on 2021-07-04 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_postmodel_blog_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='phone',
        ),
    ]