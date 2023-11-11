from django.contrib import admin

# Register your models here.
from .models import grape,wine_sort,bochka
admin.site.register(grape)
admin.site.register(wine_sort)
admin.site.register(bochka)