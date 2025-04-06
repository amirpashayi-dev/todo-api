from django.contrib import admin
from tasks.models import Tasks, Category

admin.site.register(Tasks)
admin.site.register(Category)