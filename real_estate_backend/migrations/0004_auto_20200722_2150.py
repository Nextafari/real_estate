# Generated by Django 3.0.8 on 2020-07-22 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_backend', '0003_auto_20200722_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='property_image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
