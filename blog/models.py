from django.db import models
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    cover = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, editable=False)
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}. {} | {}".format(self.id, self.title, self.category)

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()