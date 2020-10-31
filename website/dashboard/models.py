from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('dashboard:post', kwargs={'post_id': self.id})