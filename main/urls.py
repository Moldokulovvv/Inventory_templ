from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import IndexPageView, CategoryDetail, InventDetailView, add_invent, act_test, reestr_test

urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('category/<str:slug>/', CategoryDetail, name='category'),
    path('invent-detail/<int:pk>/', InventDetailView.as_view(), name='detail'),
    path('invent-add/', add_invent, name='add_invent'),
    path('act-test/', act_test, name='act-test'),
    path('reestr/test/', reestr_test, name='reestr'),


]
