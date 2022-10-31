from rest_framework import generics

from stageone.models import StageOneUser
from stageone.serializers import StageOneUserSerializer

# Create your views here.

class StageOneUserView(generics.RetrieveAPIView):
    queryset = StageOneUser.objects.all()
    serializer_class = StageOneUserSerializer
