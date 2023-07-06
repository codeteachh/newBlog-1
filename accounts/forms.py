from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomerUser

class CustomerUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomerUser
        fields=('username','first_name','last_name','email','age',)

class CustomerUserChangeForm(UserChangeForm):
            class Meta:
                model=CustomerUser
                fields=('username','first_name','last_name','email','age',)



