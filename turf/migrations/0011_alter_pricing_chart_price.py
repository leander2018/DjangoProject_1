# Generated by Django 3.2 on 2021-05-06 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf', '0010_alter_pricing_chart_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing_chart',
            name='price',
            field=models.CharField(choices=[('₹1200/hour', '1200'), ('₹1000/hour', '1000'), ('₹1300/hour', '1300'), ('₹1500/hour', '1500'), ('₹1800/hour', '1800'), ('₹800/hour', '800'), ('₹900/hour', '900'), ('₹700/hour', '700'), ('₹3000/hour', '3000'), ('₹2000/hour', '2000'), ('₹3600/hour', '3600'), ('₹1100/hour', '1100'), ('₹1400/hour', '1400'), ('₹1700/hour', '1700'), ('₹400/hour', '400'), ('₹500/hour', '500')], max_length=100),
        ),
    ]
