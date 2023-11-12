from django.contrib import admin

# Register your models here.
from .models import grape,type_wine, wine_sort, bochka
class grapeAdmin(admin.ModelAdmin):
  list_display = ('title', 'date', 'place')
  list_display_links = ('title',)
  search_fields = ('title','date', 'place')
  list_filter = ('date', 'place')

class wine_sortAdmin(admin.ModelAdmin):
  list_display = ('title', 'color', 'b_year','s_grape','type1')
  list_display_links = ('title',)
  search_fields = ('title','color', 'b_year','s_grape','type1')
  list_filter = ('color', 'type1')
  
class bochkaAdmin(admin.ModelAdmin):
  list_display = ('mesto', 'data_zapolnenya', 'obyem','pusto','sort_vina')
  list_display_links = ('mesto',)
  search_fields = ('mesto', 'data_zapolnenya', 'obyem','pusto','sort_vina')
  list_filter = ('pusto', 'sort_vina')
    
   
admin.site.register(grape,grapeAdmin)
admin.site.register(wine_sort,wine_sortAdmin)
admin.site.register(bochka,bochkaAdmin)
admin.site.register(type_wine)