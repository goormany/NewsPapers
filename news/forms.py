from django.forms import ModelForm, BooleanField
from .models import *

class NewsForm(ModelForm):
    check_box = BooleanField(label='Вы подтверждаете свои действия?')

    class Meta:
        model = Post
        fields = [
            'PostAuthor',
            'title',
            'positions',
            'category_id',
            'previewName',
            'text',
            'check_box'
        ]