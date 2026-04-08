from django import forms
from django import forms
from .models import User, Booking


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'phone']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
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

