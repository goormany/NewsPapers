from django.db import  models
from django.contrib.auth.models import User
from django.db.models import Sum

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
    category_subscriber = models.ManyToManyField(User, blank=True, verbose_name='Подписчик категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name

class Post(models.Model):
    PostAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)

    PostNews = 'PN'
    PostArticle = 'PA'

    # «статья» или «новость»
    POSITIONS = [
        (PostArticle, 'Статья'),
        (PostNews, 'Новость'),
    ]

    title = models.CharField(max_length=50)
    positions = models.CharField(max_length=2, choices=POSITIONS, default=PostArticle)
    data = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    previewName = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

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

class PostCategory(models.Model):
    pcPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    pcCategory = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пост категория'
        verbose_name_plural = 'Пост категории'

    def __str__(self):
        return f'{str(self.pcPost)}, имеет категорию {str(self.pcCategory)}'


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    commentText = models.TextField(max_length=60)
    dataCreating = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating -=1
        self.save()

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'

    def __str__(self):
        return f'{self.commentUser}: {self.commentPost}: {self.commentText}, {self.pk}'