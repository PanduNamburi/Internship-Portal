from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Applicant

# Customize admin site
admin.site.site_header = "Internship Portal Administration"
admin.site.site_title = "Internship Portal Admin"
admin.site.index_title = "Welcome to Internship Portal Administration"

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'position_type', 'department', 'status', 'applied_date')
    list_filter = ('status', 'position_type', 'department', 'applied_date')
    search_fields = ('first_name', 'last_name', 'email', 'department')
    readonly_fields = ('applied_date',)
    date_hierarchy = 'applied_date'
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'date_of_birth')
        }),
        ('Application Details', {
            'fields': ('position_type', 'department', 'start_date', 'end_date')
        }),
        ('Education & Experience', {
            'fields': ('current_education', 'institution', 'graduation_year', 'relevant_experience')
        }),
        ('Motivation & Skills', {
            'fields': ('motivation', 'skills')
        }),
        ('Additional Information', {
            'fields': ('resume', 'cover_letter'),
            'classes': ('collapse',)
        }),
        ('Application Status', {
            'fields': ('status', 'applied_date', 'admin_notes')
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related()
