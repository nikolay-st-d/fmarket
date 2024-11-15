from django.views import generic as views


class HomePageView(views.TemplateView):
    template_name = 'base.html'
