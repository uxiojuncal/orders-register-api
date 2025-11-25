from django.db import models

class Order(models.Model):
    date = models.DateTimeField()
    customer_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    receiver_name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    address = models.TextField()
    comments = models.TextField(blank=True, null=True)

    class State(models.TextChoices):
        PENDING = 'pendiente', 'Pendiente'
        PROCESSING = 'procesando', 'Procesando'
        DELIVERED = 'entregado', 'Entregado'

    state = models.CharField(max_length=20, choices=State.choices, default=State.PENDING)
