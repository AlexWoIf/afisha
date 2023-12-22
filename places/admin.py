from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html
from places.models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image', "get_preview", 'order', )
    readonly_fields = ["get_preview", ]

    def get_preview(self, obj):
        return format_html(
            '<img src="{url}" width="{width}" height={height} />',
            url=obj.image.url,
            width=obj.image.width*150/obj.image.height,
            height=150,
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', )
    inlines = [ImageInline, ]
