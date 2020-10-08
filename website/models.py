from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=60)

    def __str__(self):
        return self.name