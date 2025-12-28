from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    # Extending the UserCreationForm is used to get the default User model fields for creating a user.
    class Meta:
        model = User
        fields = ('email','username','first_name','last_name','password1','password2')


