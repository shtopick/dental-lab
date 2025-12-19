from django.urls import path
from . import views

#app_name = 'chat'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('doctors/', views.DoctorListView.as_view(), name='doctor_list'),
]