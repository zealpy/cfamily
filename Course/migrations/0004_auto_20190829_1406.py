# Generated by Django 2.2 on 2019-08-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0003_auto_20190829_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='discountcoupon',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='discountcoupon',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
