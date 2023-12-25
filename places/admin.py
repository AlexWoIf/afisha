from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html
from places.models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image', "get_image_preview", 'order', )
    readonly_fields = ["get_image_preview", ]

    def get_image_preview(self, obj):
        return format_html(
            '<img src="{url}" width="{width}" height={height} />',
            url=obj.image.url,
            width=obj.image.width*150/obj.image.height,
            height=150,
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
            '<img src="{url}" width="{width}" height={height} />',
            url=obj.image.url,
            width=obj.image.width*150/obj.image.height,
            height=150,
        )
    get_image_preview.short_description = 'Миниатюра картинки'
