# Generated by Django 3.2 on 2021-05-06 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf', '0008_alter_pricing_chart_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing_chart',
            name='s_type',
            field=models.CharField(choices=[('Football', 'Football'), ('Cricket', 'Cricket'), ('Football & Cricket', 'Football & Cricket')], max_length=100),
        ),
    ]
