from django.shortcuts import render
from adminpanel.models import *
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.


def adminpanel(request):
	return render (request, 'adminpanel.html')

def a(request):
	return render (request, 'adminpanel/a.html')

def animation(request):
	return render (request, 'adminpanel/animation.html')

def restaurants(request):
    	return render (request, 'adminpanel/restaurants.html')
 
def sales(request):
    	return render (request, 'adminpanel/sales.html')
 
 
def widgets(request):
    	return render (request, 'adminpanel/widgets.html')
def orders(request):
    	return render (request, 'adminpanel/orders.html')

 

def chat(request):
    	return render (request, 'adminpanel/apps/chat.html')
 
def email(request):
    	return render (request, 'adminpanel/apps/email.html')
 
def to_do_list(request):
    	return render (request, 'adminpanel/apps/to-do-list.html')
 
def chartjs(request):
    	return render (request, 'adminpanel/charts/chartjs.html')
 
def morris_charts(request):
    	return render (request, 'adminpanel/charts/morris-charts.html')
def customerlist(request):
    	return render (request, 'adminpanel/customer/customerlist.html')
 
def customersreview(request):
    	return render (request, 'adminpanel/customer/customersreview.html')
 
def social(request):
    	return render (request, 'adminpanel/customer/social.html')
 
 
def client_management(request):
    	return render (request, 'adminpanel/dashboard/client-management.html')
 
def project_management(request):
    	return render (request, 'adminpanel/dashboard/project-management.html')
 
def web_analytics(request):
    	return render (request, 'adminpanel/dashboard/web-analytics.html')
def form_elements(request):
    	return render (request, 'adminpanel/form/form-elements.html')
def form_layout(request):
    	return render (request, 'adminpanel/form/form-layout.html')
def form_validation(request):
    	return render (request, 'adminpanel/form/form-validation.html')
def form_wizard(request):
    	return render (request, 'adminpanel/form/form-wizard.html')
 
def a(request):
    	return render (request, 'adminpanel/invoice/a.html')
def invoicedetail(request):
    	return render (request, 'adminpanel/invoice/invoicedetail.html')
def invoicelist(request):
    	return render (request, 'adminpanel/invoice/invoicelist.html')
 
def flaticons(request):
    	return render (request, 'adminpanel/icons/flaticons.html')
def fontawesome(request):
    	return render (request, 'adminpanel/icons/fontawesome.html')
def materialize(request):
    	return render (request, 'adminpanel/icons/materialize.html')
 
def google_maps(request):
    	return render (request, 'adminpanel/maps/google-maps.html')
def vector_maps(request):
    	return render (request, 'adminpanel/maps/vector-maps.html')
def coming_soon(request):
    	return render (request, 'adminpanel/prebuilt-pages/coming-soon.html')
def default_login(request):
    	return render (request, 'adminpanel/prebuilt-pages/default-login.html')
def default_register(request):
    	return render (request, 'adminpanel/prebuilt-pages/default-register.html')
def error(request):
    	return render (request, 'adminpanel/prebuilt-pages/error.html')
def faq(request):
    	return render (request, 'adminpanel/prebuilt-pages/faq.html')
def invoice(request):
    	return render (request, 'adminpanel/prebuilt-pages/invoice.html')
def lock_screen(request):
    	return render (request, 'adminpanel/prebuilt-pages/lock-screen.html')
def modal_login(request):
    	return render (request, 'adminpanel/prebuilt-pages/modal-login.html')
def modal_register(request):
    	return render (request, 'adminpanel/prebuilt-pages/modal-register.html')
def portfolio(request):
    	return render (request, 'adminpanel/prebuilt-pages/portfolio.html')
def user_profile(request):
    	return render (request, 'adminpanel/prebuilt-pages/user-profile.html')
 
def sweet_alerts(request):
    	return render (request, 'adminpanel/popups/sweet-alerts.html')
def toast(request):
    	return render (request, 'adminpanel/popups/toast.html')
 
def addproduct(request):
    	return render (request, 'adminpanel/product/addproduct.html')
def productcata(request):
    	return render (request, 'adminpanel/product/productcata.html')
def productdetail(request):
    	return render (request, 'adminpanel/product/productdetail.html')
def productgrid(request):
    	return render (request, 'adminpanel/product/productgrid.html')
def productlist(request):
    	return render (request, 'adminpanel/product/productlist.html')
 
 
 
def basic_tables(request):
    	return render (request, 'adminpanel/tables/basic-tables.html')
def data_tables(request):
    	return render (request, 'adminpanel/tables/data-tables.html')
 
def accordions(request):
    	return render (request, 'adminpanel/ui-basic/accordions.html')
def alerts(request):
    	return render (request, 'adminpanel/ui-basic/alerts.html')
def badges(request):
    	return render (request, 'adminpanel/ui-basic/badges.html')
def breadcrumbs(request):
    	return render (request, 'adminpanel/ui-basic/breadcrumbs.html')
def buttons(request):
    	return render (request, 'adminpanel/ui-basic/buttons.html')
def cards(request):
    	return render (request, 'adminpanel/ui-basic/cards.html')
def pagination(request):
    	return render (request, 'adminpanel/ui-basic/pagination.html')
def preloaders(request):
    	return render (request, 'adminpanel/ui-basic/preloaders.html')
def progress_bars(request):
    	return render (request, 'adminpanel/ui-basic/progress-bars.html')
def tabs(request):
    	return render (request, 'adminpanel/ui-basic/tabs.html')
def typography(request):
    	return render (request, 'adminpanel/ui-basic/typography.html')
 
 
def cropper(request):
    	return render (request, 'adminpanel/ui-advanced/cropper.html')

def draggables(request):
    	return render (request, 'adminpanel/ui-advanced/draggables.html')
def range_slider(request):
    	return render (request, 'adminpanel/ui-advanced/range-slider.html')
def modals(request):
    	return render (request, 'adminpanel/ui-advanced/modals.html')
def rating(request):
    	return render (request, 'adminpanel/ui-advanced/rating.html')
def sliders(request):
    	return render (request, 'adminpanel/ui-advanced/sliders.html')

def tour(request):
    	return render (request, 'adminpanel/ui-advanced/tour.html')
 
 
 
