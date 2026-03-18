from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("listings/", views.listing_list, name="listing_list"),
    path("listings/<int:listing_id>/", views.listing_detail, name="listing_detail"),
    path("amenities/", views.amenity_list, name="amenity_list"),
    path("bookings/", views.booking_list, name="booking_list"),
    path("reviews/", views.review_list, name="review_list"),
]

