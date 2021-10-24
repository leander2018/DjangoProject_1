# Generated by Django 3.2 on 2021-04-21 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='turf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turf_name', models.CharField(max_length=400)),
                ('address', models.CharField(max_length=500)),
                ('location', models.CharField(blank=True, max_length=400)),
                ('image1', models.ImageField(upload_to='images/')),
                ('image2', models.ImageField(upload_to='images/')),
                ('image3', models.ImageField(upload_to='images/')),
                ('contact_no', models.CharField(max_length=50)),
                ('s1', models.CharField(blank=True, max_length=50)),
                ('s2', models.CharField(blank=True, max_length=50)),
                ('s3', models.CharField(blank=True, max_length=50)),
                ('s4', models.CharField(blank=True, max_length=50)),
                ('s5', models.CharField(blank=True, max_length=50)),
                ('s_count', models.IntegerField(blank=True, default=1)),
                ('g1', models.CharField(blank=True, max_length=50)),
                ('g2', models.CharField(blank=True, max_length=50)),
                ('g3', models.CharField(blank=True, max_length=50)),
                ('g4', models.CharField(blank=True, max_length=50)),
                ('g_count', models.IntegerField(blank=True, default=1)),
            ],
        ),
    ]