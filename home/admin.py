from django.contrib import admin

from home.models import Booking, Contact,Members

# Register your models here.
admin.site.register(Contact)
admin.site.register(Booking)
admin.site.register(Members)