from django.db import models
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail import blocks
from wagtail.snippets.blocks import SnippetChooserBlock
from streams.blocks import TitleBlock, CardsBlock, ImageAndTextBlock, CallToActionBlock, PricingTableBlock
# from wagtail.images.apps import ImageChooserPanel
class HomePage(Page):
    parent_page_types = ["wagtailcore.Page"]
    subpage_types = ["flex.FlexPage", "services.ServiceListingPage", "contact.ContactPage"]
    max_count = 1 
    lead_text = models.CharField(
        max_length=140,
        blank=True,
        help_text= "Subheading under the banner-title",
    )
    button = models.ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        related_name="+",
        help_text="Select an optional page to link too",
        on_delete=models.SET_NULL,
    )
    button_text = models.CharField(
        max_length=50,
        blank=False,
        default="Read more",
        help_text="Button text",
    )
    banner_background_video = models.FileField(
        upload_to="videos/",
        null=True,
        blank=True,
        help_text="The banner background video",
    )
    body = StreamField(
        [("title", TitleBlock()),("cards", CardsBlock()),("image_and_text_block", ImageAndTextBlock()),("call_to_action_block", CallToActionBlock()), ("testimonals", SnippetChooserBlock(target_model = "testimonials.Testimonial", template = "streams/testimonial_block.html")),("pricing_table",PricingTableBlock())],
          null =True,
          blank = True)
    
    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        PageChooserPanel("button"),
        FieldPanel("button_text"),
        FieldPanel("banner_background_video"),
        FieldPanel("body"),
    ]

    def save(self, *args, **kwargs):

        key = make_template_fragment_key(
            "home_page_streams",
            [self.id],
        )
        cache.delete(key)

        return super().save(*args, **kwargs)