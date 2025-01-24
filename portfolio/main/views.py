from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Skill, Project, Profile
from .forms import ContactForm

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    profile = Profile.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            return redirect('/')

    else:
        form = ContactForm()

    context = {
        'skills': skills,
        'projects': projects,
        'profile': profile,
        'form': form
    }

    return render(request, 'main/home.html', context)

