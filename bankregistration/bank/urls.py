from django.urls import path
from .import views
app_name='bank'

urlpatterns = [
    path('', views.home, name='home'),
    path('button/', views.button, name='button'),
    path('form/', views.form, name='form'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('submit/',views.Submit,name='submit'),
    path('ajax/load_branch/', views.branches, name='branches'),
]