from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'category_id', 'text', )

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', )