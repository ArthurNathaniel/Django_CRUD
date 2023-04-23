from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert', views.insertData, name='insertData'),
    path('update/<id>', views.insertData, name='insertData'),
    path('delete/<id>', views.insertData, name='insertData'),
]
