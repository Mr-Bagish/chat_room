from django.db import models

# Create your models here.
class room(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class message(models.Model):
    value = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=50)
    room = models.CharField(max_length=50)

    def __str__(self):
        return self.value
