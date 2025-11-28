from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.create_order, name='order-create'),                     # POST => create
    path('orders/<int:pk>/', views.update_order, name='order-update'),
    path('orders/search/', views.search_orders, name='order-search'),          # GET => search with query params
    path('orders/<int:pk>/pdf/', views.download_order_pdf, name='order-pdf')  # GET => download PDF
]
