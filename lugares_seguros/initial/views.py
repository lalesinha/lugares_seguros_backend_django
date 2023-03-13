from rest_framework.views import APIView
from rest_framework.response import Response
class HelloDrf(APIView):
    def get(self, request, formar=None):
        return Response ({"message": 'DRF: Lo logré de nuevo jijij'})