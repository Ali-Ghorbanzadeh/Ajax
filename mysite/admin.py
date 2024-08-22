from django.contrib import admin
from .models import Discount, Order


admin.site.register([Discount, Order])
