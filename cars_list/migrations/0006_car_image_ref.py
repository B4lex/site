# Generated by Django 3.0.6 on 2020-06-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_list', '0005_remove_car_image_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image_ref',
            field=models.TextField(null=True),
        ),
    ]
