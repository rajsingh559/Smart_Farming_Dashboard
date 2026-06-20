from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, FarmerProfile

class BootstrapFormMixin:
    """Helper mixin to automatically add Bootstrap classes to form fields."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.FileInput):
                field.widget.attrs['class'] = 'form-control-file'
            else:
                field.widget.attrs['class'] = 'form-control'

class UserRegistrationForm(BootstrapFormMixin, UserCreationForm):
    username = forms.CharField(
        required=True,
        error_messages={'required': 'Username is required.'}
    )
    email = forms.EmailField(
        required=True,
        help_text="Required for communication.",
        error_messages={'required': 'Email is required.'}
    )
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES, 
        required=True, 
        initial='farmer',
        widget=forms.Select(attrs={'class': 'form-select'}),
        error_messages={'required': 'Role is required.'}
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        required=True,
        error_messages={'required': 'Password is required.'}
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        required=True,
        error_messages={'required': 'Confirm Password is required.'}
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user

class UserLoginForm(BootstrapFormMixin, AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

class UserEditForm(BootstrapFormMixin, forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class FarmerProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = FarmerProfile
        fields = ('phone_number', 'farm_location', 'farm_size', 'preferred_crop', 'profile_picture')
        widgets = {
            'farm_location': forms.TextInput(attrs={'placeholder': 'e.g. California Central Valley'}),
            'farm_size': forms.NumberInput(attrs={'placeholder': 'e.g. 150.5'}),
            'preferred_crop': forms.TextInput(attrs={'placeholder': 'e.g. Wheat, Corn, Cotton'}),
        }
