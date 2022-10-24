
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('travelapp.urls')),
    path('credentials/',include('credentials.urls')),

    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)