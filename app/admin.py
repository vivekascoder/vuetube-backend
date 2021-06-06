from django.contrib import admin
from app.models import Category, Link

admin.site.register((Category, Link))