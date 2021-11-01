from django.contrib import admin

from accounts.models import ExtendedUser

# Register your models here.
@admin.register(ExtendedUser)
class ExtendedUserAdmin(admin.ModelAdmin):
    pass