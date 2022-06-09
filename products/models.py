from unittest.util import _MAX_LENGTH
from django.db import models


class Product(models.Model):
    name = models.Charfield(max_length=100)
    price = models.Integerfield(default=0) # cents

    def __str__(self):
        return self.name

