from django.utils.safestring import mark_safe
from docutils.core import publish_parts
from wagtail.wagtailcore import blocks


class RSTBlock(blocks.TextBlock):
    """
    A ReSTructured text block for Wagtail streamfields.
    """

    class Meta:
        icon = 'code'

    def render_basic(self, value, context=None):
        return publish_parts(value, writer_name='html')['body']
