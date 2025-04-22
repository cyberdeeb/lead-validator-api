from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_bulma.layout import Layout, Field, Submit, Column, Div

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email Address', required=True)

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Crispy form helper for styling and layout
        self.helper = FormHelper()
        self.helper.form_id = 'signup_from'
        self.helper.form_class = 'mt-5'
        #self.helper.form_horizontal = True
        #self.helper.form_show_labels = False

        self.fields['username'].help_text = "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        self.fields['password1'].help_text = "Enter a strong password with at least 8 characters."
        self.fields['password2'].help_text = "Enter the same password as above, for verification."
        self.fields['email'].help_text = "Enter a valid email address."
        

        self.helper.layout = Layout(
            Field('username', placeholder='Username', css_class=''),
            Field('email', placeholder='Email', css_class=''),
            Field('password1', placeholder='Enter Password'),
            Field('password2', placeholder='Re-enter Password'),
            Column(Submit('submit', 'Sign Up', css_class='button is-primary'), css_class='has-text-centered')
        )

class CustomUserAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Crispy form helper for styling and layout
        self.helper = FormHelper()
        self.helper.form_id = 'login_form'
        self.helper.form_class = 'mt-3'

        self.helper.layout = Layout(
            Field('username', placeholder='Username'),
            Field('password', placeholder='Password'),
            Column(Submit('submit', 'Login', css_class='button is-primary'), css_class='has-text-centered')
        )

class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

     # Crispy form helper for styling and layout
        self.helper = FormHelper()
        self.helper.form_id = 'password_reset_form'
        self.helper.form_class = 'mt-5'
        self.helper.form_horizontal = True

        self.helper.layout = Layout(
            Field('email', placeholder='Email', css_class='mt-3'),
            Div(Submit('submit', 'Submit', css_class='button is-primary mt-3'), css_class='is-flex is-justify-content-center')
        )

