from django.core.mail import send_mail
from django.urls import reverse
from django.views import generic as views
from products.models import Product
from web.forms import ContactForm


class HomePageView(views.ListView):
    HOME_PAGE_LATEST_PRODUCTS_NUMBER = 4
    model = Product
    template_name = 'index.html'

    def get_queryset(self):
        products = Product.objects.all().order_by('-views_count', '-id')[:self.HOME_PAGE_LATEST_PRODUCTS_NUMBER]
        return products


class SuccessView(views.TemplateView):
    template_name = "contact-success.html"


class ContactView(views.FormView):
    form_class = ContactForm
    template_name = "contact.html"

    def get_success_url(self):
        return reverse("contact-success")

    def form_valid(self, form):
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        full_message = f"""
            About: {subject}
            From: {name} <{email}>
            ________________________

            {message}
            """
        send_mail(
            subject="fMarket message",
            message=full_message,
            from_email=email,
            recipient_list=['contact@ndimitrov.com'],
        )
        return super(ContactView, self).form_valid(form)
