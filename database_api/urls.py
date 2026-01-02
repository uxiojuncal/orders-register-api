from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health-check'),              # GET => health check
    path('orders/', views.create_order, name='order-create'),                     # POST => create
    path('orders/<int:pk>/', views.update_order, name='order-update'),
    path('orders/search/', views.search_orders, name='order-search'),          # GET => search with query params
    path('orders/<int:pk>/pdf/', views.generate_order_pdf, name='order-pdf'),  # GET => download PDF
    path('orders/<int:pk>/signature/', views.upload_signature, name='order-signature'),  # PATCH => upload signature
    path('orders/<int:pk>/delete/', views.delete_order, name='order-delete'),   # DELETE => delete order
    path('orders/excel/', views.export_orders_excel, name='order-excel'),  # GET => export to Excel
]