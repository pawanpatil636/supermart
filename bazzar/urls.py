from django.urls import path
from .import views

app_name="bazzar"
urlpatterns  =[
    path("add-product/", views.add_product_view, name="add_product"),
    path("product-list/", views.product_list_view, name="product_list"),
    path("product-details/<int:pk>/", views.product_details_view, name="product_details"),
    path("coustomer-address-payment/<int:pk>/", views.coustomer_address_payment, name="coustomer_address_payment"),
    path("checkout-view/<int:pk>/", views.checkout_view, name="checkout_view"),
    # path("product-delete/<int:pk>/", views.product_delete_view, name="product_delete"),
    path("product-update-view/<int:pk>/", views.product_update_view, name="product_update_view"),

]