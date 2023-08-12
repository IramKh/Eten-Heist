from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Users_Name)
admin.site.register(login)

admin.site.register(Customer)

admin.site.register(Contact_Us)
admin.site.register(Our_Product)


admin.site.register(test_details)
admin.site.register(about_page)
admin.site.register(term_details) 
admin.site.register(Blog_details)
admin.site.register(lunch)
admin.site.register(breakfast)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(OrderDetails)


class OrderItemInline(admin.TabularInline):
    model = orderel
    raw_id_fields = ['order']

@admin.register(req)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    #list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
