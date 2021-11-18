from django.urls import path
from . import views

urlpatterns = [
    path('api/rooms/', views.RoomListCreate.as_view()),
]