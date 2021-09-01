from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.forms import fields
from home import models

from home.models import Account

class RegistrationForm( UserCreationForm ):
    
    email = forms.EmailField( max_length = 255, help_text = "Required. Add a valid email address")

    class Meta:
        model = Account
        fields = ('email','username','password1','password2')

    def clean_email( self ):

        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.get( email = email )
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email is already in use.")
        # raise forms.ValidationError(f"Email {email} is already in use.")
    
    def clean_username( self ):
        
        username = self.cleaned_data['username'].lower()
        try:
            account = Account.objects.get( username = username )
        except Exception as e:
            return username
        raise forms.ValidationError(f"Username is already in use.")
        # raise forms.ValidationError(f"Username {username} is already in use.")
            
class AccountAuthenticationForm( forms.ModelForm ):
    
    password = forms.CharField( label = "Password", widget = forms.PasswordInput )
    
    class Meta:
        
        model = Account
        fields = ( "email", "password" )

    def clean( self ):

        if self.is_valid():

            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate( email = email, password = password ):
                
                raise forms.ValidationError(f"Invalid Login" )

class ProfileUpdateForm( forms.ModelForm ):

    class Meta:
        model = Account
        fields = ('full_name','phone_number','address','email')

    # def clean_email( self ):

    #     email = self.cleaned_data['email'].lower()
    #     try:
    #         account = Account.objects.get( email = email )
    #     except Exception as e:
    #         return email
    #     raise forms.ValidationError(f"Email { email } is already in use.")

    # def clean_phone_number ( self ):

    #     phone_number = self.cleaned_data['phone_number']
    #     for char in phone_number:
    #         if not char.isdigit():
    #             raise forms.ValidationError("Phone number must be number")

    # def clean_full_name( self ):
        
    #     full_name = self.cleaned_data['full_name']
    #     for char in full_name:
    #         if not char.isalpha():
    #             raise forms.ValidationError("Name must not contain number")
    
    def save( self, commit = True ):

        account = super( ProfileUpdateForm, self ).save( commit = False )
        account.full_name = self.cleaned_data['full_name']
        account.phone_number = self.cleaned_data['phone_number']
        account.address = self.cleaned_data['address']
        account.email = self.cleaned_data['email'].lower()
        if commit:
            account.save()
        return account
                                