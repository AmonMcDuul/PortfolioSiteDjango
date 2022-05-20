from django.forms import ModelForm
from .models import PostComment

class CommentForm(ModelForm):
    class Meta:
        model = PostComment
        fields = ['name', 'body']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})