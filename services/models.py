from django.db import models
from django.core.exceptions import ValidationError
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel
class ServiceListingPage(Page):
    parent_page_types = ["home.HomePage"]
    max_count = 1
    subtitle = models.TextField(
        blank=True,
        max_length =500,
    )
    service_bg_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="This image will be used as background.",
        related_name="+"
    )
    
    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
         FieldPanel("service_bg_image"),

    ]
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["services"] = ServicePage.objects.live().public()
        return context

class ServicePage(Page):
    parent_page_types = ["services.ServiceListingPage"]
    description = models.CharField(
        blank=True,
        max_length=500,
    )
    description_short = models.CharField(
        blank=True,
        max_length=500,
    )
    internal_page = models.ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        related_name="+",
        help_text="select an internal page",
        on_delete=models.SET_NULL,
    )
    external_page = models.URLField(
        blank=True,
    )
    button_text = models.CharField(
        blank=True,
        max_length=50,
    )
    service_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="This image will be used on service listing page and will be crop to 570px by 370px",
        related_name="+"
    )
    service_bg_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="This image will be used as background.",
        related_name="+"
    )
    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("description_short"),
        PageChooserPanel("internal_page"),
        FieldPanel("external_page"),
        FieldPanel("button_text"),
        FieldPanel("service_image"),
        FieldPanel("service_bg_image"),
    ]
    def clean(self):
        super().clean()
        if self.internal_page and self.external_page:
            raise ValidationError({
            "internal_page":ValidationError("Please select only a page or enter a external link"),
            "external_page":ValidationError("Please select only a page or enter a external link"),
        })