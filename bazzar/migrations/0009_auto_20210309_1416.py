# Generated by Django 3.1.7 on 2021-03-09 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazzar', '0008_auto_20210308_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='card_number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cvv',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ordered', 'ordered'), ('approve', 'approve'), ('processing', 'processing'), ('billing', 'billing'), ('shipping', 'shipping'), ('dispatched', 'dispatched'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='ordered', max_length=20),
        ),
    ]
