from django.conf.urls import url
from . import views

app_name = 'identify'


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^history', views.history, name='history'),
    url(r'^search', views.fileupload2, name='search'),
    url(r'^index', views.fileupload, name='index'),
]
