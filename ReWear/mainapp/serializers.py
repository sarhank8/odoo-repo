from rest_framework import serializers
from django.contrib.auth.models import User


from .models import (
    UserProfile, ClothingItem,
    SwapRequest, RedemptionRequest,
    PointWallet
)

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# User Profile Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

# Clothing Item Serializer
class ClothingItemSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = ClothingItem
        fields = '__all__'

# Point Wallet Serializer
class PointWalletSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = PointWallet
        fields = '__all__'

# Swap Request Serializer
class SwapRequestSerializer(serializers.ModelSerializer):
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)
    offered_item = ClothingItemSerializer(read_only=True)
    requested_item = ClothingItemSerializer(read_only=True)

    class Meta:
        model = SwapRequest
        fields = '__all__'

# Redemption Request Serializer
class RedemptionRequestSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    item = ClothingItemSerializer(read_only=True)

    class Meta:
        model = RedemptionRequest
        fields = '__all__'
