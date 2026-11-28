from django.contrib import admin
from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_indexed", "uploaded_at")
    list_filter = ("is_indexed",)
