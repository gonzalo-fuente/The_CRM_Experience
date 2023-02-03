from django.contrib import admin
from .models import *

# Change default headers

admin.site.site_header = "The CRM Experience"
admin.site.site_title = "CRM Administration Area"
admin.site.index_title = "Welcome to The CRM Experience Administration Area"

# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)