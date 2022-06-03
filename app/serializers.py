from rest_framework import serializers
from . import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ('id', 'name', 'author_name', 'price', 'year')