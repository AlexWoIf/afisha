from adminsortable2.admin import SortableAdminBase, SortableTabularInline
from django.contrib import admin
from django.utils.html import format_html

from places.models import Image, Place


PREVIEW_MAX_HEIGHT = '350px'
PREVIEW_MAX_WIDTH = '200px'


class ImageInline(SortableTabularInline):
    model = Image
    extra = 1
    fields = ('image', "get_image_preview", 'order', )
    readonly_fields = ["get_image_preview", ]
    ordering = ['order']

    def get_image_preview(self, obj):
        return format_html(
            '<img src="{url}" style="max-height: '
            f'{PREVIEW_MAX_HEIGHT}; max-width: {PREVIEW_MAX_WIDTH};" /> ',
            url=obj.image.url,
        )
    get_image_preview.short_description = 'Миниатюра картинки'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['title', ]
    search_fields = ['title', ]
    inlines = [ImageInline, ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['place', 'order', ]
    autocomplete_fields = ['place', ]
    readonly_fields = ["get_image_preview", ]

    def get_image_preview(self, obj):
        return format_html(
            '<img src="{url}" style="max-height: '
            f'{PREVIEW_MAX_HEIGHT}; max-width: {PREVIEW_MAX_WIDTH};" /> ',
            url=obj.image.url,
        )
    get_image_preview.short_description = 'Миниатюра картинки'
