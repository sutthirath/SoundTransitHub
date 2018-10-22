from django import forms
from .models import Account

class Details(forms.ModelForm):
    email = forms.EmailField()
    address = forms.CharField(max_length=50)
    city = forms.CharField(max_length=20)
    state = forms.CharField(max_length=2)
    zipcode = forms.IntegerField(min_value=10000, max_value=99999)

    class Meta:
        model = Account
        fields = ('email', 'address', 'city', 'state', 'zipcode')


