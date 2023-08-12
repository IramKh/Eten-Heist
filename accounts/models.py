from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Users_Name(models.Model):
    user_name= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    email= models.EmailField()
    phone= models.IntegerField()

    def _str_(self):
        return self.user_name

class login(models.Model):
    user_id = models.ForeignKey(Users_Name, on_delete=models.CASCADE)
    login_date_time= models.DateField()



class Customer(models.Model):
    
    Customer_first_name=models.CharField(max_length=50)
    Customer_Last_Name=models.CharField(max_length=50)
    Customer_Email=models.EmailField()
    Customer_Password=models.TextField(max_length=20)
    Customer_Contact_Number=models.TextField(max_length=15)
    Customer_Address=models.TextField(max_length=500, null= True)
    
    def _str_(self):
        return self.Customer_Email









class Contact_Us(models.Model):
    first_name=models.CharField(max_length=50)
    email=models.EmailField()
    subject= models.CharField(max_length=500)
    message= models.CharField(max_length=500)

class Products(models.Model):
    ProductName=models.CharField(max_length=50)
    BranchName=models.CharField(max_length=50)
    Price=models.IntegerField()
    Type=models.CharField(max_length=50)
    Image=models.ImageField(upload_to='images')
    Location=models.CharField(max_length=50,default="All")
    Time=Time=models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)

class Order(models.Model):
    UserID=models.ForeignKey(User, on_delete=models.CASCADE)
    Status=models.CharField(max_length=50)
    TotalBill=models.FloatField()
    Time=Time=models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)
    
class OrderDetails(models.Model):
    OrderID=models.ForeignKey(Order, on_delete=models.CASCADE)
    ProductName=models.CharField(max_length=50)
    BranchName=models.CharField(max_length=50)
    Price=models.IntegerField()
    Type=models.CharField(max_length=50)
    Quantity=models.IntegerField(default=0)
    Time=Time=models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)

#--------------PRODUCT---------------------
class Our_Product(models.Model):
	name=models.CharField(max_length=50)
	price=models.IntegerField()
	Discount=models.IntegerField()
	Description=models.CharField(max_length=150)
	image=models.ImageField(upload_to='images')

	def str(self):
		return self.name

	def get_absolute_url(self):
		return reverse ('accounts:product_details', args=[self.id])


#-------Stock------




class test_details(models.Model):
    test_para=models.CharField(max_length=150)
    test_name=models.CharField(max_length=50)

class about_page(models.Model):
    about_para1=models.CharField(max_length=150)

class term_details(models.Model):
    term_para=models.CharField(max_length=150)

class Blog_details(models.Model):
    Blog_para=models.CharField(max_length=150)
    Blog_date=models.DateTimeField()

    Blog_img=models.ImageField(upload_to='image')



class req(models.Model):
    status=models.CharField(max_length=255, default='Pending')


    def __str__(self):
        return str(self.id)



class orderel(models.Model):
    order = models.ForeignKey(req, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quan= models.IntegerField()

    def __str__(self):
        return str(self.order)
    
    
class lunch(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    Description=models.CharField(max_length=150)
    image=models.ImageField(upload_to='images')
    def str(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse ('accounts:products_detail', args=[self.id])
    
class breakfast(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    Description=models.CharField(max_length=150)
    image=models.ImageField(upload_to='images')
        
    def str(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse ('accounts:products_detail', args=[self.id])
