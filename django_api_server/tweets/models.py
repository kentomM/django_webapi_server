from django.db import models
from users.models import CustomUser


class Tweet(models.Model):
    body = models.CharField('内容', max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}".format(self.body)
