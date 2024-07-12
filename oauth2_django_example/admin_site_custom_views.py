import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from oauth2_django_example.tools.oauth2 import GitHubOAuth2, GoogleOAuth2


class GitHubLoginView(APIView):
    def get(self, request, *args, **kwargs):
        query_params = request.query_params
        error = query_params.get('error')
        if error:
            logging.error(error)
            return Response({
                "error": error,
                "error_description": query_params.get("error_description")
            }, status=status.HTTP_200_OK)
        oauth = GitHubOAuth2()
        redirect_uri = request.build_absolute_uri('/oauth2/github/authorize')
        return oauth.login(request, redirect_uri)


class GitHubAuthorizeView(APIView):
    def get(self, request, *args, **kwargs):
        oauth = GitHubOAuth2()
        user_info = oauth.authorize(request)
        return Response(
            data={**user_info},
            status=status.HTTP_200_OK)


class GoogleLoginView(APIView):
    def get(self, request, *args, **kwargs):
        query_params = request.query_params
        error = query_params.get('error')
        if error:
            logging.error(error)
            return Response({
                "error": error,
                "error_description": query_params.get("error_description")
            }, status=status.HTTP_200_OK)
        oauth = GoogleOAuth2()
        redirect_uri = request.build_absolute_uri('/oauth2/google/authorize')
        return oauth.login(request, redirect_uri)


class GoogleAuthorizeView(APIView):
    def get(self, request, *args, **kwargs):
        oauth = GoogleOAuth2()
        user_info = oauth.authorize(request)
        return Response(
            data={**user_info},
            status=status.HTTP_200_OK)
