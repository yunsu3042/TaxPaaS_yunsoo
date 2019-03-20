
class DisableCSRF(object):
    def process_request(self, request):
        setattr(self, '_dont_enforce_csrf_checks', True)