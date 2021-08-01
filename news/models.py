from django.db import  models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core.cache import cache
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment

class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    authorRaitng = models.SmallIntegerField(default=0)

    def update_rating(self):
        post_rating = self.post_set.aggregate(postRating=Sum('rating'))
        postRat = 0
        postRat += post_rating.get('postRating')

        comment_rating = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        comRat = 0
        comRat += comment_rating.get('commentRating')

        self.authorRating = postRat * 3 + comRat
        self.save()

    def __str__(self):
        return str(self.authorUser)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'



class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User, blank=True, null=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name

class Post(models.Model):
    PostAuthor = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор поста')

    PostNews = 'PN'
    PostArticle = 'PA'

    # «статья» или «новость»
    POSITIONS = [
        (PostArticle, 'Статья'),
        (PostNews, 'Новость'),
    ]

    postCategory = models.ManyToManyField(Category, verbose_name='Категория поста',  through='PostCategory')
    title = models.CharField(max_length=50, verbose_name='Название')
    positions = models.CharField(max_length=2, choices=POSITIONS, default=PostArticle, verbose_name='Тип поста')
    category_id = models.ForeignKey(Category, verbose_name='Категория', null=True, on_delete=models.CASCADE, related_name='category_id')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    data_update = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True, default='/photos/def/1.jpg/')
    previewName = models.CharField(max_length=128, verbose_name='Превью поста')
    # text = models.TextField(verbose_name='Текст поста')
    text = RichTextField(blank=True, null=True, verbose_name='Текст поста')
    rating = models.SmallIntegerField(default=0, verbose_name='Рейтинг')
    public = models.BooleanField(default=True, verbose_name='Опубликовано')
    comments = GenericRelation(Comment)

    def like(self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating -=1
        self.save()

    def preview(self):
        return self.text[0:124] + '...'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return f'/news/{self.pk}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f"new-{self.pk}")


class PostCategory(models.Model):
    pcPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    pcCategory = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пост категория'
        verbose_name_plural = 'Пост категории'

    def __str__(self):
        return f'{str(self.pcPost)}, имеет категорию {str(self.pcCategory)}'


# class Comment(models.Model):

#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     commentText = models.TextField(max_length=60)
#     dataCreating = models.DateTimeField(auto_now_add=True)
#     rating = models.SmallIntegerField(default=0)
#
#     def like(self):
#         self.rating +=1
#         self.save()
#
#     def dislike(self):
#         self.rating -=1
#         self.save()
#
#     class Meta:
#         verbose_name = 'Коммент'
#         verbose_name_plural = 'Комменты'
#
#     def __str__(self):
#         return f'{self.user}: {self.post}: {self.commentText}, {self.pk}'