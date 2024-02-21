from rest_framework import generics, permissions
from blinkboard-dfr.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(APIView):
    def post(self, request):
        serializer = FollowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowerDetail(APIView):
    def delete(self, request, pk):
        follower = Follower.objects.get(pk=pk)
        follower.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


