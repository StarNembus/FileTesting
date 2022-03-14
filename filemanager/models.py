
from django.db import models
from django.utils import timezone


class Files(models.Model):
    name = models.CharField(max_length=254, null=True)
    file = models.FileField(null=True, max_length=255)
    description = models.CharField(max_length=254, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} {self.file}'
