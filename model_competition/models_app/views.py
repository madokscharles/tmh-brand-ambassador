# models_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, ProfileUpdateForm, EntryForm
from .models import Profile, Competition, Entry

# Create your views here.
# Register view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user=user)
            profile.save()
            login(request, user)
            messages.success(request, 'Your account has been created! You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})

# Home view
def home(request):
    return render(request, 'home.html')

# Competition list view
def competition_list(request):
    competitions = Competition.objects.all()
    return render(request, 'competition_list.html', {'competitions': competitions})

# Competition detail view
def competition_detail(request, competition_id):
    competition = get_object_or_404(Competition, id=competition_id)
    entries = Entry.objects.filter(competition=competition)
    return render(request, 'competition_detail.html', {'competition': competition, 'entries': entries})

# Create entry view
@login_required
def create_entry(request, competition_id):
    competition = get_object_or_404(Competition, id=competition_id)
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.profile = request.user.profile
            entry.competition = competition
            entry.save()
            messages.success(request, 'Your entry has been submitted!')
            return redirect('competition_detail', competition_id=competition.id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = EntryForm()

    return render(request, 'create_entry.html', {'form': form, 'competition': competition})

# Update profile view
@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile_update')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'profile_update.html', {'form': form})