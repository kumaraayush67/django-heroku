from django.contrib import admin
from .models import Todo, assignee

admin.site.register(Todo)
admin.site.register(assignee)