from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth import get_user_model
import uuid

USER = get_user_model()


class Card(models.Model):

    TYPE = (
        ("Amazon", "Amazon"),
        ("iTunes", "iTunes"),
        ("Starbucks", "Starbucks"),
        ("Visa", "Visa"),
        ("Walmart", "Walmart"),
    )

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TYPE)
    currency = MoneyField(max_digits=14, decimal_places=2, default_currency="NGN")
    image = models.ImageField(upload_to="card_image/")

    def __str__(self):
        return self.name


class Coin(models.Model):

    TYPE = (("Bitcoin", "Bitcoin"), ("Ethereum", "Ethereum"))

    type = models.CharField(max_length=50, choices=TYPE)
    image = models.ImageField(upload_to="coin_image/")
    code = models.CharField(max_length=300)

    def __str__(self):
        self.type


STATUS = (
    ("paid", "paid"),
    ("pending", "pending"),
    ("processing", "processing"),
    ("cancelled", "cancelled"),
    ("successful", "successful"),
)


class Payment(models.Model):

    STATUS = (
        ("paid", "paid"),
        ("pending", "pending"),
        ("processing", "processing"),
        ("cancelled", "cancelled"),
        ("successful", "successful"),
    )

    _id = models.UUIDField(default=uuid.uuid4())
    seller = models.ForeignKey(USER, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    date = models.DateField()
    status = models.CharField(choices=STATUS, max_length=15)

    def __str__(self):
        self._id


class Transaction(models.Model):

    payment_id = models.OneToOneField(Payment, on_delete=models.DO_NOTHING)
    seller = models.ForeignKey(USER, on_delete=models.DO_NOTHING)
    status = models.CharField(choices=STATUS, max_length=15)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    date = models.DateField()


