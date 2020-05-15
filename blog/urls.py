from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^detail/(?P<blog_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create/', views.create, name='create'),
    url(r'^postcreate/', views.postcreate, name='postcreate'),
    url(r'^update/(?P<blog_id>[0-9]+)/$', views.update, name='update'),
    url(r'^delete/(?P<blog_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^papago/', views.papago, name='papago'),
]
