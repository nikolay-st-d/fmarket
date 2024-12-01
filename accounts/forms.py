from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile
from fMarket.mixins import PlaceholderMixin

UserModel = get_user_model()


class AccountUserCreationForm(PlaceholderMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            user=user,
        )
        if commit:
            profile.save()
        return user
