from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'positions', 'data', 'data_update', 'rating', "public")
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'id')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    list_display_links = ('id', 'category_name',)
    search_fields = ('title',)


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
