from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','name','flag')
    list_filter = ('flag',)
    search_fields = ('name',)
    list_editable = ('flag',)