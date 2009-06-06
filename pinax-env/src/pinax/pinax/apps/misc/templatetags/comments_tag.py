from django import template
from django.conf import settings

register = template.Library()

def comments(context, obj):
    return {
        'object': obj, 
        'request': context['request'],
        'user': context['user'],
        "MEDIA_URL": settings.MEDIA_URL,
    }

register.inclusion_tag('threadedcomments/comments.html', takes_context=True)(comments)
