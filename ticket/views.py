from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .utils import generate_qr_code
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_school = request.POST.get('school')
        user_languages = request.POST.get('languages')
        user_year = request.POST.get('year')
        user_team = request.POST.get('team')
        user_course = request.POST.get('course')

        ticket, created = Ticket.objects.get_or_create(
            name = user_name,
            email = user_email,
            team = user_team,
            course = user_course,
            school = user_school,
            language = user_languages,
            year = user_year
        )

        if created:
            return redirect(reverse('ticket', kwargs={'ticket_id': ticket.id}))
        else:
            return redirect(reverse('ticket', kwargs={'ticket_id': ticket.id}))
    
    return render(request, 'main.html')

def generate_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    generate_qr_code(ticket_id)
    return render(request, 'ticket.html', {'ticket': ticket})