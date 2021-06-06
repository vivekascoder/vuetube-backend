from app.models import Category, Link
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'
  
  def create(self, validated_data):
    return Category.objects.create(**validated_data)
  
  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.save()
    return instance

class LinkSerializer(serializers.ModelSerializer):
  class Meta:
    model = Link
    fields = '__all__'

  def create(self, validated_data):
    return Link.objects.create(**validated_data)
  
  def update(self, instance, validated_data):
    instance.link = validated_data.get('link', instance.link)
    instance.description = validated_data.get('description', instance.description)
    instance.category = validated_data.get('category', instance.category)
    instance.save()
    return instance