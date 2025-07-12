from rest_framework import viewsets


from django.contrib.auth.models import User
from .models import *
from .serializers import *

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ClothingItemViewSet(viewsets.ModelViewSet):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer

class SwapRequestViewSet(viewsets.ModelViewSet):
    queryset = SwapRequest.objects.all()
    serializer_class = SwapRequestSerializer

class RedemptionRequestViewSet(viewsets.ModelViewSet):
    queryset = RedemptionRequest.objects.all()
    serializer_class = RedemptionRequestSerializer

class PointWalletViewSet(viewsets.ModelViewSet):
    queryset = PointWallet.objects.all()
    serializer_class = PointWalletSerializer
