from django import forms
<<<<<<< Updated upstream
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
=======
from django import forms
from .models import User, Booking


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'phone']
>>>>>>> Stashed changes


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
<<<<<<< Updated upstream
        fields = ['guest', 'listing', 'check_in', 'check_out', 'total_price']
=======
        fields = ['listing', 'check_in', 'check_out']

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get("check_in")
        check_out = cleaned_data.get("check_out")

        if check_in and check_out:
            if check_out <= check_in:
                raise forms.ValidationError(
                    "Check-out date must be after check-in date."
                )

        return cleaned_data

>>>>>>> Stashed changes
