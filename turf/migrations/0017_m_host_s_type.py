# Generated by Django 3.2 on 2021-06-28 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf', '0016_m_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='m_host',
            name='s_type',
            field=models.CharField(default=0, max_length=100),
        ),
    ]