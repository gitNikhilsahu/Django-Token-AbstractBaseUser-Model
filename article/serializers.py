from rest_framework import serializers
from article import models


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ('id', 'title', 'slug', 'author', 'updated_on', 'content', 'created_on', 'status')
