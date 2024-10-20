from django.urls import path
from .import views
from .views import *

urlpatterns = [
    #admin section
    path('',views.home, name='home'),  # Correct path to the 'home' view
    path('register/',views.register,name='register'),
    path('login_user/',views.login_user,name='login_user'),
    path('logout/',views.logout,name='logout'),
    path('adminpage/',views.adminpage,name='adminpage'),
    path('admincustom/',views.custompage,name='custompage'),
    path('add-company/', views.add_company, name='add_company'),
    path('update-company/<int:company_id>/', update_company, name='update_company'),
    path('deletecompany/<int:company_id>/',delete_company,name='delete_company'),
    path('product/',views.productadd,name='productadd'),
    path('viewproduct/',views.viewproduct,name='viewproduct'),
    path('updateproduct/<int:product_id>/', update_product,name='updateproduct'),
    path('deleteproduct/<int:product_id>/',deleteproduct,name='deleteproduct'),
    path('addstaff/',views.addstaff,name='addstaff'),
    path('orders/admin', admin_view_orders, name='admin_view_orders'),
    path('change_order_status/<int:order_id>/', change_order_status, name='change_order_status'),
    path('order/delete/<int:order_id>/', views.delete_order, name='delete_order'),
   
    #user section
    path('custombuild/',views.custombuild,name='custombuild'),
    path('userpage/',views.userpage,name='userpage'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('viewcart/',views.view_cart,name='view_cart'),
    path('remove_cart/',views.remove_cart,name='remove_cart'),
    path('place_order/', views.place_order, name='place_order'),
    path('orders/', view_order, name='view_order'),  # URL to view all orders
    path('orders/<int:order_id>/', view_order_detail, name='view_order_detail'),  # URL to view a specific order
    path('order/cancel/<int:order_id>/', cancel_order, name='cancel_order'),
    path('return_product/<int:order_id>/', return_product, name='return_product'),
    path('user/makepayments/', views.makepayments, name='makepayments'),
    path('card/payment' ,views.cardpayment, name='cardpayment'),
    path('cashdelivery/', views.cashdelivery,name='cashdelivery'),
    path('user/services/',views.service_view,name='service_view'),
    path('my-requests/', views.user_service_requests, name='user_service_requests'),
    
   
    #staff section 
    path('staffpage/',views.staffpage,name='staffpage'),
    path('service_request/', service_request, name='service_request'),
    path('requests/approve/<int:request_id>/', views.approve_request, name='approve_request'),
    path('requests/reject/<int:request_id>/', views.reject_request, name='reject_request'),
    path('delete/<int:service_request_id>/', views.delete_request, name='delete_request'),

    
   

   
   
]