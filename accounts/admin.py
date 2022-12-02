from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Buyer

fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Info', {'fields': ('first_name', 'last_name', 'email',
             'country', 'city', 'region', 'address', 'postal_code', 'number_phone')})

UserAdmin.fieldsets = tuple(fields)
admin.site.register(Buyer, UserAdmin)
