from django.shortcuts import render
from .models import RobotsTxt

def robots_txt_view(reqest):
    robots = RobotsTxt.objects.get()
    context = {'robots': robots}
    response = render(reqest, 'robots.txt', context, content_type='text/plain')
    return response

