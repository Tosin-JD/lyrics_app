from django import forms 
from django.core.exceptions import ValidationError

from django.contrib.auth import get_user_model


User = get_user_model()

class UserForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control m-b1 bg-light'
        self.fields['email'].widget.attrs['class'] = 'form-control mb-1 bg-light'
        self.fields['first_name'].widget.attrs['class'] = 'form-control mb-1 bg-light'
        self.fields['last_name'].widget.attrs['class'] = 'form-control mb-1 bg-light'
        self.fields['password1'].widget.attrs['class'] = 'form-control mb-1 bg-light'
        self.fields['password2'].widget.attrs['class'] = 'form-control mb-1 bg-light'
        
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
    
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


        
        


