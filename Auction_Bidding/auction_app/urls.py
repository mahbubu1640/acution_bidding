from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from auction_app.views import UserListView, AuctionListView, OngoingAuctionListView, AllAuctionsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/users/', UserListView.as_view(), name='user-list-create'),
    path('api/auctions/', AuctionListView.as_view(), name='auction-list-create'),
    path('api/ongoing-auctions/', OngoingAuctionListView.as_view(), name='ongoing-auctions-list'),
    path('api/all-auctions/', AllAuctionsListView.as_view(), name='all-auctions-list'),
]
