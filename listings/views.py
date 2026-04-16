from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing, Amenity, Booking, Review, User
from .forms import ListingForm, BookingForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Listing, Amenity, Booking, Review, ListingImage
from .forms import ListingForm, BookingForm
from decimal import Decimal

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'listings/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'listings/login.html', {'error': 'Invalid credentials'})
    return render(request, 'listings/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    guest_bookings = Booking.objects.filter(guest=user)
    hosted_listings = Listing.objects.filter(host=user)
    host_bookings = Booking.objects.filter(listing__host=user)
    return render(request, "listings/profile.html", {
        "user": user,
        "guest_bookings": guest_bookings,
        "hosted_listings": hosted_listings,
        "host_bookings": host_bookings,
    })

@login_required
def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("booking_list")
    else:
        form = BookingForm()
    return render(request, "listings/booking_form.html", {"form": form})

def home(request):
    listings = Listing.objects.order_by('-created_at')[:6]
    return render(request, "listings/home.html", {"listings": listings})

@login_required
def listing_list(request):
    listings = Listing.objects.order_by('-created_at')[:6]

    location = request.GET.get('location')
    check_in = request.GET.get('check_in')
    check_out = request.GET.get('check_out')
    guests = request.GET.get('guests')

    if location:
        listings = listings.filter(city__icontains=location) | listings.filter(country__icontains=location)
    if guests:
        listings = listings.filter(max_guests__gte=guests)

    return render(request, "listings/listing_list.html", {"listings": listings})

def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    amenities = listing.amenities.all()
    reviews = Review.objects.filter(booking__listing=listing)
    booked_dates = Booking.objects.filter(listing=listing).values_list('check_in', 'check_out')
    
    booking_form = BookingForm()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.guest = request.user
            booking.listing = listing
            nights = (booking.check_out - booking.check_in).days
            booking.total_price = nights * listing.price_per_night
            booking.save()
            return redirect('profile', user_id=request.user.id)
        
    return render(request, "listings/listing_detail.html", {
        "listing": listing,
        "amenities": amenities,
        "reviews": reviews,
        "booked_dates": booked_dates,
        "booking_form": booking_form,
    })

def listing_create(request):
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save()

            image_file = form.cleaned_data.get("image")
            if image_file:
                ListingImage.objects.create(listing=listing, image=image_file)

            return redirect("listing_list")
    else:
        form = ListingForm()

    return render(request, "listings/listing_form.html", {"form": form})

@login_required
def listing_update(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            listing = form.save()

            image_file = form.cleaned_data.get("image")
            if image_file:
                ListingImage.objects.create(listing=listing, image=image_file)

            return redirect("listing_list")
    else:
        form = ListingForm(instance=listing)

    return render(request, "listings/listing_form.html", {"form": form})

def listing_delete(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    if request.method == "POST":
        listing.delete()
        return redirect("listing_list")
    return render(request, "listings/listing_confirm_delete.html", {"listing": listing})

def amenity_list(request):
    amenities = Amenity.objects.all()
    return render(request, "listings/amenity_list.html", {"amenities": amenities})

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, "listings/booking_list.html", {"bookings": bookings})

@login_required
def amenity_list(request):
    amenities = Amenity.objects.all()
    return render(request, "listings/amenity_list.html", {"amenities": amenities})


@login_required
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, "listings/booking_list.html", {"bookings": bookings})


@login_required
def booking_create(request):
    listing_id = request.GET.get("listing")

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.guest = request.user

            days = (booking.check_out - booking.check_in).days
            if days < 1:
                days = 1

            booking.total_price = booking.listing.price_per_night * Decimal(days)
            booking.save()

            return redirect("booking_list")
    else:
        initial_data = {}
        if listing_id:
            initial_data["listing"] = listing_id
        form = BookingForm(initial=initial_data)

    return render(request, "listings/booking_form.html", {"form": form})


@login_required
def review_list(request):
    reviews = Review.objects.all()
    return render(request, "listings/review_list.html", {"reviews": reviews})


def listing_map(request):
    listings = Listing.objects.all()
    return render(request, "listings/listing_map.html", {"listings": listings})
