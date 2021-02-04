from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = "school"

urlpatterns = [
    path('', Index, name='Index'),
    path('about/', About, name='About'),
    path('acting/', Acting, name='Acting'),
    path('acting_course/', Acting_Course, name='Acting_Course'),
    path('application_form/', Application_Form, name='Application_Form'),
    path('arts/', Arts, name='Arts'),
    path('contact/', Contact, name='Contact'),
    path('dance/', Dance, name='Dance'),
    path('dance_course/', Dance_Course, name='Dance_Course'),
    path('finearts/', Finearts, name='Finearts'),
    path('login/', Login, name='Login'),
    path('login-index/', Login_Index, name='Login_Index'),
    path('music/', Music, name='Music'),
    path('music_course/', Music_Course, name='Music_Course'),
    path('signup/', Singup, name='Singup'),
    path('team/', Team, name='Team'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)