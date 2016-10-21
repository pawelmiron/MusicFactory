from django.conf.urls import url
from . import views

app_name ='music'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetalView.as_view(), name='detail'),

    # /music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),


]
