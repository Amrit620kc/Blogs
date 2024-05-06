from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.utils.timezone import now
from tinymce.models import HTMLField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    image= models.ImageField(upload_to='category/')
    def __str__(self):
        return self.name
    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px; heigth:40px; border-radius:20px;"/>'.format(self.image))


class Post(models.Model):
    title = HTMLField()
    body = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    url=models.CharField(max_length=30)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    views=models.IntegerField(default=0)
    Image=models.ImageField(upload_to='post/')

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    timestamp=models.DateTimeField(default=now)
    def __str__(self):
        return self.comment






class Contact(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField()
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.fname+self.lname
    




