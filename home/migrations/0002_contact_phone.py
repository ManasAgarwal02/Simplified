# Generated by Django 3.0.8 on 2020-08-01 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=13),
        ),
    ]
