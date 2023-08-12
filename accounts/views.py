from errno import ESTALE
from django.shortcuts import get_object_or_404, redirect, render
from urllib3 import Retry
from accounts.models import *
from . forms import CustomerUpdateForm, CreateUserForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
import socket
socket.getaddrinfo('localhost', 25)


# Create your views here.from django.http import HttpResponse
def home(request):
    location="ALL"
    loclist=[]
    pro=Products.objects.all()
    for data in pro:
        if data.Location in loclist:
            pass
        else:
            loclist.append(data.Location)

    temp=Our_Product.objects.all()
    temp1=Contact_Us.objects.all()
    if request.method=="POST":
        if request.POST.get("loc"):
            location=request.POST.get("loc")
        else:
            fname=request.POST['name']
            email=request.POST[email]
            subject=request.POST['subject']
            msg=request.POST['message']
            ins=Contact_Us(first_name=fname,email=email,subject=subject,messages=msg)
            ins.save()
    return render (request, 'accounts/index.html',{'about':temp1,'abt':temp,'Location':location,'products':loclist})

def userprofile(request):
    usr=User.objects.get(username=request.user)

    if request.method=="POST":
        usr.first_name=request.POST.get('fname')
        usr.last_name=request.POST.get('lname')
        usr.email=request.POST.get('email')
        usr.save()
    return render(request,'accounts/profile_user.html',{"usr":usr})

def testimonials(request):
    temp1= test_details.objects.all()

    return render(request, 'accounts/Testimonials.html', {'abt':temp1})

def products(request):
	temp= Our_Product.objects.all()
	return render (request, 'accounts/products.html',{'about':temp})

def about(request):
	temp=about_page.objects.all()
	return render (request, 'accounts/about.html',{'about':temp})

def contact(request):
	temp= Contact_Us.objects.all()
	temp1= Contact_Us.objects.all()
	if request.method=="POST":
		fname= request.POST['name']
		email= request.POST['email']
		subject= request.POST['subject']
		msg= request.POST['message']
		ins= Contact_Us(name=fname,email=email, subject=subject, message= msg)
		ins.save()
	return render (request, 'accounts/contact.html',{'about':temp1,'abt':temp})
 


def blog(request):
	temp=Blog_details.objects.all()
	return render (request, 'accounts/blog.html',{'about':temp})

def blog_post(request):
	return render (request, 'accounts/blog-post.html')

def checkout(request):
    totalBill=0.0
    obj=request.session['cart']
    for key,value in obj.items():
        totalBill+=float(value['quantity'])*float(value['price'])

    ordrid=Order.objects.create(UserID=request.user,Status="Pending",TotalBill=totalBill)

    for key,value in obj.items():
        OrderDetails.objects.create(OrderID=ordrid,ProductName=value['name'],BranchName=value['branchName'],Price=value['price'],Type=value['type'],Quantity=value['quantity'])
    cart_clear(request)
    return redirect('orderdetail')

def orderdetail(request):
    ordrobj=Order.objects.filter(UserID=request.user)
    ordrprod=OrderDetails.objects.all()
    return render (request, 'accounts/OrderDetails.html',{"Order":ordrobj,"OrderProducts":ordrprod})

def terms(request):
	temp=term_details.objects.all()
	return render (request, 'accounts/terms.html',{'about':temp})

def testimonials(request):
	temp=test_details.objects.all()
	return render (request, 'accounts/testimonials.html',{'about':temp})

def CustomerUpdate(request, pk):
    order=  Customer.objects.get(id=pk)
    form= CustomerUpdateForm(instance=order)
    if request.method == 'POST':
        form= CustomerUpdateForm(request.POST, instance= order)
        if form.is_valid:
            form.save()
            return redirect('/CustomerInfo/')
    context= {'form': form}
    return render(request, 'accounts/CustomerUpdate.html',context)

def customer_info(request):
    temp2= Customer.objects.all()
    return render(request, 'accounts/CustomerInfo.html',{'cus':temp2})


def CustomerDelete(request, pk):
    order= Customer.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/CustomerInfor')
    context= {'item': order}
    return render(request, 'accounts/CustomerDelete.html',context)

def messages(request):
	temp= Contact_Us.objects.all()

	context={'abt':temp}
	return render (request, 'accounts/messages.html' ,context)

def product_details(request, id):
    product= get_object_or_404(Our_Product,id=id)
    return render(request,'accounts/product-details.html', {'product':product})

def Admin_Login(request):
    return render(request,'accounts/Admin_Login.html')

def register(request):
    if request.method=="POST":
        try:
            # Get the post parameters
            username=request.POST['Username']
            email=request.POST['email']
            fname=request.POST['Fname']
            lname=request.POST['Lname']
            pass1=request.POST['Password']
            pass2=request.POST['Re-Type']

            # username should be alphabetic
            if not username.isalpha():
                return render(request, 'accounts/Register.html',{"username":"username should be Alphabetic"} )

            

            # password should match 
            if (pass1!= pass2):
                return render(request, 'accounts/Register.html',{"pas":"Passwords do not match"})
            # Create the user
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name= fname
            myuser.last_name= lname
            myuser.save()
            return redirect('Login')
        except Exception as e:
            return render(request, 'accounts/Register.html',{"pas":e})
    return render(request, 'accounts/Register.html')


def CustomerData(request):
    temp2= Customer.objects.all()
    if request.method=="POST":
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        Address= request.POST.get('address')
        number= request.POST['number']
        ins=Customer(Customer_first_name=fname,Customer_Email=email, Customer_Last_Name=lname, Customer_Address= Address,Customer_Contact_Number=number)
        ins.save()
        return redirect('Login')
    return render(request, 'accounts\CustomerData.html')




def post(self_, request):
	product = request.POST.get['product']
	print(product)
	return redirect('index')

def Login(request):
    err=""
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                err='Username OR password is incorrect'
        context = {"err":err}
        return render(request, 'accounts\Login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('index')








def store(request):
    template = render_to_string('accounts\email_template.html', {'name': request.user.username})
    email = EmailMessage(
        'Thanks for Purchasing',
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email],
    )
    email.fail_silently=False
    email.send()

    cart = Cart(request)
    ab=request.session['cart']
    print(ab)
    req.objects.create()
    max_val=req.objects.latest('id')
    print(max_val)
    for key,value in ab.items():
        print(value['name'])

        orderel.objects.create(order=max_val, name=value['name'], quan=value['quantity'], price=value['price'])

    cart.clear()

    return render(request, 'accounts/success.html', {'cart': cart})



from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse, HttpResponseBadRequest
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='accounts/pdf')
	return None


data = {
	"company": "Eten Heist",
	"address": "Near Wapda Colony Multan, ABC 10001 Pakistan",
	"city": "Multan",
	"zipcode": "98663",


	"phone": " +92 333 3451111",
	"email": "etenheist@gmail.com",
	"website": "https://waterfiltration.herokuapp.com/",
	}

#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('accounts/pdf_template.html', data)
		return HttpResponse(pdf, content_type='accounts/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('accounts/pdf_template.html', data)

		response = HttpResponse(pdf, content_type='accounts/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response

def index(request):
	return render(request, 'accounts/cart_detail.html')

def breakfast(request,location):
    if location=="ALL":
        bfast=Products.objects.filter(Type="Breakfast")

        if request.method == 'POST':
            l=[]
            price=int(request.POST["range"])
            for x in bfast:
                if x.Price<=price:
                    l.append(x)
            return render (request, 'accounts/breakfast.html',{"foods":l})

        return render (request, 'accounts/breakfast.html',{"foods":bfast})

    else:
        bfast=Products.objects.filter(Type="Breakfast",Location=location)
        if request.method == 'POST':
            l=[]
            price=int(request.POST["range"])
            for x in bfast:
                if x.Price<=price:
                    l.append(x)
            return render (request, 'accounts/breakfast.html',{"foods":l})

        return render (request, 'accounts/breakfast.html',{"foods":bfast})

    

def lunch(request,location):
    if location=="ALL":
        lunch=Products.objects.filter(Type="Lunch")
        if request.method == 'POST':
            l=[]
            price=int(request.POST["range"])
            for x in lunch:
                if x.Price<=price:
                    l.append(x)
            return render (request, 'accounts/lunch.html',{"foods":l})

        return render (request, 'accounts/lunch.html',{"foods":lunch})
    else:
        lunch=Products.objects.filter(Type="Lunch",Location=location)
        if request.method == 'POST':
            l=[]
            price=int(request.POST["range"])
            for x in lunch:
                if x.Price<=price:
                    l.append(x)
            return render (request, 'accounts/lunch.html',{"foods":l})

        return render (request, 'accounts/lunch.html',{"foods":lunch})

def Dinner(request,location):
    if location=="ALL":
        dinner=Products.objects.filter(Type="Dinner")
        if request.method == 'POST':
            l=[]
            price=int(request.POST["range"])
            for x in dinner:
                if x.Price<=price:
                    l.append(x)
            return render (request, 'accounts/Dinner.html',{"foods":l})

        return render (request, 'accounts/Dinner.html',{"foods":dinner})
    else:
        dinner=Products.objects.filter(Type="Dinner",Location=location)
        if request.method == 'POST':
            l=[]
            price=int(request.POST["range"])
            for x in dinner:
                if x.Price<=price:
                    l.append(x)
            return render (request, 'accounts/Dinner.html',{"foods":l})

        return render (request, 'accounts/Dinner.html',{"foods":dinner})


def Restaurant_registration(request):
    	return render (request, 'accounts/Restaurant_registration.html')
 
#add to cart_view
@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

@login_required(login_url="/users/login")
def cart_detail(request):
    total=0.00
    cart = Cart(request)
    ab=request.session['cart']

    for key,value in ab.items():
        #print(value['name'])
        total = float( float(value['price'])* float(value['quantity'])) + total

    return render(request, 'accounts/cart_detail.html',{'total':total})

@login_required(login_url="/users/login")
def deletecartitem(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product=product)
    return redirect("cart_detail")




def adminpanel(request):
	return render (request, 'adminpanel/index1.html')


def rider(request):
	return render (request, 'accounts/rider.html')

def poached_egg(request):
	return render (request, 'accounts/poached-egg.html')

def pizza(request):
	return render (request, 'accounts/pizza.html')

def egg_paratha(request):
	return render (request, 'accounts/egg-paratha.html')

def biryani(request):
    	return render (request, 'accounts/biryani.html')

