# Generated by Django 5.0.8 on 2024-08-23 15:24

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_homepage_banner_background_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('title', 1)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Text to display', 'required': True}), 1: ('wagtail.blocks.StructBlock', [[('text', 0)]], {})}, null=True),
        ),
    ]
