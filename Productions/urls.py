from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = "Productions"

urlpatterns = [
    path('', Index, name='Index'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)