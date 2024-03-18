from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .utils import generate_qr_code
from django.urls import reverse
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail

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

        # Generate QR code URL
        qr_code_url = request.build_absolute_uri(reverse('ticket', kwargs={'ticket_id': ticket.id}))

        email_content = render_to_string('registration_email.html', { 
            'name' : ticket.name,
            'email': ticket.email,
            'team' : ticket.team,
            "course" : ticket.course,
            "school" : ticket.school,
            "language" : ticket.language,
            "year" :ticket.year,
            'qr_code_url': qr_code_url,
            'ref_code': ticket.ref_code
        })

        send_mail(
            'Registration Details',
            email_content,
            settings.DEFAULT_FROM_EMAIL,
            [ticket.email],
            fail_silently=False,
        )

        if created:
            return redirect(reverse('ticket', kwargs={'ticket_id': ticket.id}))
        else:
            return redirect(reverse('homepage'))
    
    return render(request, 'main.html')

def generate_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    generate_qr_code(ticket_id)
    return render(request, 'ticket.html', {'ticket': ticket})