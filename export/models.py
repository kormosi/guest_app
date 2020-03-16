from django.db import models

class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    base64_image = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'First Name: {self.first_name} Last Name: {self.last_name}'
