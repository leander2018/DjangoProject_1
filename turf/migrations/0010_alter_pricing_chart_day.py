# Generated by Django 3.2 on 2021-05-06 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf', '0009_alter_pricing_chart_s_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing_chart',
            name='day',
            field=models.CharField(choices=[('Weekday', 'Weekday'), ('Weekend', 'Weekend'), ('Holiday', 'Holiday'), ('Weekday,Weekend,Holiday', 'Weekday,Weekend,Holiday')], max_length=100),
        ),
    ]