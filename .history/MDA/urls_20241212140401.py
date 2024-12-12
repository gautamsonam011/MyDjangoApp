from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('index/', views.index_views, name="index"),
    path('member/', views.member_views, name='member'),
    path('date/', views.date_details, name='date')
]