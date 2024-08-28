# Generated by Django 5.0.8 on 2024-08-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField(max_length=500)),
                ('attribution', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Testimonal',
                'verbose_name_plural': 'Testimonals',
            },
        ),
    ]
