# Generated by Django 3.1.1 on 2020-10-13 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_remove_cart_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sold_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('volume', models.IntegerField()),
                ('selling_price', models.FloatField()),
                ('purchase_price', models.FloatField()),
                ('benifit', models.FloatField()),
                ('total', models.FloatField()),
                ('total_quantity', models.IntegerField(default=1)),
            ],
        ),
    ]
