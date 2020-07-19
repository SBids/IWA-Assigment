from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    blog_type = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='blog_author')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


