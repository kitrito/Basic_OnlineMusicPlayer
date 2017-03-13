from django.conf.urls import url
from . import views
app_name = 'muzisystem'


urlpatterns = [
    # for /index/
    url(r'^uploadtracks/$', views.upload_track, name='utracks'),
    url(r'^uploadalbums/$', views.upload_album, name='ualbums'),
    url(r'^home/$', views.home, name='home'),
    url(r'^uploadgenre/$', views.upload_genre, name='ugenre'),
    url(r'^uploadartist/$', views.upload_artist, name='uartist'),
 ]
