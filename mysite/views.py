from django.http import HttpResponse
from django.shortcuts import render
from price_update.models import MacPrice
from price_update.models import KingPrice
from price_update.models import PrawnsPrice
from django.shortcuts import render
from django.http import HttpResponse
from online_orders.models import Order
from django.shortcuts import render, redirect
from online_orders.models import Order
from .forms import OrderForm
from django.shortcuts import render, redirect
from .forms import OrderForm



def landing_page(request):
    return render(request,'index.html')

def home_page(request):
    mac_price_data = MacPrice.objects.all()
    king_price_data = KingPrice.objects.all()
    prawns_price_data = PrawnsPrice.objects.all()
    data = {
        'mac_price_data' : mac_price_data,
        'king_price_data':king_price_data,
        'prawns_price_data':prawns_price_data
    }
    return render(request,'home.html',data)

# Simulated price data for demonstration
fish_prices = {
    'Mackerel': 250,  # ₹ per kg
    'King Fish': 500,
    'Prawns': 300,
}

def place_order(request):
    if request.method == 'POST':
        name = request.POST['name']
        place = request.POST['place']
        contact = request.POST['contact']
        fish = request.POST['fish']
        quantity = float(request.POST['quantity'])

        # Get the price for the selected fish
        fish_price = fish_prices.get(fish, 0)

        # Calculate total price
        total_price = fish_price * quantity

        # Save order to the database
        order = Order(
            name=name,
            place=place,
            contact=contact,
            fish=fish,
            quantity=quantity,
            total_price=total_price,
        )
        order.save()

        # Simulate returning a bill as a response
        return HttpResponse(f"Order placed! Total price: ₹{total_price:.2f}")
    else:
        return render(request, 'home.html')
    
def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('order_success')  # Redirect to success page
    else:
        form = OrderForm()  # Empty form for GET request

    return render(request, 'order_form.html', {'form': form})

def order_success(request):
    return render(request, 'order_success.html')  # Show success message
 