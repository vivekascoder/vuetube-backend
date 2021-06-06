from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=200)
  time = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Link(models.Model):
  link = models.URLField(max_length=200)
  description = models.CharField(max_length=200)
  time = models.DateTimeField(auto_now_add=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.link


