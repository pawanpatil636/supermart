# Generated by Django 3.1.7 on 2021-03-06 04:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bazzar', '0003_address_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='expiry_date',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bazzar.address'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='1', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='cvv',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('payed_on', models.DateField()),
                ('payment_id', models.CharField(max_length=30)),
                ('card_holder', models.CharField(max_length=50)),
                ('card_number', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('expiry_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]