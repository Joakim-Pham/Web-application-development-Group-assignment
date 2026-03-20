from django import forms
from .models import Listing, Booking

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            'host',
            'title',
            'description',
            'price_per_night',
            'status',
            'city',
            'country',
            'address',
            'latitude',
            'longitude',
            'amenities',
        ]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest', 'listing', 'check_in', 'check_out', 'total_price']