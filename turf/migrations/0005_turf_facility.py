# Generated by Django 3.2 on 2021-04-22 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turf', '0004_turf_add'),
    ]

    operations = [
        migrations.CreateModel(
            name='turf_facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(max_length=200)),
                ('f2', models.CharField(max_length=200)),
                ('f3', models.CharField(max_length=200)),
                ('f4', models.CharField(max_length=200)),
                ('f5', models.CharField(max_length=200)),
                ('f6', models.CharField(max_length=200)),
                ('f7', models.CharField(max_length=200)),
                ('f8', models.CharField(max_length=200)),
                ('f_count', models.IntegerField(default=1)),
                ('turf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turf.turf')),
            ],
        ),
    ]
