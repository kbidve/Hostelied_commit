from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cotbasisroom/$', views.CotBasisList.as_view(), name='CotBasis-create'),
    url(r'^cotbasisroom/(?P<pk>[0-9]+)/$', views.CotBasisDetais.as_view(), name='CotBasis-create'),
]