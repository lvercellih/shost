from rest_framework.authentication import BaseAuthentication, get_authorization_header


class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()


    def authenticate_header(self, request):
        return 'Token'


class RsaAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()

    def authenticate_header(self, request):
        return 'RSA'
