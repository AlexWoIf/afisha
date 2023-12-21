from django.contrib import admin
from places.models import Place

@admin.register(Place)
class Place(admin.ModelAdmin):
    list_display = ('title', )