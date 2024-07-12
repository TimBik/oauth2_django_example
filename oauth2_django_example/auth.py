from django.contrib.auth.backends import ModelBackend
from django.http import HttpRequest
from authlib.integrations.django_client import OAuth


class OAuth2Authentication(ModelBackend):
    def __init__(self):
        self.oauth = OAuth()

        self.oauth.register(
            'github',
            client_kwargs={'scope': 'openid email'},
        )

    def authenticate(self, request: HttpRequest, username=None, password=None, **kwargs):
        redirect_uri = request.build_absolute_uri('/login')
        self.oauth.github.authorize_redirect(request, redirect_uri)
        return None
