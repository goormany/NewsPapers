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

        widgets = {
            'PostAuthor': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'positions': forms.Select(attrs={'class': 'form-control'}),
            'category_id': forms.Select(attrs={'class': 'form-control'}),
            'previewName': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = [
#             'commentText',
#         ]
#
#         widgets = {
#             'commentText': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'rows': 5,
#                 'placeholder': 'Введите комментарий...',
#             })
#         }
