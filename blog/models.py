from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(null=True, max_length=20)
    
    def __str__(self):
        return self.caption
    
class Author(models.Model):
    first_name = models.CharField(null=True, max_length=100)
    last_name = models.CharField(null=True, max_length=100)
    email = models.EmailField(null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Post(models.Model):
    title = models.CharField(null=True, max_length=150)
    excerpt = models.CharField(null=True, max_length=200)
    image =  models.CharField(null=True, max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.CharField(null=True, max_length=100)
    content = models.TextField(null=True, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)
        