from rest_framework import serializers
from snippets.models import Snippets , LANGUAGE_CHOICES,STYLE_CHOICES
from .models import Users

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippets
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style','owner']
    
    def create(self, validated_data):
        return Snippets.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippets.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
    
class MyUser(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fiels = ["name","email","password"]