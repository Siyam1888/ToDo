from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='task_list'),
    path('update/<int:pk>/', views.update, name='update_task'),
    path('delete/<int:pk>/', views.delete, name='delete_task'),

]