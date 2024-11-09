from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Animal, Health, Breeding
from .forms import (
    AnimalForm,
    HealthForm,
    BreedingForm,
    CustomUserCreationForm
)

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return super().form_invalid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return self.success_url

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! Welcome to the Livestock Management System.")
            return redirect('dashboard')
        messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Here you would typically:
        # 1. Generate a password reset token
        # 2. Send an email with the reset link
        # 3. Save the token in the database
        messages.success(request, "If an account exists with this email, you will receive password reset instructions.")
        return redirect('login')
    return render(request, 'auth/password_reset.html')

# Dashboard Views
@login_required
def dashboard(request):
    total_animals = Animal.objects.count()
    recent_health_records = Health.objects.order_by('-date')[:5]
    active_breedings = Breeding.objects.filter(success=False)
    
    context = {
        'total_animals': total_animals,
        'recent_health_records': recent_health_records,
        'active_breedings': active_breedings,
    }
    return render(request, 'dashboard/index.html', context)

# Animal Management Views
@login_required
def animal_list(request):
    animals = Animal.objects.all().order_by('-created_at')  # Assuming you have a created_at field
    return render(request, 'livestock/list.html', {'animals': animals})

@login_required
def animal_add(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.created_by = request.user  # Assuming you have this field
            animal.save()
            messages.success(request, 'Animal added successfully!')
            return redirect('animal_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AnimalForm()
    return render(request, 'livestock/add.html', {'form': form})

@login_required
def animal_edit(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Animal updated successfully!')
            return redirect('animal_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'livestock/edit.html', {'form': form, 'animal': animal})

@login_required
def animal_delete(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    try:
        animal.delete()
        messages.success(request, 'Animal deleted successfully!')
    except Exception as e:
        messages.error(request, 'Unable to delete the animal. It may have related records.')
    return redirect('animal_list')

@login_required
def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    health_records = Health.objects.filter(animal=animal).order_by('-date')
    breeding_records = Breeding.objects.filter(mother=animal) | Breeding.objects.filter(father=animal)
    
    context = {
        'animal': animal,
        'health_records': health_records,
        'breeding_records': breeding_records,
    }
    return render(request, 'livestock/detail.html', context)

# Health Management Views
@login_required
def health_list(request):
    health_records = Health.objects.all().order_by('-date')
    return render(request, 'health/list.html', {'health_records': health_records})

@login_required
def health_add(request):
    if request.method == 'POST':
        form = HealthForm(request.POST)
        if form.is_valid():
            health_record = form.save(commit=False)
            health_record.recorded_by = request.user  # Assuming you have this field
            health_record.save()
            messages.success(request, 'Health record added successfully!')
            return redirect('health_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = HealthForm()
    return render(request, 'health/add.html', {'form': form})

@login_required
def health_edit(request, pk):
    health_record = get_object_or_404(Health, pk=pk)
    if request.method == 'POST':
        form = HealthForm(request.POST, instance=health_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Health record updated successfully!')
            return redirect('health_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = HealthForm(instance=health_record)
    return render(request, 'health/edit.html', {'form': form, 'health_record': health_record})

@login_required
def health_delete(request, pk):
    health_record = get_object_or_404(Health, pk=pk)
    try:
        health_record.delete()
        messages.success(request, 'Health record deleted successfully!')
    except Exception as e:
        messages.error(request, 'Unable to delete the health record.')
    return redirect('health_list')

# Breeding Management Views
@login_required
def breeding_list(request):
    breedings = Breeding.objects.all().order_by('-breeding_date')
    return render(request, 'breeding/list.html', {'breedings': breedings})

@login_required
def breeding_add(request):
    if request.method == 'POST':
        form = BreedingForm(request.POST)
        if form.is_valid():
            breeding = form.save(commit=False)
            breeding.recorded_by = request.user  # Assuming you have this field
            breeding.save()
            messages.success(request, 'Breeding record added successfully!')
            return redirect('breeding_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BreedingForm()
    return render(request, 'breeding/add.html', {'form': form})

@login_required
def breeding_edit(request, pk):
    breeding = get_object_or_404(Breeding, pk=pk)
    if request.method == 'POST':
        form = BreedingForm(request.POST, instance=breeding)
        if form.is_valid():
            form.save()
            messages.success(request, 'Breeding record updated successfully!')
            return redirect('breeding_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BreedingForm(instance=breeding)
    return render(request, 'breeding/edit.html', {'form': form, 'breeding': breeding})

@login_required
def breeding_delete(request, pk):
    breeding = get_object_or_404(Breeding, pk=pk)
    try:
        breeding.delete()
        messages.success(request, 'Breeding record deleted successfully!')
    except Exception as e:
        messages.error(request, 'Unable to delete the breeding record.')
    return redirect('breeding_list')