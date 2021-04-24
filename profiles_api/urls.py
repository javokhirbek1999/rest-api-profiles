from django.urls import path
from . import views

urlpatterns = [
    path('hello-views/',views.HelloApiView.as_view()),
    path('population/',views.PopulationData.as_view()),
]
