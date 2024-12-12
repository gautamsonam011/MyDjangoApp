from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main_views, name='main'),
    path('members/', views.members, name='members'),
    path('index/', views.index_views, name="index"),
    path('main/member/', views.member_views, name='member'),
    path('main/member/date/<int:id>', views.date_details, name='date'),
    path('master/', views.master_views, name='master'),
    path('404/', views.not_found, name='404'),
    path('test/', views.testing_views, name='test'),
]