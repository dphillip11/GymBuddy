from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def is_past(date):
    return date < timezone.now().date()

@register.filter
def is_superuser(user):
    if not user:
        return False
    return user.is_superuser
