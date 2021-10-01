# Generated by Django 3.2.4 on 2021-06-26 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_profilemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='facebook',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='facebook'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='instagram',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='instagram'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='twitter',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='twitter'),
        ),
    ]