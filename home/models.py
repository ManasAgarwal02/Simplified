from django.db import models


# Create your models here.

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=60, default="")
    phone = models.CharField(max_length=13, default="")
    desc = models.TextField()

    def __str__(self):
        return self.name + " - " + self.email + " - " + str(self.timestamp)[0:-12]
