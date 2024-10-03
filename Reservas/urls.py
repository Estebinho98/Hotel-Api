from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    UserView,
    RoomsView,
    SingleRoomView,
    ServicesView,
    SingleServiceView,
    BookingView,
    Booking_MarriageView,
    Booking_FamilyView
)


router = DefaultRouter()
router.register(r'users', UserView)
router.register(r'bookings', BookingView)
router.register(r'booking-marriage', Booking_MarriageView)
router.register(r'booking-family',Booking_FamilyView)

urlpatterns = [
    path('', include(router.urls)),
    path('rooms/', RoomsView.as_view(), name='prices-list' ),
    path('rooms/<int:pk>/', SingleRoomView.as_view(), name='prices-list' ),
    path('services/', ServicesView.as_view(), name='prices-list' ),
    path('services/<int:pk>/', SingleServiceView.as_view(), name='prices-list' ),
    path('reservas-token-auth/', obtain_auth_token),

]

