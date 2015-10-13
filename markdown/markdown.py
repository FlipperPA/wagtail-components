from django.utils.safestring import mark_safe
from markdown import markdown
from wagtail.wagtailcore import blocks


class MarkDownBlock(blocks.TextBlock):
    """
    A MarkDown block for Wagtail streamfields.
    """

    class Meta:
        icon = 'code'

    def render_basic(self, value):
        md = markdown(
            value,
            [
                'markdown.extensions.fenced_code',
                'codehilite',
            ],
        )
        return mark_safe(md)
