from django.urls import path
#from .views import index
from . import views
urlpatterns=[
    # path('',index),
    path('',views.index,name='home'),#круглые скобки не нужны. нужно лишь обратиться без его выполенния поэтому без ()
    path('sortofwine/',views.sortW,name='sortofwine'),
    path('barrels/',views.barrelwine,name='barrelofwine'),
]