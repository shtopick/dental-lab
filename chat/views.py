from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Doctor

# Главная страница
def home_view(request):
    context = {
        'doctor_count': Doctor.objects.count(),
    }
    return render(request, 'home.html', context)

# Список врачей
class DoctorListView(LoginRequiredMixin, ListView):
    model = Doctor
    template_name = 'chat/doctor_list.html'
    context_object_name = 'doctors'
    paginate_by = 10
    
    def get_queryset(self):
        return Doctor.objects.all().order_by('last_name', 'first_name')