from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from wino import views

urlpatterns = [
    path('', include('wino.urls')), 
    path('admin/', admin.site.urls),
    # path("htmlk/", views.index),
    #path('',include('wino.urls'))
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
