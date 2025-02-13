from django.contrib import admin
from .models import Address, Letting

# Check if Address is already registered
if not admin.site.is_registered(Address):

    class AddressAdmin(admin.ModelAdmin):
        list_display = (
            "number",
            "street",
            "city",
            "state",
            "zip_code",
            "country_iso_code",
        )

    admin.site.register(Address, AddressAdmin)

# Check if Letting is already registered
if not admin.site.is_registered(Letting):

    class LettingAdmin(admin.ModelAdmin):
        list_display = ("title", "address")

    admin.site.register(Letting, LettingAdmin)
