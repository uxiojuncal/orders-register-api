from django.http import JsonResponse
from .models import Order
import json
from django.shortcuts import get_object_or_404

def create_order(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    try:
        payload = json.loads(request.body.decode() or '{}')
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    required_fields = ['date', 'customer_name', 'customer_phone', 'receiver_name', 'product_name', 'address']
    for field in required_fields:
        if field not in payload:
            return JsonResponse({'error': f'Missing required field: {field}'}, status=400)
        
    order = Order.objects.create(
        date=payload['date'],
        customer_name=payload['customer_name'],
        customer_phone=payload['customer_phone'],
        receiver_name=payload['receiver_name'],
        receiver_phone=payload['receiver_phone'],
        product_name=payload['product_name'],
        address=payload['address'],
        comments=payload.get('comments', ''),
        status=payload.get('status', Order.Status.PENDING)
    )

    return JsonResponse({'order_id': order.pk}, status=201)

def update_order(request, pk):
    if request.method not in ('PATCH', 'PUT'):
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        payload = json.loads(request.body.decode() or '{}')
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    order = get_object_or_404(Order, pk=pk)

    allowed_fields = {
        'date', 'customer_name', 'phone_number', 'receiver_name',
        'product_name', 'address', 'comments', 'status'
    }

    for field, value in payload.items():
        if field in allowed_fields:
            setattr(order, field, value)

    order.save()

    data = {
        'id': order.pk,
        'date': order.date.isoformat() if order.date else None,
        'customer_name': order.customer_name,
        'phone_number': order.phone_number,
        'receiver_name': order.receiver_name,
        'product_name': order.product_name,
        'address': order.address,
        'comments': order.comments,
        'status': order.status,
    }
    return JsonResponse({'order': data})

def search_orders(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

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
            try:
                day, month = date.split('-')
                day = int(day)
                month = int(month)
                orders = orders.filter(date__day=day, date__month=month)
            except ValueError:
                return JsonResponse({'error': 'Formato de fecha inválido. Use DD-MM.'}, status=400)
        
    return JsonResponse({'orders': list(orders.values())})

def download_order_pdf(request, pk):
    pass
