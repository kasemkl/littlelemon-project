from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingsViewSet, basename='booking') 


urlpatterns = [
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuView.as_view()),
    path('bookings/', include(router.urls)),
    path('users/', views.UserViewSet.as_view({'get;list'})),
]