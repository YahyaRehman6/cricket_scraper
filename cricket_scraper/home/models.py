from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    title_image = models.CharField(max_length=1055)
    created_at = models.DateTimeField(auto_now_add=True)