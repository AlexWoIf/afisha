from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from adminsortable2.admin import SortableTabularInline
from django.contrib import admin
from django.utils.html import format_html
from places.models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    extra = 1
    fields = ('image', "get_image_preview", 'order', )
    readonly_fields = ["get_image_preview", ]
    ordering = ['order']

    def get_image_preview(self, obj):
        return format_html(
            '<img src="{url}" style="max-height:200px;max-width:350px;'
            'width: expression(this.width > 350 ? 350: true);" />',
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
            '<img src="{url}" style="max-height:200px; max-width:350px; '
            'width: expression(this.width > 350 ? 350: true);" />',
            url=obj.image.url,
        )
    get_image_preview.short_description = 'Миниатюра картинки'
