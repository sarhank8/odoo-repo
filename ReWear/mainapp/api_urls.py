from rest_framework import routers


from .api_views import (
    UserViewSet, UserProfileViewSet,
    ClothingItemViewSet, SwapRequestViewSet,
    RedemptionRequestViewSet, PointWalletViewSet
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', UserProfileViewSet)
router.register(r'items', ClothingItemViewSet)
router.register(r'swaps', SwapRequestViewSet)
router.register(r'redemptions', RedemptionRequestViewSet)
router.register(r'wallets', PointWalletViewSet)

urlpatterns = router.urls
