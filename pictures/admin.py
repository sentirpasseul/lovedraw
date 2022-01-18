from django.contrib import admin

from .models import Picture
from .models import Style
from .models import Artist

class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'style', 'price', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', )

class StyleAdmin(admin.ModelAdmin):
    list_display = ('style')
    list_display_links = ('style')
    search_fields = ('style')

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('artist')
    list_display_links = ('artist')
    search_fields = ('artist')

admin.site.register(Artist)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Style)
# Register your models here.
