# Generated by Django 3.1.1 on 2020-10-16 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_auto_20201015_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='sold_history',
            name='order_no',
            field=models.IntegerField(default=0),
        ),
    ]