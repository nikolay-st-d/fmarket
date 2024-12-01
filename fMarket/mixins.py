from django.forms import Select, FileInput


class PlaceholderMixin:

    def set_placeholder(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (Select, FileInput)):
                continue
            placeholder = field.label or field.name.replace('_', ' ').capitalize()
            if field.help_text:
                placeholder = field.help_text
                field.help_text = ''
            field.widget.attrs['placeholder'] = placeholder

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_placeholder()
