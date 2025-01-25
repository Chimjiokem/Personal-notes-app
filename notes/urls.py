from django.urls import path
from .import views

app_name = 'notes'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_note/', views.add_note, name='add_note'),
    path('note_detail/<int:id>/', views.note_detail, name='note_detail'),
]