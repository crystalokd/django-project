from rest_framework import serializers
from appi.models import News



class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
    model = News