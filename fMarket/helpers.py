from sellers.models import Seller


def get_seller_pk_for_user(user):
    try:
        seller = Seller.objects.get(account=user)
        return seller.pk
    except Seller.DoesNotExist:
        return None
