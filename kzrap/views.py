from django.shortcuts import render, get_object_or_404
from .models import Track, Contact, Rapper

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import SubscribeForm


def index(request):
    return render(request, 'kzrap/index.html')


def top5(request):
    top_tracks = Track.objects.all()
    return render(request, 'kzrap/top5.html', {'top': top_tracks})


def contacts(request):
    contact = Contact.objects.all()
    return render(request, 'kzrap/contacts.html', {'contacts': contact})


def rappers(request):
    rapper = Rapper.objects.all()
    return render(request, 'kzrap/rappers.html', {'rappers': rapper})


def sponsors(request):
    return render(request, 'kzrap/sponsors.html')


def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'LAB5'
            message = 'Salem Aleikum!'
            recipient = form.cleaned_data.get('email')
            send_mail(subject,
                      message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Кетті!')
            return redirect('subscribe')

    return render(request, 'kzrap/successful.html', {'form': form})


