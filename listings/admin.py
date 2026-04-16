from django.contrib import admin
from .models import User, Listing, Amenity, ListingAmenity, ListingImage, Booking, Review


class ListingImageInline(admin.TabularInline):
    model = ListingImage
    extra = 1


class ListingAmenityInline(admin.TabularInline):
    model = ListingAmenity
    extra = 1


class ListingAdmin(admin.ModelAdmin):
    inlines = [ListingImageInline, ListingAmenityInline]


admin.site.register(User)
admin.site.register(Amenity)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Listing, ListingAdmin)