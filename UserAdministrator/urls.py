from django.conf.urls import url
from . import views
from PostYourAd.views import CotBasisDetais , FlatOnRentDetais

urlpatterns = [
    url(r'^$', views.UserList.as_view(), name='UserAdministrator-create'),
    url(r'^(?P<pk>[0-9]+)/$', views.UserDetais.as_view(), name='UserAdministrator-list'),
    url(r'^(?P<user_id>[0-9]+)/postedads/$', views.UsersAdsList.as_view(), name='UserAdministrator-postedads'),
    url(r'^(?P<user_id>[0-9]+)/postedads/rooms$', views.UsersRoomAdsList.as_view(), name='UserAdministrator-postedroomsads'),
    url(r'^(?P<user_id>[0-9]+)/postedads/flats$', views.UsersFlatAdsList.as_view(), name='UserAdministrator-postedflatsads'),
    url(r'^(?P<user_id>[0-9]+)/postedads/rooms/(?P<pk>[0-9]+)$', CotBasisDetais.as_view(), name='UserAdministrator-postedroomad'),
    url(r'^(?P<user_id>[0-9]+)/postedads/flats/(?P<pk>[0-9]+)$', FlatOnRentDetais.as_view(), name='UserAdministrator-postedflatad'),
]