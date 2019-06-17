from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(label="Password",max_length=100)



class OneForm(forms.Form):
    name = forms.CharField(label='NAME', max_length=100)
    age = forms.IntegerField(label='Age')
    image = forms.ImageField()
    dob = forms.DateField(label='Date of Birth')
