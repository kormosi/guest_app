from django.db import models

class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    base64_image = models.TextField()

    def __str__(self):
        return str(self.first_name + " " + self.last_name)
