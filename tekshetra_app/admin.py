from django.contrib import admin
from .models import Professional

@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'domain', 'experience','expertise_tools' ,'created_at')
    search_fields = ('name', 'designation', 'domain', 'expertise_tools')
