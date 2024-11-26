from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('save-person/<int:pk>/', views.save_person, name='edit_person'),
    path('save-person/', views.save_person, name='add_person'),
    path('delete-person/<int:pk>/', views.delete_person, name='delete_person'),
    path('filter-persons/', views.filter_persons, name='filter_persons'),
]
