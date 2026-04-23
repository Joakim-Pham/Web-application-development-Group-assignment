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
        fields = ['title', 'description', 'price_per_night', 'city', 'country', 
                  'address', 'latitude', 'longitude', 'amenities', 'property_type', 
                  'max_guests', 'bedrooms', 'bathrooms', 'available_from', 'available_to']


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
        listing = cleaned_data.get("listing")

        if check_in and check_out:
            if check_out <= check_in:
                raise forms.ValidationError("Check-out date must be after check-in date.")

            if listing:
                if listing.available_from and check_in < listing.available_from:
                    raise forms.ValidationError(f"This listing is only available from {listing.available_from}.")
                if listing.available_to and check_out > listing.available_to:
                    raise forms.ValidationError(f"This listing is only available until {listing.available_to}.")

        return cleaned_data