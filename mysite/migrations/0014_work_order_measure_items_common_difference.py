# Generated by Django 2.0 on 2021-12-01 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_auto_20211129_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_order_measure_items',
            name='common_difference',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
