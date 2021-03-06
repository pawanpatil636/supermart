# Generated by Django 3.1.7 on 2021-03-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('grocery', 'grocery'), ('food', 'food')], max_length=10)),
                ('availability', models.BooleanField(default=True)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
