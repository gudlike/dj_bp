from django.conf.urls import url
from django.views.generic import TemplateView

from .views import IndexView, Horizontal_bar_View

urlpatterns = [
    url(r'^visualmain', IndexView.as_view(), name='index'),
]