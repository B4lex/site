# Generated by Django 3.0.6 on 2020-06-02 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars_list', '0004_auto_20200602_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='image_ref',
        ),
    ]
