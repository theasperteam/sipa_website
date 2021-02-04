from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = "events"

urlpatterns = [
    path('', Index, name='Index'),
    path('about/', About, name='About'),
    path('contact/', Contact, name='Contact'),
    path('corporate/', Corporate, name='Corporate'),
    path('gallery/', Gallery, name='Gallery'),
    path('government/', Government, name="Government"),
    path('wedding/', Wedding, name="Wedding"),
    path('sports/', Sports, name="Sports"),
    path('cultural/', Cultural, name="Cultural"),
    path('team/', Team, name="Team"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)