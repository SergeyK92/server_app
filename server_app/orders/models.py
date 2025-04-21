from django.db import models
from users.models import User


# Create your models here.
class Order(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    order_dt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
