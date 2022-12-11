from django.urls import path, include
from .viewsets import AppointmentViewSet, BranchViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'appointments', AppointmentViewSet)
router.register(r'branches', BranchViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('available/<int:unit_id>', views.get_available_intervals),
  path('location/', views.get_user_location),
  path('cities/', views.get_cities),
  path('close-branches/', views.get_close_branches)
]
