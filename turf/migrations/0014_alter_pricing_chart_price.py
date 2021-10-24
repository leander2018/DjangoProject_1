# Generated by Django 3.2 on 2021-05-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf', '0013_remove_pricing_chart_timing2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing_chart',
            name='price',
            field=models.CharField(choices=[('₹1200/hour', '1200'), ('₹1000/hour', '1000'), ('₹1300/hour', '1300'), ('₹1500/hour', '1500'), ('₹1800/hour', '1800'), ('₹0800/hour', '0800'), ('₹0900/hour', '0900'), ('₹0700/hour', '0700'), ('₹3000/hour', '3000'), ('₹2000/hour', '2000'), ('₹3600/hour', '3600'), ('₹1100/hour', '1100'), ('₹1400/hour', '1400'), ('₹1700/hour', '1700'), ('₹0400/hour', '0400'), ('₹0500/hour', '0500')], max_length=100),
        ),
    ]