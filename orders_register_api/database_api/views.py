from django.http import JsonResponse
from .models import Order

def create_order(request):
    pass

def update_order(request, pk):
    pass

def search_orders(request):
    orders = Order.objects.none()

    if any(request.GET.values()):
        orders = Order.objects.all()

        if customer_name := request.GET.get('customer_name'):
            orders = orders.filter(customer_name__icontains=customer_name)
        if status := request.GET.get('status'):
            orders = orders.filter(status=status)
        if id := request.GET.get('id'):
            orders = orders.filter(id=id)
        if date := request.GET.get('date'):
            orders = orders.filter(date=date)
        
    return JsonResponse({'orders': list(orders.values())})

def download_order_pdf(request, pk):
    pass
