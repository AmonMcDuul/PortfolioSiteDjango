from django.contrib import admin

# Register your models here.
from .models import PostComment

admin.site.register(PostComment)