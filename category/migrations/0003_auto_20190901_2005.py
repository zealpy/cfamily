# Generated by Django 2.2 on 2019-09-01 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20190901_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='meta_title',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
