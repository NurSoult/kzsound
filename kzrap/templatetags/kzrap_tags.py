from django import template
from kzrap.models import *

register = template.Library()


@register.simple_tag(name='gettracks')
def get_tracks():
    return Track.objects.all()


@register.simple_tag(name='getcontacts')
def get_contacts():
    return Contact.objects.all()


@register.simple_tag(name='getrappers')
def get_rappers():
    return Rapper.objects.all()
