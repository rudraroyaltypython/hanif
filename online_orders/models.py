from django.db import models

class Order(models.Model):
    FISH_CHOICES = [
        ('Mackerel', 'Mackerel'),
        ('King Fish', 'King Fish'),
        ('Prawns', 'Prawns'),
    ]

    name = models.CharField(max_length=255)  # Customer's name
    place = models.CharField(max_length=255)  # Place/Location
    contact = models.CharField(max_length=15)  # Contact Number
    fish = models.CharField(max_length=50, choices=FISH_CHOICES)  # Fish type
    quantity = models.DecimalField(max_digits=5, decimal_places=2)  # Quantity in kg (e.g., 1.50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Calculated price
    order_date = models.DateTimeField(auto_now_add=True)  # Auto-added timestamp

    def __str__(self):
        return f"{self.name} - {self.fish} ({self.quantity} kg)"


class OrderPDF(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='pdf')
    pdf_file = models.FileField(upload_to='pdfs/')
    generated_at = models.DateTimeField(auto_now_add=True)


