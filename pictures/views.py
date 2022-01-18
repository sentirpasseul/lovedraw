from django.shortcuts import render
from django.http import HttpResponse
from .models import Picture
from .models import Style
from .models import Artist
from django.template import loader
from django.shortcuts import render
# Create your views here.

def main(request):
    return HttpResponse("Главная страница")

def galleries(request):
    return HttpResponse("Галереи")

def artists(request, artist_id):
    pictures = Picture.objects.filter(artist=artist_id)
    artists = Artist.objects.all()
    current_artist = Artist.objects.get(pk=artist_id)
    context = {'pictures':pictures, 'artists':artists, 'current_artist': current_artist}
    return HttpResponse(request, 'picture/artist.index', context)

def picture(request):
    pictures = Picture.objects.all()
    styles = Style.objects.all()
    artists = Artist.objects.all()
    context = {'pictures':pictures, 'styles': styles, 'artists': artists}
    return render(request, 'picture/index.html', context)

def by_style(request, style_id):
    pictures = Picture.objects.filter(style = style_id)
    styles = Style.objects.all()
    current_style = Style.objects.get(pk=style_id)
    context = {'pictures': pictures, 'styles': styles, 'current_style': current_style}
    return render(request, 'picture/by_style.html', context)