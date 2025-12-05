from django.conf import settings
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static

from cars import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('cars', views.cars_page, name='cars')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)