from django.contrib import admin
from django.db.models import TextField
from django_markdown.widgets import AdminMarkdownWidget
from django_markdown.admin import MarkdownModelAdmin
from . import models


class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}


admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag)
