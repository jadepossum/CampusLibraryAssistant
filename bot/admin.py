from django.contrib import admin
from bot.models import Subject, Document, Book, PQP , PPT

# Register your models here.
from import_export.admin import ImportExportModelAdmin
class BookAdmin(ImportExportModelAdmin):
    list_display = ['Dept', 'Title', 'Author', 'Location']

class PQPAdmin(ImportExportModelAdmin):
    lsit_display = ['Regulation','Semester','Branch','Subject','Year','Link']

admin.site.register(Subject)
admin.site.register(Document)
admin.site.register(Book,BookAdmin)
admin.site.register(PQP,PQPAdmin)
admin.site.register(PPT,PQPAdmin)