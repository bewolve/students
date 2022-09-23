from django.urls import path
from . import views


urlpatterns = [

    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),


    path('', views.home, name='home'),

    path('routes/', views.bus_home, name='routes-home'),
    path('routes/create_routes', views.create_bus, name='route-create'),
    path('routes/update_routes/<str:pk>', views.update_bus, name='update-bus'),
    path('routes/delete_routes/<str:pk>', views.delete_bus, name='delete-bus'),
    

    path('create-student', views.create_student, name='create-student'),
    path('update-student/<str:pk>', views.update_student, name='update-student'),
    path('delete-student/<str:pk>', views.delete_student, name='delete-student'),


]
