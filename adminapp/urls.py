from django.urls import path
from . import views 


app_name = "adminapp"
urlpatterns = [
    path('order-list/',views.order_list_view, name = 'order_list'),
    path('order-approve/<int:pk>/',views.order_approve_view, name = 'order_approve'),
    path('order-processing/<int:pk>/',views.order_processing_view, name = 'order_processing'),
    path('order-billing/<int:pk>/',views.order_billing_view, name = 'order_billing'),
    path('order-shipping/<int:pk>/',views.order_shipping_view, name = 'order_shipping'),
    path('order-dispatched/<int:pk>/',views.order_dispatched_view, name = 'order_dispatched'),
    path('order-delivered/<int:pk>/',views.order_delivered_view, name = 'order_delivered'),
    path('order-cancelled/<int:pk>/',views.order_cancelled_view, name = 'order_cancelled'),
]