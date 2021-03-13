from django.shortcuts import render,redirect
from bazzar.models import Order

def order_list_view(request):
    order = Order.objects.all()
    return render(request, 'adminapp/order_list.html',{'order':order})

def order_approve_view(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        order = Order.objects.get(id=pk)
        order.status = "approve"
        order.save()
        return redirect('/adminapp/order-list/')

def order_processing_view(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        order = Order.objects.get(id=pk)
        order.status = "processing"
        order.save()
        return redirect('/adminapp/order-list/')

def order_billing_view(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        order = Order.objects.get(id=pk)
        order.status = "billing"
        order.save()
        return redirect('/adminapp/order-list/')

def order_shipping_view(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        order = Order.objects.get(id=pk)
        order.status = "shipping"
        order.save()
        return redirect('/adminapp/order-list/')

def order_dispatched_view(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        order = Order.objects.get(id=pk)
        order.status = "dispatched"
        order.save()
        return redirect('/adminapp/order-list/')

def order_delivered_view(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        order = Order.objects.get(id=pk)
        order.status = "delivered"
        order.save()
        return redirect('/adminapp/order-list/')

def order_cancelled_view(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        order = Order.objects.get(id=pk)
        order.status = "cancelled"
        order.save()
        return redirect('/adminapp/order-list/')
