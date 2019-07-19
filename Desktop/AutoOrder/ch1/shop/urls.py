from django.urls import re_path
from . import views


urlpatterns = [
    re_path('^$', views.shop_list, name='shop_list'),
    re_path('^(?P<shop>\[w|W]+)/$', views.menu_list, name='menu_list'),
    re_path('^(?P<shop>\[w|W])/(?P<pk>\d+)/$', views.menu_detail),
]
