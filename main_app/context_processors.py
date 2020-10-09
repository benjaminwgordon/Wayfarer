from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def auth_context_processor(request):
    return {
        'register_form': UserCreationForm(),
        'login_form': AuthenticationForm()
    }