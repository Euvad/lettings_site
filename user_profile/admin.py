from django.contrib import admin
from .models import Profile

# Check if Profile is already registered
if not admin.site.is_registered(Profile):

    class ProfileAdmin(admin.ModelAdmin):
        list_display = ("user", "favorite_city")

    admin.site.register(Profile, ProfileAdmin)

# Register your models here.
