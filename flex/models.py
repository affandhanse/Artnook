from wagtail.models import Page
from django.db import models
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail import blocks
from wagtail import blocks as wagtail_blocks
from wagtail.snippets.blocks import SnippetChooserBlock
from streams.blocks import TitleBlock, CardsBlock, ImageAndTextBlock, CallToActionBlock, PricingTableBlock, RichTextBlock


class FlexPage(Page):
    parent_page_types = ["home.HomePage", "flex.FlexPage"]
    body = StreamField(
        [("title", TitleBlock()),
         ("cards", CardsBlock()),
         ("image_and_text_block", ImageAndTextBlock()),
         ("call_to_action_block", CallToActionBlock()),
         ("testimonals", SnippetChooserBlock(
               target_model = "testimonials.Testimonial",
                 template = "streams/testimonial_block.html")),
         ("pricing_table",PricingTableBlock()), 
         ("richtext",RichTextBlock()),
        ],
          null =True,
          blank = True)
     
    content_panels = Page.content_panels +[
            FieldPanel("body"),
     ]
    
    class Meta:
        verbose_name ="Flex (Misc) page"
        verbose_name_plural ="Flex (Misc) pages"
