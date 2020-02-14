from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import BaseUser as User
from .forms import UserAdminCreationForm, UserAdminChangeForm
from farmer.models import Farmer
from supplier.models import Supplier
from retailer.models import Retailer


# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_superuser')
    list_filter = ('is_superuser', 'active')
    fieldsets = (
        (None, {'fields': ('name', 'contact', 'email', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'contact', 'email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'full_name', 'contact')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Farmer)
admin.site.register(Retailer)
admin.site.register(Supplier)
