from django import forms
from wagtail.admin import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required=True,
        help_text='Title text to display',
    )

    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = 'Title'
        help_text = "Centered title text to display on the page"


class LinkValue(blocks.StructValue):
    """Additional logic for our links"""

    def url(self):
        internal_page = self.get("internal_page")
        external_link = self.get("external_link")
        if internal_page:
            return internal_page.url
        elif external_link:
            return external_link;
        return ""


class Link(blocks.StructBlock):
    link_text = blocks.CharBlock(
        max_length=50,
        default="More Detail",
    )
    internal_page = blocks.PageChooserBlock(
        required=False,
    )
    external_link = blocks.URLBlock(
        required=False,
    )

    class Meta:
        value_class = LinkValue


class Card(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=100,
        help_text="Bold title text for this card.",
    )
    text = blocks.TextBlock(
        max_length=255,
        help_text="Optional text for this card",
        required=False,
    )
    image = ImageChooserBlock(
        help_text="Image will be automagically cropped 570px x 370px",
    )
    link = Link(help_text="Enter a link or select a page")


class CardsBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        Card()
    )

    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "Standard Cards"


class RadioSelectBlock(blocks.ChoiceBlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field.widget = forms.RadioSelect(
            choices=self.field.widget.choices
        )


class ImageAndTextBlock(blocks.StructBlock):

    image = ImageChooserBlock(help_text='Image will be automagically cropped to 786px by 552px')
    image_alignment = RadioSelectBlock(
        choices=(
            ("float-start", "Image to the left"),
            ("float-end", "Image to the right"),
        ), default='left', help_text='Image on the left with text on the right or vice versa'
    )
    title = blocks.CharBlock(max_length=60, help_text='Max length of 60 characters.')
    text = blocks.CharBlock(max_length=140, required=False)
    link = Link()

    class Meta:
        template = "streams/image_and_text_block.html"
        icon = "image"
        label = "Image & Text"
