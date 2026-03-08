from django.contrib import admin
from .models import User, Listing, Amenity, ListingAmenity, Image, Booking, Review

admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Amenity)
admin.site.register(ListingAmenity)
admin.site.register(Image)
admin.site.register(Booking)
admin.site.register(Review)