# Generated by Django 2.0 on 2021-12-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0022_auto_20211207_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_order_appearance_defect',
            name='base64_image',
            field=models.TextField(blank=True, max_length=1000000),
        ),
    ]
