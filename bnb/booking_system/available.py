import datetime
from bnb.models import House, Booking


# logic for making a booking and not dubblebook a house


def available(house, check_in, check_out):
    available_list = []
    bookings_list = Booking.objects.filter(house=house)
    for booking in bookings_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            available_list.append(True)
        else:
            available_list.append(False)
    return all(available_list)
