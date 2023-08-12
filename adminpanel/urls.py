from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    
    
    #for adminpanel
    
    path('admin/', admin.site.urls),
    path('', views.adminpanel),
    path('adminpanel/',views.adminpanel, name=("adminpanel")),
    path('a/',views.a, name=("a")),
    path('animation/',views.animation, name=("animation")),
    path('orders/',views.orders, name=("orders")),
    path('restaurants/',views.restaurants, name=("restaurants")),
    path('sales/',views.sales, name=("sales")),
    path('widgets/',views.widgets, name=("widgets")),
    path('chat/',views.chat, name=("chat")),
    path('email/',views.email, name=("email")),
    path('to-do-list/',views.to_do_list, name=("to-do-list")),
    path('chartjs/',views.chartjs, name=("chartjs")),
    path('morris-charts/',views.morris_charts, name=("morris-charts")),
    path('customerlist/',views.customerlist, name=("customerlist")), 
    path('customersreview/',views.customersreview, name=("customersreview")),
    path('social/',views.social, name=("social")),
    path('client-management/',views.client_management, name=("client-management")),
    path('project-management/',views.project_management, name=("project-management")),
    path('web-analytics/',views.web_analytics, name=("web-analytics")),
    path('form-elements/',views.form_elements, name=("form-elements")),
    path('form-layout/',views.form_layout, name=("form-layout")),
    path('form-validation/',views.form_validation, name=("form-validation")),
    path('form-wizard/',views.form_wizard, name=("form-wizard")),
    path('a/',views.a, name=("a")),
    path('invoicedetail/',views.invoicedetail, name=("invoicedetail")),
    path('invoicelist/',views.invoicelist, name=("invoicelist")),
    path('flaticons/',views.flaticons, name=("flaticons")),
    path('fontawesome/',views.fontawesome, name=("fontawesome")),
    path('materialize/',views.materialize, name=("materialize")),
    path('google-maps/',views.google_maps, name=("google-maps")),
    path('vector-maps/',views.vector_maps, name=("vector-maps")),
    path('coming-soon/',views.coming_soon, name=("coming-soon")),
    path('default-login/',views.default_login, name=("default-login")),
    path('default-register/',views.default_register, name=("default-register")),
    path('error/',views.error, name=("error")),
    path('faq/',views.faq, name=("faq")),
    path('invoice/',views.invoice, name=("invoice")),
    path('lock-screen/',views.lock_screen, name=("lock-screen")),
    path('modal-login/',views.modal_login, name=("modal-login")),
    path('modal-register/',views.modal_register, name=("modal-register")),
    path('portfolio/',views.portfolio, name=("portfolio")),
    path('user-profile/',views.user_profile, name=("user-profile")),
    path('sweet-alerts/',views.sweet_alerts, name=("sweet-alerts")),
    path('toast/',views.toast, name=("toast")),
    path('addproduct/',views.addproduct, name=("addproduct")),
    path('productcata/',views.productcata, name=("productcata")),
    path('productdetail/',views.productdetail, name=("productdetail")),
    path('productgrid/',views.productgrid, name=("productgrid")),
    path('productlist/',views.productlist, name=("productlist")),
    
    
    path('basic-tables/',views.basic_tables, name=("basic-tables")),
    path('data-tables/',views.data_tables, name=("data-tables")),
    path('accordions/',views.accordions, name=("accordions")),
    path('alerts/',views.alerts, name=("alerts")),
    path('badges/',views.badges, name=("badges")),
    path('breadcrumbs/',views.breadcrumbs, name=("breadcrumbs")),
    path('buttons/',views.buttons, name=("buttons")),
    path('cards/',views.cards, name=("cards")),
    path('pagination/',views.pagination, name=("pagination")),
    path('preloaders/',views.preloaders, name=("preloaders")),
    path('progress-bars/',views.progress_bars, name=("progress-bars")),
    path('tabs/',views.tabs, name=("tabs")),
    path('typography/',views.typography, name=("typography")),
    
    path('cropper/',views.cropper, name=("cropper")),
   
    path('draggables/',views.draggables, name=("draggables")),
    path('range-slider/',views.range_slider, name=("range-slider")),
    path('modals/',views.modals, name=("modals")),
    path('rating/',views.rating, name=("rating")),
    path('sliders/',views.sliders, name=("sliders")),
    
    path('tour/',views.tour, name=("tour")),

    
    
    
    
    
    

    
    path('modals/',views.modals, name=("modals")),

    

    

]