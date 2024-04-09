
from django.urls import path
from .import views

urlpatterns = [
    # path("",views.index,name="Shop"),
    path("",views.index,name="index"),
    path("shop/index/",views.index,name="index"),
    path("shop/about/",views.about,name="about"),

    path("shop/contact/",views.contact,name="contactUs"),
    path("shop/tracker/",views.tracker,name="tracker"),
    path("shop/search/",views.search,name="search"),
    path("shop/products/<int:myid>",views.productview,name="productView"),
    path("shop/checkout/",views.checkout,name="Checkout"),
    path("shop/handlerequest/",views.handlerequest,name="HandleRequest"),
    # path("cart/",views.cart,name="Cart"),
]
