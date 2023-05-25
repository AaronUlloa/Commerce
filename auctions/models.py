from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Bid(models.Model):
    bid = models.FloatField(default=0.00)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="userBid")

    def __str__(self):
        return f"{self.bid}"


class Category(models.Model):
    categoryName = models.CharField(max_length=60)
    categoryStatus = models.BooleanField(default=True)

    def __str__(self):
        return f"Name:{self.categoryName}, Status:{self.categoryStatus}"


class Listing(models.Model):
    title = models.CharField(max_length=80)
    image1 = models.CharField(max_length=500)
    image2 = models.CharField(max_length=500)
    image3 = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    price = models.ForeignKey(
        Bid, on_delete=models.CASCADE, blank=True, null=True, related_name="bidPrice")
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="userOwner")
    isActive = models.BooleanField(default=True)
    watchList = models.ManyToManyField(
        User, blank=True, null=True, related_name="userWatchList")

    def __str__(self):
        return f"{self.title}"
