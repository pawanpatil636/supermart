from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Product
from .models import Address
from .models import Order
from .models import Payment



def add_product_view(request):
    if request.user.is_superuser:
        if request.method == "POST":
            productname=request.POST['product_name']
            category=request.POST['category']
            price=request.POST['price']
            description=request.POST['description']
            image = request.FILES['image']

            product=Product(product_name=productname,price=price,category=category,description=description,image=image)
            product.save()
            return redirect('/bazzar/product-list/')
        return render(request,'bazzar/add_product.html')
    else:
        return redirect('/account/login/')

def product_list_view(request):
    product = Product.objects.all()
    return render(request, "bazzar/product_list.html",{'product':product})

def product_details_view(request,pk):
    # product = Product.objects.get(id=pk)
    product = get_object_or_404(Product,id=pk)
    return render(request, "bazzar/product_details.html",{'product':product})

# def place_order_view(request):
#     # product = get_object_or_404(Product,id=pk)
#     product = Product.objects.all()
#     return render(request, "bazzar/place_order.html",{'product':product})

# def product_delete_view(request, pk):
#     product =get_object_or_404(Product ,id=pk).delete()
#     return redirect('/bazzar/product-list/')

def product_update_view(request,pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        productname=request.POST['product_name']
        category=request.POST['category']
        price=request.POST['price']
        description=request.POST['description']
        image = request.FILES['image']

        product.product_name = productname
        product.image = image
        product.category = category
        product.description = description
        product.price = price
        product.save()
        return redirect('/')
    return render(request, 'bazzar/add_product.html',{'product':product})






def coustomer_address_payment(request,pk):
    product = Product.objects.get(id=pk)
    id=product.id
    if request.method == "POST":
        flat_number = request.POST['flat_number']
        appartment_name = request.POST['appartment_name']
        street_name = request.POST['street_name']
        pincode = request.POST['pincode']
        state = request.POST['state']
        country = request.POST['country']

        card_holder= request.POST['card_holder']
        card_number= request.POST['card_number']
        cvv= request.POST['cvv']
        
        address = Address(user=request.user,flat_number=flat_number,appartment_name=appartment_name,street_name=street_name,pincode=pincode,state=state,country=country)
        address.save() 
        payment = Payment(user=request.user,card_holder=card_holder,card_number=card_number,cvv=cvv)
        payment.save()
        
        return redirect(f'/bazzar/checkout-view/{id}')
    return render(request, "bazzar/payment.html", {'product':product})

def checkout_view(request,pk):
    product = Product.objects.get(id=pk)
    address=Address.objects.filter(user=request.user)[0]
    order =Order(order_id=1,user=request.user,address=address,product_name=product.product_name,category=product.category,price=product.price,description=product.description)
    order.save()   
    return render(request, 'bazzar/checkout.html',{'product':product})


def redirect_view(request):
    return redirect("/bazzar/product-list/")



# Create your views here.

