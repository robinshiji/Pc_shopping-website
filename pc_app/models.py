from django.db import models


USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('staff','Staff'),
    ]

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)  # username should be unique and non-nullable
    password = models.CharField(max_length=150)  # Password should not be null for new entries
    usertype = models.CharField(max_length=5, choices=USER_TYPE_CHOICES, default='user')  # User type defaults to 'user'

    def __str__(self):
        return self.username

class staff(models.Model):
    usertype = models.CharField(max_length=5, choices=USER_TYPE_CHOICES, default='staff')
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.IntegerField()
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    

class Company(models.Model):
    companyname = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.companyname

class product(models.Model): #for custom products
    company = models.ForeignKey(Company, on_delete=models.CASCADE) 
    productname=models.CharField(max_length=255)
    desc=models.CharField(max_length=100,null=True)
    price=models.IntegerField()
    photo=models.ImageField(upload_to='static/images')
    category=models.CharField(max_length=255,null=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User
    product = models.ForeignKey(product, on_delete=models.CASCADE ,blank=True ,null=True)  # Link to Product
    quantity = models.IntegerField(default=1)
    


    def __str__(self):
        return f'{self.user.username} - {self.product.productname} ({self.quantity})'



ORDER_STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Shipped', 'Shipped'),
    ('out for delivery', 'Out for delivery'),
    ('delivered', 'Delivered'),
    ('Product Returned', 'Product Returned'),
]


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='Pending')
    def __str__(self):
        return f'Order {self.id} by {self.user.username}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.productname} in Order {self.order.id}'

class makepayment(models.Model):
    cardnumber=models.IntegerField()
    name=models.CharField(max_length=255)
    cvv=models.IntegerField()


class services(models.Model):
    name=models.CharField(max_length=255 ,null=True)
    email=models.CharField(max_length=50)
    service_type=models.CharField(max_length=150)
    description=models.TextField()
    status = models.CharField(max_length=20, default='Pending') 


