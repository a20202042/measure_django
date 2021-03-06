# Generated by Django 2.0 on 2021-11-29 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_remove_measure_values_measure_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measure_values',
            name='measure_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mysite.project'),
        ),
        migrations.AlterField(
            model_name='measure_values',
            name='measure_tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mysite.measuring_tool'),
        ),
    ]
