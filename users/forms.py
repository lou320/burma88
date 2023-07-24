from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from users.models import Users

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=100, help_text="Required username." )
    profile_image = forms.ImageField(required=False)
    class Meta:
        model = Users
        fields = ('email', 'username', 'password1', 'password2')

    def validate_username(username):
        # Remove leading and trailing spaces
        username = username.strip().lower()

        # Check if the username is empty after removing spaces
        if not username:
            raise forms.ValidationError("Username cannot be empty.")

        # Check if the username already exists in the database
        if Users.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("Username already taken.")

        # Return the normalized username
        return username
    
    def clean_username(self):
        username = self.cleaned_data['username']
        username = username.strip().lower()
        
        try:
            user = Users.objects.get(username = username)
        except Users.DoesNotExist:
            return username
        raise forms.ValidationError(f"Username {username} is already in use.")
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            user = Users.objects.get(email = email)
        except Users.DoesNotExist:
            return email
        raise forms.ValidationError(f"Username {email} is already in use.")
    
    
class UsersAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    class Meta:
        model = Users
        fields = ("email", "password")
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email = email, password=password):
                raise forms.ValidationError("Invalid Login")
            

class UsersUpdateForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('username','email', 'phone', 'social_media_choice','social_media_link')
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if email != self.cleaned_data['email']:
            try:
                Users = Users.object.get(email = email)
            except Users.DoesNotExist:
                return email
            raise forms.ValidationError(f"Email {email} is already in use.")
        else:
            return email
    def clean_username(self):
        username = self.cleaned_data['username']
        username = username.strip().lower()
        if username != self.cleaned_data['username']:
            try:
                Users = Users.object.get(username = username)
            except Users.DoesNotExist:
                return username
            raise forms.ValidationError(f"Username {username} is already in use.")
        else:
            return username
    def save(self, commit = True):
        users = super(UsersUpdateForm, self).save(commit=False)
        users.username = self.cleaned_data['username']
        users.email = self.cleaned_data['email']
        users.phone = self.cleaned_data['phone']
        users.social_media_link = self.cleaned_data['social_media_link']
        users.social_media_choice = self.cleaned_data['social_media_choice']
        if commit:
            users.save()
        return users