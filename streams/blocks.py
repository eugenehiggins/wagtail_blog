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


class CardsBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(max_length=100, help_text="Bold title text for this card.")),
                ("text", blocks.TextBlock(max_length=255, help_text="Optional text for this card", required=False)),
                ("image", ImageChooserBlock(help_text="Image will be automagically cropped 570px x 370px")),
                ("link_text", blocks.CharBlock(max_length=50, default="More Detail")),
                ("internal_page", blocks.PageChooserBlock(required=False)),
                ("external_link", blocks.URLBlock(required=False)),
            ]
        )
    )

    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "Standard Cards"
