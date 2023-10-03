from rest_framework import generics
from django.utils import timezone
from .models import CustomUser, Auction
from .serializers import UserSerializer, AuctionSerializer

class UserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class AuctionListView(generics.ListCreateAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

class OngoingAuctionListView(generics.ListAPIView):
    queryset = Auction.objects.filter(end_time__gt=timezone.now())
    serializer_class = AuctionSerializer

class AllAuctionsListView(generics.ListAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
