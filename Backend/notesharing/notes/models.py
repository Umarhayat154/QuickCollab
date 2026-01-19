from django.db import models
from users.models import User

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    content= models.TextField()
    is_public=models.BooleanField(default=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        unique_together=('title','author')

    
    def __str__(self):
        return self.title
    