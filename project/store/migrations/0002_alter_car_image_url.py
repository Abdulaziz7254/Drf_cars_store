# Generated by Django 5.0.6 on 2024-07-08 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image_url',
            field=models.ImageField(upload_to=''),
        ),
    ]
