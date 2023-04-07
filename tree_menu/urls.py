from django.urls import path
from .views import MenuView

urlpatterns = [
    path('<slug>/', MenuView.as_view()),
]
