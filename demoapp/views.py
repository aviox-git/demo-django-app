from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Person
from .forms import PersonForm
from datetime import datetime

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'demoapp/login.html')

@login_required
def dashboard(request):
    persons = Person.objects.all()
    return render(request, 'demoapp/index.html', {'persons': persons})

@login_required
def save_person(request, pk=None):
    if pk:
        person = get_object_or_404(Person, pk=pk)
    else:
        person = None

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save()
            html = render_to_string('demoapp/person_row.html', {'person': person})
            return JsonResponse({'success': True, 'html': html})
        else:
            return JsonResponse({'success': False, 'errors': form.errors.as_json()})
    else:
        form = PersonForm(instance=person)
        html = render_to_string('demoapp/modals.html', {
            'form': form, 
            'pk': pk,
        })
        return JsonResponse({'html': html})

@login_required
def delete_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person.delete()
        return JsonResponse({'success': True, 'pk': pk})
    return JsonResponse({
        'html': render_to_string('demoapp/delete_modal.html', {'person': person})
    })

@login_required
def filter_persons(request):
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    persons = Person.objects.all()
    
    if from_date:
        persons = persons.filter(created_at__date__gte=from_date)
    if to_date:
        persons = persons.filter(created_at__date__lte=to_date)
    
    rows = []
    for person in persons:
        row_html = render_to_string('demoapp/person_row.html', {'person': person})
        rows.append(row_html)
    return JsonResponse({'html': rows})
