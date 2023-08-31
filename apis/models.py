from django.db import models

from authentication.models import Usertable

# Create your models here.
CATEGORY = (
    ("Python", "Python"),
    ("Java", "Java"),
    ("C++", "C++"),
    ("Swift", "Swift")
)

class Content(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=300)
    summary = models.CharField(max_length=60)
    document = models.FileField(upload_to='media/')
    category = models.CharField(choices= CATEGORY,max_length=30, default= "Python")
    author = models.ForeignKey(Usertable, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return self.title