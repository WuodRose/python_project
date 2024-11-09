from django.urls import path ,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [


    path('', views.dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),


    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('password_reset/', views.password_reset, name='password_reset'),


    path('', views.dashboard, name='dashboard'),
    path('animals/', views.animal_list, name='animal_list'),
    path('animals/add/', views.animal_add, name='animal_add'),
    path('animals/<int:pk>/edit/', views.animal_edit, name='animal_edit'),
    path('animals/<int:pk>/delete/', views.animal_delete, name='animal_delete'),


    path('animals/<int:pk>/', views.animal_detail, name='animal_detail'),
    path('health/', views.health_list, name='health_list'),
    path('health/add/', views.health_add, name='health_add'),
    path('health/<int:pk>/edit/', views.health_edit, name='health_edit'),
    path('health/<int:pk>/delete/', views.health_delete, name='health_delete'),
    path('breeding/', views.breeding_list, name='breeding_list'),
    path('breeding/add/', views.breeding_add, name='breeding_add'),
    path('breeding/<int:pk>/edit/', views.breeding_edit, name='breeding_edit'),
    path('breeding/<int:pk>/delete/', views.breeding_delete, name='breeding_delete'),
]