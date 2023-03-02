from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    decription=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    created=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['complete']
    