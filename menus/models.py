from django.db import models
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from wagtail.admin.panels import FieldPanel, PageChooserPanel, InlinePanel
from django_extensions.db.fields import AutoSlugField
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable
# Create your models here.

class MenuItem(Orderable):
    link_title= models.CharField(
        max_length  =30,
        blank=True,
        help_text= "Enter menu-item names upto 30 characters"
    )
    link_url = models.CharField(
        max_length=500,
        blank=True,
        )
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name="+",
        on_delete= models.CASCADE,
      )
    open_in_new_tab = models.BooleanField(
        default=False,
        blank=True,
    )
    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_page"),
        PageChooserPanel("link_url"),
        FieldPanel("open_in_new_tab"),
    ]
    page = ParentalKey("Menu", related_name="menu_items")

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        else:
            return "#"
        

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return "Missing Title"
    

    
class Menu(ClusterableModel):
    title = models.CharField(
        max_length = 60,
        help_text ="title upto 60 characters.",
        )
    slug = AutoSlugField(
        populate_from = "title",
        editable = True,
    )
    panels = [
        FieldPanel("title"),
        FieldPanel("slug"),
        InlinePanel("menu_items", label = "Menu Item"),
    ]
    def __str__(self):
        return self.title
    
    def save(self, *args,**kwargs):

        key = make_template_fragment_key(
            "site_header",
        )
        cache.delete(key)

        key = make_template_fragment_key(
            "site_footer",
        )
        cache.delete(key)

        return super().save(*args,**kwargs)
    