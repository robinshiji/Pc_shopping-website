from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import get_object_or_404


#home page
def home(request):
    return render(request,'index.html')

#register page
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Set user type to 'user' by default
        usertype = 'user'  # Default user type for regular users

        # Validate inputs
        if not username or not password:
            messages.error(request, 'Username and password are required.')
            return redirect('register')

        try:
            user = User(username=username, password=password, usertype=usertype)
            user.save()
            messages.success(request, 'Registration successful!')
            return redirect('login_user')  # Redirect to the login page
        except Exception as e:
            messages.error(request, 'Registration failed:')
            return redirect('register')  # Redirect back to register

    return render(request, 'register.html')

#login page
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Check in the User model
        user = User.objects.filter(username=username).first()  # Use filter() and first() to avoid MultipleObjectsReturned

        if user:  # User found in User model
            if user.password == password:  # Compare plain text passwords
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                messages.success(request, 'Login successful!')

                # Redirect based on user role
                if user.usertype == 'admin':
                    return redirect('adminpage')
                elif user.usertype == 'staff':
                    return redirect('staffpage')
                else:  # Regular user
                    return redirect('userpage')
            else:
                messages.error(request, 'Invalid credentials. Please try again.')
        else:  # User not found, check in the Staff model
            staff_member = staff.objects.filter(username=username).first()  # Use filter() and first()

            if staff_member:
                if staff_member.password == password:  # Compare plain text passwords
                    request.session['user_id'] = staff_member.id
                    request.session['username'] = staff_member.username
                    messages.success(request, 'Login successful!')

                    return redirect('staffpage')  # Redirect to staff home
                else:
                    messages.error(request, 'Invalid credentials. Please try again.')
            else:
                messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'login.html')
#logout page

def logout(request):
    request.session.flush()  # Clear session data
    messages.success(request, 'You have been logged out.')
    return redirect('home')  # Redirect to login page after logout

#admin pages 
def adminpage(request):
    return render(request,'admin/adminhome.html')

def custompage(request):
    return render(request,'admin/custompage.html')

def add_company(request):
    if request.method == 'POST':
        company_name = request.POST.get('companyname')

        if company_name: 
            company = Company(companyname=company_name)
            company.save()
            return redirect('add_company')  
    comp = Company.objects.all()
    return render(request, 'admin/addcompany.html', {'comp':comp})



def productadd(request):
    if request.method=='POST':
        company=request.POST.get('company_id')
        productname=request.POST.get('productname')
        descr=request.POST.get('desc')
        photo = request.FILES.get('photo') 
        price=request.POST.get('price')
        category=request.POST.get('category')
        products=product(company_id=company,productname=productname,desc=descr,photo=photo,price=price,category=category)
        products.save()
        return redirect('viewproduct')
    companies = Company.objects.all()

    return render(request,'admin/addproduct.html',{'companies': companies})

def viewproduct(request):
    produ=product.objects.all()

    return render(request,'admin/viewproduct.html',{'produ':produ})


def update_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    if request.method == 'POST':
        # Handle updating the company name
        company_name = request.POST.get('companyname')
        if company_name:
            company.companyname = company_name
            company.save()
            return redirect('add_company')  # Redirect after updating

    return render(request, 'admin/updatecompany.html', {'company': company})

def delete_company(request,company_id):
     company = get_object_or_404(Company, id=company_id)
     company.delete()
     return redirect('add_company')

def update_product(request, product_id):
    Product = get_object_or_404(product, id=product_id)

    if request.method == 'POST':
        productname = request.POST.get('productname')
        desc = request.POST.get('desc') 
        price = request.POST.get('price')
        photo = request.FILES.get('photo')
        category=request.POST.get('category')
        Product.productname = productname
        Product.desc= desc
        Product.price = price
        Product.category = category
        if photo:
            Product.photo = photo

        Product.save()
        return redirect('viewproduct')

    return render(request, 'admin/updateproduct.html', {'Product': Product})

def deleteproduct(request, product_id):  # Change to match the URL pattern
    Product = get_object_or_404(product, id=product_id)
    Product.delete()
    return redirect('viewproduct')

#adding staff from admin
def addstaff(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        username=request.POST.get('username')
        password=request.POST.get('password')
        staff_detail=staff(name=name,email=email,phone=phone,username=username,password=password,usertype='staff')
        staff_detail.save()
        return redirect('adminpage')
    return render(request,'admin/addstaff.html')

def admin_view_orders(request):
    orders = Order.objects.all()  # Get all orders
    return render(request, 'admin/view_orders.html', {'orders': orders})

def change_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()
        return redirect('admin_view_orders')  # Redirect to the orders view after changing status
    
    # Pass status choices to the template
    status_choices = Order._meta.get_field('status').choices
    return render(request, 'admin/change_order_status.html', {
        'order': order,
        'status_choices': status_choices,
    })



#USER CODE 
def custombuild(request):
    products=product.objects.all()
    return render(request,'user/custombuild.html',{'products':products})

def userpage(request):
    return render(request,'user/Welcome.html')

def add_to_cart(request, product_id):
    if request.session.get('username'):
        user_id = request.session.get('user_id')
        user = get_object_or_404(User, id=user_id)

        # Get the product by ID
        product_item = get_object_or_404(product, id=product_id)

        # Add to cart logic
        cart_item, created = Cart.objects.get_or_create(user=user, product=product_item)

        if not created:
            # If the cart item already exists, increment the quantity
            cart_item.quantity += 1
            cart_item.save()
           

        return redirect('view_cart')  # Redirect to the cart view

    return redirect('login')  # Redirect to login or

def view_cart(request):
    if request.session.get('username'):
        user_id = request.session.get('user_id')
        user = User.objects.get(id=user_id)
        
        # Get all cart items for the user
        cart_items = Cart.objects.filter(user=user)

        total_price = sum(item.product.price * item.quantity for item in cart_items)

        return render(request, 'user/cart.html', {'cart_items': cart_items,'total_price':total_price })
    
def remove_cart(request):
    cart=Cart.objects.all()
    cart.delete()
    return redirect('view_cart')


def place_order(request):
    user_id = request.session.get('user_id')
    if not user_id:
        
        return redirect('login')

    # Get the user's cart items
    carts = Cart.objects.filter(user_id=user_id)

    if not carts.exists():
       
        return redirect('view_cart')

    # Calculate the total price for the entire cart
    total_price = sum(cart.product.price * cart.quantity for cart in carts)

    # Create the order
    order = Order.objects.create(
        user_id=user_id,
        total_price=total_price,
    )

    # Create order items for each product in the cart
    for cart in carts:
        OrderItem.objects.create(
            order=order,
            product=cart.product,
            quantity=cart.quantity,
            
        )

    # Clear the cart after placing the order
    carts.delete()

   
    return redirect('makepayments')  # Redirect to view orders or another appropriate page


def makepayments(request):
    return render(request,'user/make_payment.html')

def cardpayment(request):

    if request.method == 'POST':
        name=request.POST.get('name')
        cardnumber=request.POST.get('cardnumber')
        cvv=request.POST.get('cvv')

        payments=makepayment(name=name,cardnumber=cardnumber,cvv=cvv)
        payments.save()
        return redirect('view_order')
    
   
    return render(request,'user/card_payment.html')

def cashdelivery(request):
    return redirect('view_order')

def view_order(request):
    user_id = request.session.get('user_id')  # Retrieve user ID from session

    if not user_id:
      
        return redirect('login')

    # Use filter() to fetch all orders for the user
    orders = Order.objects.filter(user_id=user_id)

    if not orders.exists():
        
        return redirect('view_cart')  # Redirect to another view if no orders exist

    return render(request, 'user/view_orders.html', {'orders': orders})  # Pass orders to template

def view_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)  # This is correct for single order retrieval
    order_items = order.items.all()  # Access related items via reverse relation

    return render(request, 'user/order_detail.html', {'order': order, 'order_items': order_items})

def cancel_order(request, order_id):
    user_id = request.session.get('user_id')  # Check if the user is logged in
    if not user_id:
        
        return redirect('login')

    # Get the order by ID, ensuring it belongs to the logged-in user
    order = get_object_or_404(Order, id=order_id, user_id=user_id)

    if order.status == 'Pending':
        order.status = 'Canceled'  # Change status to Canceled
        order.save()
        
    return redirect('view_order') 

def delete_order(request, order_id):
    # Fetch the order object based on order_id
    order = get_object_or_404(Order, id=order_id)
    
    # Delete the order from the database
    order.delete()
    
    # Show a success message
 

    # Redirect to the order list view (replace with your order list URL)
    return redirect('admin_view_orders')

def return_product(request, order_id):
    # Get the order instance
    order = get_object_or_404(Order, id=order_id)

    # Check if the order status is 'Pending' or can be returned
    if order.status == 'Pending':
        
        return redirect('view_order')  # Redirect to the orders view

    # Update the order status to 'Product Returned'
    order.status = 'Product Returned'
    order.save()

    
    return redirect('view_order')

def service_view(request):
    return render(request,'user/services.html')

def service_request(request):

    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        service_type=request.POST.get('service_type')
        description=request.POST.get('description')

        service=services(name=name,email=email,service_type=service_type,description=description)
        service.save()
        return redirect('service_view')
    
   
    return render(request,'user/service_request.html')


def user_service_requests(request):
    # Access user information from request.user
  # Access the user's email correctly
    
    # Fetch the user's requests
    user_requests = services.objects.all()
    
    context = {
        'user_requests': user_requests
    }
    return render(request, 'user/user_service_requests.html', context)



#Staff code 
def staffpage(request):
    req=services.objects.all()
    return render(request,'staff/staff_home.html' ,{'req':req})

def approve_request(request, request_id):
    service_request = get_object_or_404(services, id=request_id)
    service_request.status = 'Approved'
    service_request.save()
   
    return redirect('staffpage')  # Redirect back to the request viewing page

# View to reject a request
def reject_request(request, request_id):
    service_request = get_object_or_404(services, id=request_id)
    service_request.status = 'Rejected'
    service_request.save()
    
    return redirect('staffpage')

def delete_request(request, service_request_id):
    service_request = get_object_or_404(services, id=service_request_id)  # Fetch the object using the correct ID
    service_request.delete()
    return redirect('staffpage')


