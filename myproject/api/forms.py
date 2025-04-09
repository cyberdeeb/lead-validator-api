from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_bulma.layout import Layout, Field, Submit, Column

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Crispy form helper for styling and layout
        self.helper = FormHelper()
        self.helper.form_id = 'signup_from'
        self.helper.form_class = 'mt-5'
        #self.helper.form_horizontal = True
        #self.helper.form_show_labels = False
        

        self.helper.layout = Layout(
            Field('username', placeholder='Username', css_class=''),
            Field('password1', placeholder='Enter Password'),
            Field('password2', placeholder='Re-enter Password'),
            Column(Submit('submit', 'Sign Up', css_class='is-primary'), css_class='has-text-centered')
        )