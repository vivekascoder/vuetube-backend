from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Category, Link
from app.serializers import CategorySerializer, LinkSerializer

from django.shortcuts import Http404


class CategoryList(APIView):
  def get(self, request, *args, **kwargs):
    categories = Category.objects.all()
    serializer = CategorySerializer(instance=categories, many=True)
    return Response(serializer.data)
  
  def post(self, request, *args, **kwargs):
    print(f'Request.Data: {request.data}')
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    else:
      return Response(serializer.errors, status=400)


class CategoryDetail(APIView):
  def get_object(self, pk):
    try:
      category = Category.objects.get(pk=pk)
      return category
    except Category.DoesNotExist:
      raise Http404

  def get(self, request, *args, **kwargs):
    """ Return detail of a specific category. """
    print("Getting Data")
    category = self.get_object(kwargs.get('pk'))
    serializer = CategorySerializer(category)
    return Response(serializer.data)
  
  def put(self, request, *args, **kwargs):
    category = self.get_object(kwargs.get('pk'))
    serializer = CategorySerializer(instance=category, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=200)
    else:
      return Response(serializer.errors, status=400)

  def delete(self, request, *args, **kwargs):
    category = self.get_object(kwargs.get('pk'))
    category.delete()
    return Response(status=204)


class CategoryLinks(APIView):
  """ Return links corresponds to a category's pk """
  
  endpoint = "category/<int:pk>/links"
  def get(self, request, *args, **kwargs):
    links = Link.objects.filter(category__pk=kwargs.get('pk'))
    serializer = LinkSerializer(links, many=True)
    return Response(serializer.data)
    



class LinkList(APIView):
  def get(self, request, *args, **kwargs):
    links = Link.objects.all()
    serializer = LinkSerializer(links, many=True)
    return Response(serializer.data)

  def post(self, request, *args, **kwargs):
    serializer = LinkSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    else:
      return Response(serializer.errors, status=400)

class LinkDetail(APIView):
  def get_object(self, pk):
    try:
      link = Link.objects.get(pk=pk)
      return link
    except Link.DoesNotExist:
      raise Http404

  def get(self, request, *args, **kwargs):
    """ Return detail of a specific category. """
    link = self.get_object(kwargs.get('pk'))
    serializer = LinkSerializer(link)
    return Response(serializer.data)
  
  def put(self, request, *args, **kwargs):
    link = self.get_object(kwargs.get('pk'))
    serializer = LinkSerializer(instance=link, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=200)
    else:
      return Response(serializer.errors, status=400)

  def delete(self, request, *args, **kwargs):
    link = self.get_object(kwargs.get('pk'))
    link.delete()
    return Response(status=204)
