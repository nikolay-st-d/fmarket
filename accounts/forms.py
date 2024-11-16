from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile

UserModel = get_user_model()


class AccountUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            contry=self.cleaned_data['country'],
            phone_number=self.cleaned_data['phone_number'],
        )

        if commit:
            profile.save()

        return user
