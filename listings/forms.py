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
            'title',
            'description',
            'price_per_night',
            'city',
            'country',
            'address',
            'property_type',
            'square_meters',
            'max_guests',
            'bedrooms',
            'bathrooms',
            'number_of_beds',
            'latitude',
            'longitude',
            'amenities',
]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['listing', 'check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get("check_in")
        check_out = cleaned_data.get("check_out")
        if check_in and check_out:
            if check_out <= check_in:
                raise forms.ValidationError("Check-out date must be after check-in date.")
        return cleaned_data
