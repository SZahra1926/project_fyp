from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_files, name='upload_files'),
    path('generate-text/', views.generate_text_view, name='generate_text'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('create/', views.create_task, name='create'), 
]
