from sellers.models import Seller


def seller_pk(request):
    if request.user.is_authenticated:
        try:
            seller = Seller.objects.get(account=request.user)
            return {'seller_pk': seller.pk}
        except Seller.DoesNotExist:
            pass
    return {'seller_pk': None}