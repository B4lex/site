# Generated by Django 3.0.6 on 2020-06-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image_ref',
            field=models.TextField(default='Not found.', editable=False),
        ),
    ]
