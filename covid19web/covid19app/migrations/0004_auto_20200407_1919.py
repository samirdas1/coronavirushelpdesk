# Generated by Django 3.0.5 on 2020-04-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19app', '0003_auto_20200407_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='person_help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=12)),
                ('food', models.BooleanField(default=False)),
                ('sanitizer', models.BooleanField(default=False)),
                ('mask', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='p_help',
        ),
    ]
