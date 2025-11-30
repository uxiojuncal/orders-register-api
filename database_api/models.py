from django.db import models

class Order(models.Model):
    date = models.DateField()
    customer_name = models.CharField(max_length=255)
    customer_phone = models.IntegerField(blank=True, null=True)
    receiver_name = models.CharField(max_length=255)
    receiver_phone = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=255)
    address = models.TextField()
    observations = models.TextField(blank=True, null=True)
    signature = models.ImageField(upload_to='signatures/', blank=True, null=True)

    class Status(models.TextChoices):
        PENDING = 'pending'
        PROCESSING = 'processing'
        DELIVERED = 'delivered'
        PROBLEMATIC = 'problematic'

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
