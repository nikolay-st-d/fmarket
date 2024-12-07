from django.contrib.auth import get_user_model
from accounts.models import Profile
from products.models import Product
from reviews.models import Review
from sellers.models import Seller

UserModel = get_user_model()


def seller_pk(request):
    if request.user.is_authenticated:
        try:
            seller = Seller.objects.get(account=request.user)
            return {'seller_pk': seller.pk}
        except Seller.DoesNotExist:
            pass
    return {'seller_pk': None}


def seller_approved(request):
    if request.user.is_authenticated:
        try:
            Seller.objects.get(account=request.user, approved=True)
            return {'seller_approved': True}
        except Seller.DoesNotExist:
            pass
    return {'seller_approved': False}


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


def site_stats(request):
    num_users = UserModel.objects.all().count()
    num_sellers = Seller.objects.all().count()
    num_products = Product.objects.all().count()
    data = {
        'number_of_users': num_users,
        'number_of_sellers': num_sellers,
        'number_of_products': num_products,
    }
    return data


def user_wrote_review(request):
    if not request.user.is_authenticated or not hasattr(request, 'product'):
        return {'user_wrote_review': False}
    product = request.product
    user_review_exists = Review.objects.filter(product=product, owner=request.user).exists()
    return {'user_wrote_review': user_review_exists}



