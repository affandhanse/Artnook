# Generated by Django 5.0.8 on 2024-08-20 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_servicepage_service_bg_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicepage',
            old_name='service_bg_image',
            new_name='background_image',
        ),
    ]
