# Generated by Django 3.1.7 on 2021-03-08 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bazzar', '0007_auto_20210308_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payed_on',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='price',
        ),
    ]
