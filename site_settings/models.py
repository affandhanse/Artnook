from django.db import models
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import RichTextField
# Create your models here.

@register_setting
class HoursSettings(BaseSiteSetting):
    hours = models.CharField(
        max_length= 50,
        help_text = "working hours max characters 50."
    )

    contents = [
        FieldPanel("hours"),
    ]
    def save(self, *args, **kwargs):
        key = make_template_fragment_key(
            "footer_hours_settings",
        )
        cache.delete(key)
        return super().save(*args, **kwargs)

@register_setting
class ContactSettings(BaseSiteSetting):
    contact =RichTextField(
        blank=True,
        null = True,
        features=["link"],
    )
    contents = [
        FieldPanel("contact"),
    ]
    def save(self, *args, **kwargs):
        key = make_template_fragment_key(
            "footer_contact_settings",
        )
        cache.delete(key)
        return super().save(*args, **kwargs)

@register_setting
class SocialMediaSettings(BaseSiteSetting):
    facebook = models.URLField(
        blank=True,
        help_text = "Enter your URL"
    )
    twitter = models.URLField(
        blank=True,
        help_text = "Enter your URL"
    )
    instagram = models.URLField(
        blank=True,
        help_text = "Enter your URL"
    ) 
    youtube = models.URLField(
        blank=True,
        help_text = "Enter your URL"
    )
    panels = [
        FieldPanel("facebook"),
        FieldPanel("twitter"),
        FieldPanel("instagram"),
        FieldPanel("youtube"),
    ]

    def save(self, *args, **kwargs):

        key = make_template_fragment_key(
            "footer_social_media_settings",
        )
        cache.delete(key)


        return super().save(*args, **kwargs)
    

@register_setting
class FooterCTASettings(BaseSiteSetting):
    title=models.CharField(max_length=100)
    subtitle = models.TextField(max_length=250)
    button_text = models.CharField(max_length=50, default="Contact Us")
    button_internal_page = models.ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Select a internal page. ",
    )
    button_external_page = models.URLField(
        blank = True,
        null=True,
        help_text = "Enter the link to external page.(either internal or external page allowed)"
    )
    panels = [
        FieldPanel("title"),
        FieldPanel("subtitle"),
        FieldPanel("button_text"),
        PageChooserPanel("button_internal_page"),
        FieldPanel("button_external_page"),
    ]
    
    def save(self, *args, **kwargs):

        key = make_template_fragment_key(
            "footer_cta_settings",
        )
        cache.delete(key)


        return super().save(*args, **kwargs)