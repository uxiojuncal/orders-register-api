from django.db import models

class Order(models.Model):
    date = models.DateTimeField()
    customer_name = models.CharField(max_length=255)
    customer_phone = models.IntegerField()
    receiver_name = models.CharField(max_length=255)
    receiver_phone = models.IntegerField()
    product_name = models.CharField(max_length=255)
    address = models.TextField()
    comments = models.TextField(blank=True, null=True)

    class Status(models.TextChoices):
        PENDING = 'pendiente', 'Pendiente'
        PROCESSING = 'procesando', 'Procesando'
        DELIVERED = 'entregado', 'Entregado'

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
