from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_author = models.CharField(max_length=50, default="Anonymous")
    blog_title = models.CharField(max_length=50, default="")
    timeStamp = models.DateTimeField(auto_now=True)
    blog_content = models.TextField()
    smug = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.blog_title + " by- " + self.blog_author

    def createSmug(self):
        self.smug = str(self.blog_title)[0:10] + str(self.blog_id) + "by" + str(self.blog_author)[0:2]


class BlogComment(models.Model):
    Sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:10] + " by " + self.user.username
