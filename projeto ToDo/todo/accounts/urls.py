from django.urls import path

from . import views

# adicionando as urls do app
urlpatterns = [
    path('register/', views.SignUp.as_view(), name="signup"),
]
