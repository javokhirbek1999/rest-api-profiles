from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')
router.register('demo',views.DemoViewSet,base_name='demo')
router.register('profiles',views.UserProfileViewSet)
router.register('countries',views.CountriesData,base_name='countries')
router.register('companies',views.Companies,base_name='companies')
router.register('users',views.UserProfViewSet)

urlpatterns = [
    path('hello-views/',views.HelloApiView.as_view()),
    path('', include(router.urls)),
    path('population/',views.PopulationData.as_view()),
    path('jobs/',views.Job.as_view()),
]
