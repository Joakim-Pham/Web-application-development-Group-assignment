from django.shortcuts import render, get_object_or_404, redirect

import listings
from django.contrib.auth.decorators import login_required
from .models import Listing, Amenity, Booking, Review
from .forms import ListingForm, BookingForm
 
 
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
def listing_create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listing_list")
    else:
        form = ListingForm()
    return render(request, "listings/listing_form.html", {"form": form})
 
 
@login_required
def listing_update(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect("listing_list")
    else:
        form = ListingForm(instance=listing)
    return render(request, "listings/listing_form.html", {"form": form})
 
 
@login_required
def listing_delete(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    if request.method == "POST":
        listing.delete()
        return redirect("listing_list")
    return render(request, "listings/listing_confirm_delete.html", {"listing": listing})
 
 
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
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("booking_list")
    else:
        form = BookingForm()
    return render(request, "listings/booking_form.html", {"form": form})

def listing_map(request):

    listings = Listing.objects.all()

    return render(request, "listings/listing_map.html", {"listings": listings})
