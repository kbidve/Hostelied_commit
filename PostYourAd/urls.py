from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cotbasisroom/$', views.CotBasisDetails.as_view(), name='CotBasis-create'),
]