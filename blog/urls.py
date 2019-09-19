from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/(?P<slugInput>[\w-]+)/$', views.slugPost, name='details'),
    # url(r'^khusus/(?P<slugInput>[\w-]+)$',views.khusus, name="khusus"),
    url(r'^category/(?P<categoryInput>[\w-]+)/$', views.categoryPost, name='category'),
    url(r'^$', views.index, name='index'),
]