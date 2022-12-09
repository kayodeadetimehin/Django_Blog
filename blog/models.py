from django.db import models

# Create your models here.

STATUS = (
    (0,'Draft'),
    (1, 'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=200)
    authur = models.CharField(max_length=100)
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices= STATUS, default=0)


    class Meta():
        ordering =['-date_created']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post= models.ForeignKey('blog.post',on_delete=models.CASCADE,related_name='comment')
    authur = models.CharField(max_length=100)
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField() 