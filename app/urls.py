from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('cadastro', views.cadastrar, name ='cadastro'),
    path('lista', views.listar, name='lista')
]#+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 