# Generated by Django 2.0 on 2021-12-14 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0029_work_order_parts_reamke'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='batch_number',
        ),
    ]
