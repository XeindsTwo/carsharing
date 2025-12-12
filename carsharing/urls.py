from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static

from cars import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('cars', views.cars_page, name='cars'),
    path('users/', include('users.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)