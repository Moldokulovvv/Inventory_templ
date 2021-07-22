from django.contrib import admin

from institution.models import Institution, Address, Oblast

admin.site.register(Institution)
admin.site.register(Address)
admin.site.register(Oblast)

