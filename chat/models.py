from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    # Основная информация
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=100, blank=True, verbose_name="Отчество")
    
    # Контакты
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(blank=True, verbose_name="Email")
    
    # Клиника/место работы
    clinic_name = models.CharField(max_length=200, verbose_name="Название клиники")
    clinic_address = models.TextField(blank=True, verbose_name="Адрес клиники")
    
    # Дополнительно
    specialization = models.CharField(max_length=200, blank=True, verbose_name="Специализация")
    notes = models.TextField(blank=True, verbose_name="Заметки")
    
    # Даты
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Кем создан")
    
    # Методы
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}".strip()
    
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}".strip()
    
    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"
        ordering = ['last_name', 'first_name']