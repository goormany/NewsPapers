from django.forms import ModelForm, BooleanField
from .models import *

class NewsForm(ModelForm):
    confirm_box = BooleanField(label='Вы подтверждаете свои действия?')

    class Meta:
        model = Post
        fields = [
            'PostAuthor',
            'title',
            'positions',
            'previewName',
            'text',
        ]