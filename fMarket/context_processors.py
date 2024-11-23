from accounts.models import Profile
from sellers.models import Seller


def seller_pk(request):
    if request.user.is_authenticated:
        try:
            seller = Seller.objects.get(account=request.user)
            return {'seller_pk': seller.pk}
        except Seller.DoesNotExist:
            pass
    return {'seller_pk': None}


def account_complete(request):
    if request.user.is_authenticated:
        user = Profile.objects.get(pk=request.user)
        try:
            if (user.first_name is None or user.last_name is None
                    or user.phone_number is None or user.country is None):
                return {'account_complete': False}
        except user.DoesNotExist:
            pass
    return {'account_complete': True}

