from django.db import models


# Create your models here.
class RoastMe(models.Model):
    Name = models.CharField(max_length = 150)
    Content = models.TextField(null = False, blank = False)
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.Name
