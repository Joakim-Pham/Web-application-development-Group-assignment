from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('guest', 'Guest'),
        ('host', 'Host'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, blank=True)


class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Listing(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField()

    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.BooleanField(default=True)

    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    latitude = models.FloatField()
    longitude = models.FloatField()

    amenities = models.ManyToManyField(Amenity, through='ListingAmenity')

    def __str__(self):
        return self.title


class ListingAmenity(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)


class Image(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    image_url = models.URLField()


class Booking(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    check_in = models.DateField()
    check_out = models.DateField()

    total_price = models.DecimalField(max_digits=10, decimal_places=2)


class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)

    rating = models.IntegerField()
    comment = models.TextField()