from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name
