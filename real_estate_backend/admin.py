from django.contrib import admin
from .models import Properties

# Register your models here.
class RentLeasePurchase(admin.ModelAdmin):
    list_display = ["property_type",
                    "property_description", 
                    "property_location", 
                    "property_price", 
                    "bedroom_desc", 
                    "bathroom_desc",
                    "toilet_desc",]

admin.site.register(Properties, RentLeasePurchase)
