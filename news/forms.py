from django import forms
from django.forms import ModelForm, BooleanField, ModelChoiceField
from .models import *

class NewsForm(ModelForm):
    public = BooleanField(label='Опубликовано?', initial=True, required=False)
    category_id = ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Выберите категорию')
    PostAuthor = ModelChoiceField(queryset=Author.objects.all(), label='Автор', empty_label='Выберите автора')

    class Meta:
        model = Post
        fields = [
            'PostAuthor',
            'title',
            'positions',
            'category_id',
            'previewName',
            'text',
            'photo',
            'public'
        ]



        # model = Post
        # fields = [
        #     'PostAuthor',
        #     'title',
        #     'positions',
        #     'category_id',
        #     'previewName',
        #     'text',
        #     'photo',
        #     'public',
        # ]

        # from django.forms import ModelForm, BooleanField
        # from .models import *
        # from django import forms
        #
        # class NewsForm(ModelForm):
        #     check_box = BooleanField(label='Вы подтверждаете свои действия?')
        #     # title = forms.CharField(max_length=50, label='Название поста')
        #     # text = forms.CharField(label='Текст поста')
        #     #  public1 = forms.BooleanField(label='Опубликовано?')
        #     # category = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all())
        #
        # class Meta:
        #     model = Post
        #     fields = [
        #         'PostAuthor',
        #         'title',
        #         'positions',
        #         'category_id',
        #         'previewName',
        #         'text',
        #         'photo',
        #         'check_box',
        #     ]