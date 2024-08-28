from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from django import forms
from wagtail.contrib.table_block.blocks import TableBlock
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList

class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required=True,
        help_text="Text to display",
    )
    class Meta:
        template = "streams/title_block.html"
        label = "Title" 
        icon = "edit"
        help_text = "Centered text to display on the page."

class LinkValue(blocks.StructValue):
       """Addtitional logic for links """
       def url(self) -> str:
              internal_page = self.get("internal_page")
              external_page = self.get("external_page")
              if internal_page:
                     return internal_page.url
              elif external_page:
                     return external_page
              return ""
       
class link(blocks.StructBlock):
              link_text = blocks.CharBlock(
                max_length=50,
                default="More details")
              internal_page = blocks.PageChooserBlock(required=False)
              external_page = blocks.URLBlock(required=False)

              class Meta:
                   value_class = LinkValue

              def clean(self, value):
                     internal_page = value.get("internal_page")
                     external_page = value.get("external_page")
                     errors = {}
                     if internal_page and external_page:
                            errors["internal_page"] = ErrorList()
                            errors["external_page"] = ErrorList()

                     elif internal_page and external_page:
                            errors["internal_page"] = ErrorList()
                            errors["external_page"] = ErrorList()
                     
                     if errors:
                            raise ValidationError("Link is required, select only one Type of link", params=errors)
                     return super().clean(value)
              

class card( blocks.StructBlock):
            title= blocks.CharBlock(
                max_length=100,
                help_text="Bold title text for the card. Max length of 100 characters.")
            text =blocks.TextBlock(
                max_length=255,
                help_text="Optional text for the card. Max length of 255 characters.",
                required=False)
            image = ImageChooserBlock(
                help_text="Image will be automatically cropped to 570px by 370px")
            link = link(help_text= "Enter your link details here.")


class CardsBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
          card()
           
    )
    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "Standard Cards"



class RadioSelectBlock(blocks.ChoiceBlock):
       def __init__(self, *args, **kwargs):
              super().__init__(*args, **kwargs)
              self.field.widget = forms.RadioSelect(
                     choices= self.field.widget.choices
              )



class ImageAndTextBlock(blocks.StructBlock):
       image = ImageChooserBlock(help_text = "Image will be cropped to 786px by 552px")
       image_alignment = RadioSelectBlock(
              choices = (
                     ("left", "Image to the left"),
                     ("right", "Image to the right"),
              ),
              default= "left",
              help_text ="Image on the left with text on the right. Or image  on the right with text on the left"
       )
       title = blocks.CharBlock(
              max_length = 60,
              help_text = "Max length 60 characters",
       )
       text = blocks.CharBlock(
              required = True,
              max_length = 140,
              help_text = "Description upto 140 charaters",
       )
       link = link()

       class Meta:
              template = "streams/image_and_text_block.html"
              icon = "image"
              label = "Image & Text"

class CallToActionBlock(blocks.StructBlock):
       title = blocks.CharBlock(
              max_length = 200,
              blank = True,
              null = True,
              help_text="max length of 200",
                                )
       link = link()

       class Meta:
              template = "streams/call_to_action_block.html"
              label = "Call to Action"
              icon = "plus"

class PricingTableBlock(TableBlock):
#     table = TableBlock()
    pass
    


    class Meta:
           template = "streams/pricing_table_block.html"
           label= "Pricing Table"
           icon = "table"
           help_text = "Your pricing table should include x columns"



class RichTextBlock(blocks.StructBlock):
       title = blocks.CharBlock(
              required = False,
              max_length = 200,
              null = True,
              blank = True,
              help_text = "Enter the title for richtext upto 200 characters"
       )
       content = blocks.RichTextBlock(

       )

       class Meta:
              template = 'streams/rich_text_block.html'
              label = "Richtext Block"