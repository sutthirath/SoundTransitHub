from django import forms

class Address(forms.Form):
    address = forms.CharField(label='Adress', max_length=100)
    city = forms.CharField(label='City', max_length=100)
    state = forms.CharField(label='State', max_length=2)
    zipcode = forms.IntegerField(min_value=10000, max_value=99999)


