from django.contrib import admin
from bot.models import Subject, Document, Book, PQP

# Register your models here.
from import_export.admin import ImportExportModelAdmin
class BookAdmin(ImportExportModelAdmin):
    list_display = ['Dept', 'Title', 'Author', 'Location']

admin.site.register(Subject)
admin.site.register(Document)
admin.site.register(Book,BookAdmin)
admin.site.register(PQP)