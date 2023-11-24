from rest_framework import serializers
from news.models import News, User, Category


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    categories = serializers.PrimaryKeyRelatedField(many=True,
                                                    queryset=Category.objects.
                                                    all())
  
    class Meta:
        model = News
        fields = ["id", "title", "content", "author", "created_at",
                  "image", "categories"]
