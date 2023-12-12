from django.contrib import admin
from .models import BookModal

# Register your models here.
@admin.register(BookModal)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
