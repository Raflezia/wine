from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from wino import views

urlpatterns = [
    path('wino/', include('wino.urls')), #url отслеживание адресов
    path('admin/', admin.site.urls),
    path("htmlk/", views.index),
    #path('',include('wino.urls'))#main страница отслеживание. передача прав приложению погребок
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
