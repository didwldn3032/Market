from django.contrib import admin
from .models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'created_at',
    )
    search_fields = (
        'title',
    )
# Register your models here.
