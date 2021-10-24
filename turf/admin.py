from django.contrib import admin
from . models import turf,turf_add,turf_facility,Pricing_chart,Booking_slot3,M_Host

# Register your models here.
admin.site.register(turf)
admin.site.register(turf_add)
admin.site.register(turf_facility)
admin.site.register(Pricing_chart)
admin.site.register(Booking_slot3)
admin.site.register(M_Host)