from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from sellers.models import Seller


@receiver(pre_save, sender=Seller)
def send_approval_email(sender, instance, **kwargs):
    if instance.pk:
        previous_instance = sender.objects.get(pk=instance.pk)

        if not previous_instance.approved and instance.approved:
            subject = "Your fMarket Seller Account Has Been Approved"
            message = (f"Hello {instance.name},\n\nYour Seller account has been approved. "
                       f"You can now start adding products on our platform.\n\nThank you!")
            from_email = "admin@fmarket.com"
            to_email = instance.account.email
            recipient_list = [to_email]

            send_mail(subject, message, from_email, recipient_list)
