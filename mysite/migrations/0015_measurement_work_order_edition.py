# Generated by Django 2.0 on 2021-12-01 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_work_order_measure_items_common_difference'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement_work_order',
            name='edition',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]