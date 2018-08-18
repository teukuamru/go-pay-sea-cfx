from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from accounts.models import CustomUser


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken,
                         self).post(request, *args, **kwargs)
        
        token = Token.objects.get(key=response.data['token'])
        user_id = token.user_id
        username = CustomUser.objects.get(id=user_id).username
        
        response = {
            'token': token.key,
            'id': user_id,
            'username': username
        }
        return Response(response)
