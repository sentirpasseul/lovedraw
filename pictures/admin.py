from django.contrib import admin

from .models import Picture
from .models import Style

class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'style', 'price', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', )

class StyleAdmin(admin.ModelAdmin):
    list_display = ('style')
    list_display_links = ('style')
    search_fields = ('style')



admin.site.register(Picture, PictureAdmin)
admin.site.register(Style)
# Register your models here.
