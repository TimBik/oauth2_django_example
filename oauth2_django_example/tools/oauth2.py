import json

from authlib.integrations.django_client import OAuth
from requests import Response


class OAuth2Base:
    def __init__(self, provider_name, **kwargs):
        oauth = OAuth()
        self.oauth = oauth.register(
            provider_name,
            **kwargs
        )

    def login(self, request, redirect_uri=None):
        return self.oauth.authorize_redirect(request, redirect_uri)

    def authorize(self, request):
        return self.oauth.authorize_access_token(request)

class GitHubOAuth2(OAuth2Base):
    def __init__(self, **kwargs):
        super(GitHubOAuth2, self).__init__(
            provider_name='github',
            client_kwargs={'scope': 'openid email'},
            **kwargs,
        )
    def authorize(self, request):
        token = super().authorize(request)
        resp_user: Response = self.oauth.get('user', token=token)
        user_info = json.loads(resp_user.content)
        return user_info


class GoogleOAuth2(OAuth2Base):
    def __init__(self, **kwargs):
        super(GoogleOAuth2, self).__init__(
            provider_name='google',
            client_kwargs={'scope': 'openid email profile'},
            **kwargs,
        )

    def authorize(self, request):
        token = super().authorize(request)
        return token['userinfo']