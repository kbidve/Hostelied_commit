from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^mess/$', views.MessList.as_view(), name='Mess_List'),
    url(r'^mess/(?P<pk>[0-9]+)/$', views.MessDetails.as_view(), name='Mess_Info'),
]