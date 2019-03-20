
from rest_framework.authentication import SessionAuthentication

class CsrfExcempSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return