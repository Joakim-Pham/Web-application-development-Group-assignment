from django import forms
from .models import User, Booking, Listing


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length= 8,
        help_text="Password must be at least 8 characters long.",
    )
    password_confirm = forms.CharField( 
        widget=forms.PasswordInput,
        label="Confirm Password",
    )

    email = forms.EmailField(required=True, help_text="Enter a valid email address.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'phone']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email address is already in use.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken.")
        return username
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price_per_night', 'status', 'city', 'country', 'address', 'latitude', 'longitude', 'amenities']


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
                raise forms.ValidationError("Check-out date must be after check-in date.")
        return cleaned_data