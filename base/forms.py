from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserDetails, Sharing, Product
from django.forms import ModelForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def clean(self):
        super(UserForm, self).clean()
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        try:
            check_user = User.objects.get(username=username)
        except:
            check_user = None
        
        try:
            check_email = User.objects.get(email=email)
        except:
            check_email = None

        if check_user is not None:
            self._errors['username'] = self.error_class([
                'This username is already exist'])

        if check_email is not None:
            self._errors['email'] = self.error_class(['This email is already exist`'])
                   
        return self.cleaned_data

class UserDetailsForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = "__all__"
        exclude = ['user']

class SharingForm(ModelForm):
    class Meta:
        model = Sharing
        fields = ['text',]
    

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"