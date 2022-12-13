from django.urls import path
from .views import HouseListView, BookingList, BookingViwe, HouseDetailViwe

app_name = 'bnb'

urlpatterns = [
    path('house_list/', HouseListView.as_view(), name='HouseListView'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingViwe.as_view(), name='BookingViwe'),
    path('house/<category>', HouseDetailViwe.as_view(), name='HouseDetailViwe')
]
