# Generated by Django 3.2 on 2021-04-21 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf', '0003_auto_20210421_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='turf_add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=400)),
                ('turf_nm', models.CharField(max_length=400)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('sports', models.CharField(blank=True, max_length=200)),
                ('contact_no', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]