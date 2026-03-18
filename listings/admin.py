from django.contrib import admin
from .models import User, Listing, Amenity, ListingAmenity, ListingImage, Booking, Review

admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Amenity)
admin.site.register(ListingAmenity)
admin.site.register(ListingImage)
admin.site.register(Booking)
admin.site.register(Review)