from django_filters import FilterSet
from .models import Post

class newsFilter(FilterSet):

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'data': ['gte'],
            'PostAuthor': ['exact']
        }