from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')
router.register('demo',views.DemoViewSet,base_name='demo')

urlpatterns = [
    path('hello-views/',views.HelloApiView.as_view()),
    path('', include(router.urls)),
    path('population/',views.PopulationData.as_view()),
    path('jobs/',views.Job.as_view()),
]
