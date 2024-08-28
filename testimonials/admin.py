from django.db import models
from wagtail_modeladmin.options import (
    ModelAdmin, modeladmin_register
)
from .models import Testimonial

@modeladmin_register
class TestimonialAdmin(ModelAdmin):
    """Testimonial admin"""

    model = Testimonial
    menu_label = "Testimonials"
    menu_icon = "placeholder"
    menu_order = 200
    add_to_settings_menu = False 
    exclude_from_explorer = False
    list_display = ("quote", "attribution")
    search_fields = ("quote", "attribution")
