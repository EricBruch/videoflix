from rest_framework import viewsets, permissions, authentication
from .models import Video
from .serializers import VideoSerializer

# Create your views here.


class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view and add videos
    """

    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]  # IsAuthenticatedOrReadOnly
