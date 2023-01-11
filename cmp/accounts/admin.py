from django.contrib import admin
from .models import *

# Change default headers

admin.site.site_header = "CMP Admin"
admin.site.site_title = "CMP Admin Area"
admin.site.index_title = "Welcome to the Customer Management Platform Administration Area"

# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)