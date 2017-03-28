from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.UserList.as_view(), name='UserAdministrator-create'),
    url(r'^(?P<pk>[0-9]+)/$', views.UserDetais.as_view(), name='UserAdministrator-create'),
]