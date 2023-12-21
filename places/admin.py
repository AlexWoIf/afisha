from django.contrib import admin
from places.models import Place, Image


@admin.register(Place)
class Place(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(Image)