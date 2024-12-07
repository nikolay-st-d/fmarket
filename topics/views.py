from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from fMarket.mixins import StuffOnlyPermissionMixin
from topics.forms import TopicCreateForm
from topics.models import Topic


class TopicsListView(views.ListView):
    model = Topic
    template_name = 'topics/topics.html'
    ordering = ('list_order', 'title')


class TopicDetailsView(views.DetailView):
    model = Topic
    template_name = 'topics/topic-details.html'


class TopicCreateView(LoginRequiredMixin, StuffOnlyPermissionMixin, views.CreateView):
    model = Topic
    form_class = TopicCreateForm
    template_name = 'topics/topic-create.html'
    success_url = reverse_lazy('topics')

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class TopicUpdateView(LoginRequiredMixin, StuffOnlyPermissionMixin, views.UpdateView):
    model = Topic
    form_class = TopicCreateForm
    template_name = 'topics/topic-update.html'
    success_url = reverse_lazy('topics')

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class TopicDeleteView(LoginRequiredMixin, StuffOnlyPermissionMixin, views.DeleteView):
    model = Topic
    template_name = 'topics/topic-delete.html'
    success_url = reverse_lazy('topics')
