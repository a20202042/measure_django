# Generated by Django 2.0 on 2021-12-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0019_work_order_appearance_defect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_order_appearance_defect',
            name='base64_image',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
