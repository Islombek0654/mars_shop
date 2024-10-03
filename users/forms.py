from django.forms import ModelForm
from .models import CustomerUser


class Sighn_up_Form(ModelForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'avatar', 'password')



class Sign_in_Form(ModelForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'password')



class Edit_form(ModelForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'avatar')