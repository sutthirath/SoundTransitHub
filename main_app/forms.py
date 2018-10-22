from django import forms
from .models import Account, Comment

class Details(forms.ModelForm):
    email = forms.EmailField()
    address = forms.CharField(max_length=50)
    city = forms.CharField(max_length=20)
    state = forms.CharField(max_length=2)
    zipcode = forms.IntegerField(min_value=10000, max_value=99999)

    class Meta:
        model = Account
        fields = ('email', 'address', 'city', 'state', 'zipcode')


class CommentForm(forms.ModelForm):
    title = forms.CharField(max_length=20)
    content = forms.Textarea()

    class Meta:
        model = Comment
        fields = ('title', 'content')