# context_processors.py
from django.conf import settings # type: ignore
from writely.settings import env 

def google_client_id(request):
    return {
        'GOOGLE_CLIENT_ID': env('GOOGLE_CLIENT_ID')
    }