# Generated by Django 2.2 on 2019-08-29 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0004_auto_20190829_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='start_date',
        ),
    ]