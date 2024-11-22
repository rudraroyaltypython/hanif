# forms.py
from django import forms
from online_orders.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'place', 'contact', 'fish', 'quantity']  # Include the fields you want in the form
