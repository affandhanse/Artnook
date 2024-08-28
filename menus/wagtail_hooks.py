from wagtail_modeladmin.options import (
    ModelAdmin, modeladmin_register
)
from .models import Menu

class MenuAdmin(ModelAdmin):
    model = Menu
    menu_label = "Menus"
    icon = "list-ul"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False

modeladmin_register(MenuAdmin)