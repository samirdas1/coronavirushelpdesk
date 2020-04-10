# Generated by Django 3.0.5 on 2020-04-07 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19app', '0004_auto_20200407_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='ngo_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_name', models.CharField(max_length=50)),
                ('ngo_district', models.CharField(max_length=30)),
                ('ngo_state', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=50)),
            ],
        ),
    ]
