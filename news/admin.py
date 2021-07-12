from django import forms
from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Действие в админ панели 'Снять пост с публикации'
def public_off(modeladmin, request, queryset):
    queryset.update(public=False)


public_off.short_description = 'Снять пост с публикации'


# Действие в админ панели 'Опубликовать пост'
def public_on(modeladmin, request, queryset):
    queryset.update(public=True)


public_on.short_description = 'Опубликовать пост'


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())  # Новый редактор текста в админке

    class Meta:
        model = Post
        fields = '__all__'


# Вид админ панели постов
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'title', 'positions', 'category_id', 'data', 'data_update', 'rating', "public")
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'id')
    list_editable = ('public',)
    list_filter = ('positions', 'data', 'data_update', 'public')
    actions = [public_off, public_on]


# Вид админ панели категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    list_display_links = ('id', 'category_name',)
    search_fields = ('title',)


# Вид админ панели комментарии
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'post', 'commentText', 'rating',)


# Регистрация моделей в админку
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Comment, CommentAdmin)
