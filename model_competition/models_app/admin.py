# models_app/admin.py

from django.contrib import admin
from .models import Profile, Competition, Entry

# Register your models here.
admin.site.register(Profile)
admin.site.register(Competition)
admin.site.register(Entry)