from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePage.as_view(), name='home')
]

if settings.DEBUG:  # Только для режима разработки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)