# Generated by Django 5.0.8 on 2024-08-20 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicepage',
            old_name='decription',
            new_name='description',
        ),
    ]
