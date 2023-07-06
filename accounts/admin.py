from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomerUserCreationForm,CustomerUserChangeForm
from .models import CustomerUser


class CustomerUserAdmin(UserAdmin):
    add_form=CustomerUserCreationForm
    form=CustomerUserChangeForm
    model=CustomerUser
    list_display=['email','username','first_name','last_name','age','is_staff',]
    fieldsets=UserAdmin.fieldsets + (
        (None,{'fields':('age',)}),
    )
    add_fieldsets=UserAdmin.add_fieldsets+(
        (None,{'fields':('age',)}),
    )
admin.site.register(CustomerUser,CustomerUserAdmin)
