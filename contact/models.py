from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from modelcluster.fields import ParentalKey
from wagtail.fields import RichTextField

# Create your models here.

class FormField(AbstractFormField):
    page = ParentalKey(
        "ContactPage",
        on_delete = models.CASCADE,
        related_name = "form_fields",
    )



class ContactPage(AbstractEmailForm):

    template = "contact/contact_page.html"
    landing_page_template = "contact/contact_page_landing.html"
    subpage_types = []
    max_count = 1
    intro = RichTextField(blank = True, features=["bold","ul","ol","link"])
    thank_you_text = RichTextField(blank=True, features=["bold","link","ol","ul"])
    map_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text= "The image will be cropped to 580px by 355px",
        related_name="+"
    )
    map_url = models.URLField(
        blank=True,
        null=True,
        help_text="if you provide a link here the map_image will become a link.",
    )

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("intro"),
        FieldPanel("map_image"),
        FieldPanel("map_url"),
        InlinePanel("form_fields", label = "Form Fields"),
        FieldPanel("thank_you_text"),
        FieldPanel("to_address"),
        FieldPanel("from_address"),
        FieldPanel("subject"),

    ]