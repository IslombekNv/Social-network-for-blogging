# Generated by Django 3.2.4 on 2021-06-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_title_categorymodel_title2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttagmodel',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
    ]