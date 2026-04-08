from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Listing, Booking, User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'phone', 'password1', 'password2']

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            'host',
            'title',
            'description',
            'price_per_night',
            'max_guests',
            'square_meters',
            'city',
            'country',
            'address',
            'amenities',
        ]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest', 'listing', 'check_in', 'check_out']