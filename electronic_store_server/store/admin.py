from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Device)
admin.site.register(Basket)
admin.site.register(BasketItem)
admin.site.register(Brand)
admin.site.register(Type)