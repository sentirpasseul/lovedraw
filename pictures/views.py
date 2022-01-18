from django.shortcuts import render
from django.http import HttpResponse
from .models import Picture
from .models import Style
from django.template import loader
from django.shortcuts import render
# Create your views here.

def main(request):
    return HttpResponse("Главная страница")

def galleries(request):
    return HttpResponse("Галереи")

def artists(request):
    return HttpResponse("Художники")

def picture(request):
    pictures = Picture.objects.all()
    styles = Style.objects.all()
    context = {'pictures':pictures, 'styles': styles,}
    return render(request, 'picture/index.html', context)

def by_style(request, style_id):
    pictures = Picture.objects.filter(style = style_id)
    styles = Style.objects.all()
    current_style = Style.objects.get(pk=style_id)
    context = {'pictures': pictures, 'styles': styles, 'current_style': current_style}
    return render(request, 'picture/by_style.html', context)