from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name=("main")),
    path('index.html/',views.home, name=("index")),
    path('products.html/',views.products, name=("products")),

    path('contact.html/',views.contact, name=("contact")),
    path('blog.html/',views.blog, name=("blog")),
    path('blog-post.html/',views.blog_post, name=("blog-post")),
    path('checkout',views.checkout, name=("checkout")),
    path('terms.html/',views.terms, name=("terms")),
    path('about.html/',views.about, name=("about")),
    path('testimonials.html/',views.testimonials, name=("testimonials") ),
    path('cu.html/',views.about, name=("about")),
    path('about.html/',views.about, name=("about")),
    path('CustomerInfo/', views.customer_info, name=("CustomerInfo")),
    path('CustomerUpdate/<str:pk>', views.CustomerUpdate, name=("CustomerUpdate")),
    path('CustomerDelete/<str:pk>', views.CustomerDelete, name=("CustomerDelete")),
    path('messages', views.messages, name=("messages")),

    path('product_details/<str:id>', views.product_details, name='product_details'),

    path('store', views.store, name='store'),
    path('Admin_Login/',views.Admin_Login, name='Admin_Login'),
    path('register/',views.register, name='register'),
    path('CustomerData/', views.CustomerData, name='CustomerData'),
    path('Login/', views.Login, name=("Login")),
    path('logout/', views.logoutUser, name="logout"),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
    
   
    path('breakfast/<str:location>',views.breakfast, name=("breakfast")),
    path('lunch/<str:location>',views.lunch, name=("lunch")),
    path('Dinner/<str:location>',views.Dinner, name=("Dinner")),
    path('userprofile/',views.userprofile, name=("userprofile")),
    
    path('rider/',views.rider, name=("rider")),
    path('poached-egg/',views.poached_egg, name=("poached-egg")),
    path('pizza/',views.pizza, name=("pizza")),
    path('egg-paratha/',views.egg_paratha, name=("egg-paratha")),
    path('biryani/',views.biryani, name=("biryani")),
  
    
    path('Restaurant_registration/',views.Restaurant_registration, name=("Restaurant_registration")),
    
    #cart data--------------------------------
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),

    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),

    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),

    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),

    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),

    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    path('cart/deletecartitem/<int:id>',views.deletecartitem,name='deletecartitem'),

    path('orderdetail',views.orderdetail, name=("orderdetail")),

]
