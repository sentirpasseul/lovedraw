from django.urls import path

from .views import main
from .views import picture, by_style

urlpatterns = [
    path('<int:style_id>/', by_style, name = 'by_style'),
    path('', picture, name = 'picture')
]