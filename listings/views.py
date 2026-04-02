from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Listing, Amenity, Booking, Review

def home(request):
    return render(request, "listings/home.html")

@login_required
def listing_list(request):
    listings = Listing.objects.all()
    return render(request, "listings/listing_list.html", {"listings": listings})

@login_required
def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    return render(request, "listings/listing_detail.html", {"listing": listing})

@login_required
def amenity_list(request):
    amenities = Amenity.objects.all()
    return render(request, "listings/amenity_list.html", {"amenities": amenities})

@login_required
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, "listings/booking_list.html", {"bookings": bookings})

@login_required
def review_list(request):
    reviews = Review.objects.all()
    return render(request, "listings/review_list.html", {"reviews": reviews})

def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    return render(request, "listings/listing_detail.html", {"listing": listing})


def amenity_list(request):
    amenities = Amenity.objects.all()
    return render(request, "listings/amenity_list.html", {"amenities": amenities})


def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, "listings/booking_list.html", {"bookings": bookings})


def review_list(request):
    reviews = Review.objects.all()
    return render(request, "listings/review_list.html", {"reviews": reviews})
                                                        