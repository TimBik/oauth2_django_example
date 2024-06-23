from authlib.integrations.django_client import OAuth
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        # user = authenticate(request)
        self.oauth = OAuth()

        self.oauth.register(
            'github',
            client_kwargs={'scope': 'user:email'},
        )
        redirect_uri = request.build_absolute_uri('/login')
        return self.oauth.github.authorize_redirect(request, redirect_uri)
