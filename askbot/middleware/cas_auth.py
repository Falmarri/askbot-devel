from django.conf import settings
from django.contrib.auth import authenticate, login
import caslib
import logging

LOG = logging.getLogger(__name__)

class CASMiddleware(object):

    

    def __init__(self):
        caslib.SELF_SIGNED_CERT = True
        caslib.cas_init('https://auth.iplantcollaborative.org', 'https://localhost:8080/CAS_serviceValidater?sendback=/application/')

    def process_request(self, request):
        if request.user.is_anonymous() and request.GET['ticket']:
            if not request.session['cas_check']:
                user = authenticate(method='cas', cas_token=request.GET['ticket'])
                if user and user.is_active:
                    login(request, user)

        request.session['cas_check'] = True
                    