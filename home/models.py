from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.api import APIField
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from streams import blocks


class HomePage(Page):
    # body = RichTextField(blank=True)

    body = StreamField([
        ("title", blocks.TitleBlock()),
        ("cards", blocks.CardsBlock()),
        ("image_and_text", blocks.ImageAndTextBlock()),
        ("cta", blocks.CallToActionBlock()),
    ], null=True, blank=True)

    api_fields = [
        APIField('body'),
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]