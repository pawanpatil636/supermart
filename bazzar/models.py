from django.db import models
from django.contrib.auth.models import User


CATEGORY_CHOICES=(  
('grocery','grocery'),
('food','food'),
)

STATUS_CHOICES=(  
('ordered','ordered'),
('approve','approve'),
('processing','processing'),
('billing','billing'),
('shipping','shipping'),
('dispatched','dispatched'),
('delivered','delivered'),
('cancelled','cancelled'),
)
class Product(models.Model):
    product_name =models.CharField(max_length=30)
    category =models.CharField(max_length=10,choices=CATEGORY_CHOICES)
    availability =models.BooleanField(default=True)
    price =models.IntegerField()
    description =models.CharField(max_length=30)
    image = models.ImageField(upload_to="product_images", null=True)


    def __str__(self):
        return str(self.product_name)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    flat_number=models.IntegerField()
    appartment_name=models.CharField(max_length=50)
    street_name=models.CharField(max_length=50)
    pincode=models.IntegerField()
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    mobile=models.IntegerField(default='8317404976')

    def __str__(self):
        return self.appartment_name


class Order(models.Model):
    order_id=models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.ForeignKey(Address, on_delete=models.CASCADE , null=True)
    product_name =models.CharField(max_length=30)
    category =models.CharField(max_length=10,choices=CATEGORY_CHOICES)
    price =models.IntegerField()
    description =models.CharField(max_length=30)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ordered")
    
    def __str__(self):
        return str(self.user)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True)
    card_holder=models.CharField(max_length=50)
    card_number=models.IntegerField()
    cvv =models.IntegerField()

    def __str__(self):
        return str(self.user)

    


