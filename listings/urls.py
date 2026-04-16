from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("listings/", views.listing_list, name="listing_list"),
    path("listings/<int:listing_id>/", views.listing_detail, name="listing_detail"),
    path("listings/create/", views.listing_create, name="listing_create"),
    path("listings/<int:listing_id>/edit/", views.listing_update, name="listing_update"),
    path("listings/<int:listing_id>/delete/", views.listing_delete, name="listing_delete"),
    path("amenities/", views.amenity_list, name="amenity_list"),
    path("bookings/", views.booking_list, name="booking_list"),
    path("bookings/create/", views.booking_create, name="booking_create"),
    path("reviews/", views.review_list, name="review_list"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path("map/", views.listing_map, name="listing_map"),
]
