from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse  
from datetime import datetime  
from .models import Title, Content
from .forms import TitleForm, ContentForm


def home(request):
    notes = Title.objects.all()
    return render(request, 'notes/home.html', {'notes': notes, 'today': datetime.today()})


def add_note(request):
    if request.method == 'POST':
        title_form = TitleForm(request.POST)
        content_form = ContentForm(request.POST)
        if title_form.is_valid() and content_form.is_valid():
            title = title_form.save()
            content = content_form.save(commit=False)
            content.title = title
            content.save()
            return redirect('notes:home')
    else:
        title_form = TitleForm()
        content_form = ContentForm()
    return render(request, 'notes/add_note.html', {'title_form': title_form, 'content_form': content_form})

def note_detail(request, id):
    title = get_object_or_404(Title, pk=id)
    return render(request, 'notes/note_detail.html', {'title': title})

# Create your views here.
