from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View
from .models import House, Booking
from .booking_form import AvailableForm
from bnb.booking_system.available import available


class HouseListView(ListView):
    model = House


class BookingList(ListView):
    model = Booking


class HouseDetailViwe(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        house_list = House.objects.filter(category=category)

        if len(house_list) > 0:
            house = house_list[0]
            house_category = dict(house.HOUSE_CATEGORIES).get(house.category, None)
            context = {
                'house_category': house_category
            }
            return render(request, 'house_detail_view.html', context)
        else:
            return HttpResponse('Category dose not exist')

    def post(self, request, *args, **kwargs):
        house_list = House.objects.filter(category=category)
        available_house = []
        for house in house_list:
            if available(house, data['check_in'], data['check_out']):
                available_house.append(house)

        if len(available_house) > 0:

            house = available_house[0]
            booking = Booking.objects.create(
                user=self.request.user,
                house=house,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)

        else:
            return HttpResponse('This catagory of house is booked')


# Too check if the house is available


class BookingViwe(FormView):
    form_class = AvailableForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        house_list = House.objects.filter(category=data['house_category'])
        available_house = []
        for house in house_list:
            if available(house, data['check_in'], data['check_out']):
                available_house.append(house)

        if len(available_house) > 0:

            house = available_house[0]
            booking = Booking.objects.create(
                user=self.request.user,
                house=house,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)

        else:
            return HttpResponse('This catagory of house is booked')
