from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('save-person/<int:pk>/', views.save_person, name='edit_person'),
    path('save-person/', views.save_person, name='add_person'),
    path('delete-person/<int:pk>/', views.delete_person, name='delete_person'),
    path('filter-persons/', views.filter_persons, name='filter_persons'),
]
