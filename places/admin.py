from django.contrib import admin
from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

@admin.register(Place)
class Place(admin.ModelAdmin):
    list_display = ('title', )
    inlines = [ImageInline]


admin.site.register(Image)
