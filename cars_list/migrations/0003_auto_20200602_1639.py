# Generated by Django 3.0.6 on 2020-06-02 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_list', '0002_car_image_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image_ref',
            field=models.TextField(),
        ),
    ]
