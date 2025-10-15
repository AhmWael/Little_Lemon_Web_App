from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),         # Home & menu URLs
    path('restaurant/booking/', include(router.urls)),  # Booking API
    path('auth/', include('djoser.urls')),       # User registration & management
    path('auth/', include('djoser.urls.authtoken')),  # Token auth endpoints
]
