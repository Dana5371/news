from django.db import models

from account.models import User


class Category(models.Model):
    slug = models.SlugField(primary_key=True, max_length=200)
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='categories', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} --> {self.name}'
        else:
            return self.name




class Post(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    OPTIONS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )   
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='places')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='places')
    created = models.DateTimeField()
    status = models.CharField(max_length=10, choices=OPTIONS, default='draft')
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    likes = models.ManyToManyField(User, related_name='likes')
    objects = models.Manager()
    newmanager = NewManager()


    def __str__(self):
        return self.title




class Image(models.Model):
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        if self.image:
            return self.image.url
        return ''