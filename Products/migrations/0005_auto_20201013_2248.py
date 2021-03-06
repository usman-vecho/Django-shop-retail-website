# Generated by Django 3.1.1 on 2020-10-13 17:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_sold_history'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sold_history',
            old_name='total_quantity',
            new_name='total_quantity_sold',
        ),
        migrations.AddField(
            model_name='sold_history',
            name='sold_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
