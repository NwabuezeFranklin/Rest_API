from . models import Article, Profile
from rest_framework import serializers

'''
class ArticleSerializer(serializers.Serializer):
    topic = serializers.CharField(max_length=100)
    author= serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()
    
    def create(self, obj):
        return Article.objects.create(obj)
    
    def update(self, instance, obj):
        instance.topic = obj.get('topic', instance.topic)
        instance.author = obj.get('topic', instance.author)
        instance.email = obj.get('topic', instance.email)
        instance.date = obj.get('topic', instance.date)
        instance.save()
        return instance
'''


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['occupation']
        
    