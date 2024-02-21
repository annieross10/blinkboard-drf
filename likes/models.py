from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Like by {self.user.username} on {self.post}"



