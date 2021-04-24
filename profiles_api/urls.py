from django.urls import path
from . import views

urlpatterns = [
    path('hello-views/',views.HelloApiView.as_view()),
    path('movies/',views.MoviesList.as_view()),
]
