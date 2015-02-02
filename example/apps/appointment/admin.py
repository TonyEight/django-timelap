from django.contrib import admin
from appointment.models import SimpleEvent, ClassicEvent


admin.site.register(SimpleEvent)
admin.site.register(ClassicEvent)
