# Generated by Django 3.1.7 on 2021-03-05 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bazzar', '0002_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_number', models.IntegerField()),
                ('appartment_name', models.CharField(max_length=50)),
                ('street_name', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('grocery', 'grocery'), ('food', 'food')], max_length=10)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=30)),
                ('card_number', models.IntegerField()),
                ('expiry_date', models.DateField()),
                ('cvv', models.IntegerField(max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]