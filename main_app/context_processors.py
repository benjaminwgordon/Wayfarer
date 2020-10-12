from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm

def auth_context_processor(request):
    return {
        'register_form': NewUserForm(),
        'login_form': AuthenticationForm()
    }