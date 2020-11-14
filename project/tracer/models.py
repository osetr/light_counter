from django.db import models

class TrackedUsers(models.Model):
    ip = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f'{self.ip} is tracked'