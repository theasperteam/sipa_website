from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Contact_Form_Events, Book_Appointment_Events)
class ViewAdmin(ImportExportModelAdmin):
    pass
