from django.contrib import admin
from .models import Person


class SAAdmin(admin.ModelAdmin):
    
    list_display = ('Firstname', 'Lastname', 'Email','PhoneNo')


admin.site.register(Person ,SAAdmin)

