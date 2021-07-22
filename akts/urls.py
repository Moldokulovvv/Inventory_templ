from django.urls import path

from akts.views import act_create, ActDetailView, act_create_time, Test, ActListView

urlpatterns = [
    path('', ActListView.as_view(), name='acts'),
    path('create/', act_create, name='act-create'),
    path('create/time/', act_create_time, name='act-create-time'),
    path('detail/<int:pk>/', ActDetailView.as_view(), name='act-detail'),
    path('test-pdf/<int:pk>/', Test.as_view(), name='test')


]