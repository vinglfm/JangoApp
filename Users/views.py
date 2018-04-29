from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import logout


# Create your views here.

def logout_view(request):
    """Log out user"""
    logout(request)
    return HttpResponseRedirect(reverse('tango_do:index'))
