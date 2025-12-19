from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'clinic_name', 'phone', 'created_at')
    list_filter = ('clinic_name', 'created_at')
    search_fields = ('last_name', 'first_name', 'phone', 'email', 'clinic_name')
    fieldsets = (
        ('Основная информация', {
            'fields': ('last_name', 'first_name', 'middle_name')
        }),
        ('Контакты', {
            'fields': ('phone', 'email')
        }),
        ('Клиника', {
            'fields': ('clinic_name', 'clinic_address', 'specialization')
        }),
        ('Дополнительно', {
            'fields': ('notes', 'created_by')
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Если объект создается впервые
            obj.created_by = request.user
        super().save_model(request, obj, form, change)