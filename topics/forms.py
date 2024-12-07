from django.forms import ModelForm
from fMarket.mixins import PlaceholderMixin
from topics.models import Topic


class BaseTopicForm(PlaceholderMixin, ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
        exclude = ('updated_by',)


class TopicCreateForm(BaseTopicForm):
    pass


class TopicUpdateForm(BaseTopicForm):
    pass
