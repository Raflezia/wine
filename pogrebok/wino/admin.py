from django.contrib import admin

# Register your models here.
from .models import grape,type_wine, wine_sort, bochka
class grapeAdmin(admin.ModelAdmin):
  list_display = ('title', 'date', 'place')
  list_display_links = ('title',)
  search_fields = ('title','date', 'place')
  list_filter = ('date', 'place')


admin.site.register(grape,grapeAdmin)
admin.site.register(wine_sort)
admin.site.register(bochka)
admin.site.register(type_wine)