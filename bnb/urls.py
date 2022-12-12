from django.urls import path
from .views import HouseList, BookingList, BookingViwe

app_name = 'bnb'

urlpatterns = [
    path('house_list/', HouseList.as_view(), name='HouseList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingViwe.as_view(), name='BookingViwe')
]
