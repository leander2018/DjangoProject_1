# Generated by Django 3.2 on 2021-05-06 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf', '0007_pricing_chart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing_chart',
            name='price',
            field=models.CharField(choices=[('₹1200/hour', '₹1200/hour'), ('₹1000/hour', '₹1000/hour'), ('₹1300/hour', '₹1300/hour'), ('₹1500/hour', '₹1500/hour'), ('₹1800/hour', '₹1800/hour'), ('₹800/hour', '₹800/hour'), ('₹900/hour', '₹900/hour'), ('₹700/hour', '₹700/hour'), ('₹3000/hour', '₹3000/hour'), ('₹2000/hour', '₹2000/hour'), ('₹3600/hour', '₹3600/hour'), ('₹1100/hour', '₹1100/hour'), ('₹1400/hour', '₹1400/hour'), ('₹1700/hour', '₹1700/hour'), ('₹400/hour', '₹400/hour'), ('₹500/hour', '₹500/hour')], max_length=100),
        ),
    ]
