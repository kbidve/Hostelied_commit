from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.UserList.as_view(), name='UserAdministrator-create'),
    url(r'^(?P<pk>[0-9]+)/$', views.UserDetais.as_view(), name='UserAdministrator-list'),
    url(r'^(?P<user_id>[0-9]+)/postedads/$', views.UsersAdsList.as_view(), name='UserAdministrator-postedads'),
]