

# Register your models here.
from django.contrib import admin
from .models import ClothingItem, PointWallet, SwapRequest, RedemptionRequest, UserProfile

# Custom display for ClothingItem
@admin.register(ClothingItem)
class ClothingItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'category', 'size', 'condition', 'available', 'listed_on')
    list_filter = ('category', 'size', 'condition', 'available')
    search_fields = ('name', 'owner__username')


@admin.register(PointWallet)
class PointWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'points')
    search_fields = ('user__username',)


@admin.register(SwapRequest)
class SwapRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_user', 'to_user', 'offered_item', 'requested_item', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('from_user__username', 'to_user__username')


@admin.register(RedemptionRequest)
class RedemptionRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'item', 'status', 'requested_on', 'fulfilled_on')
    list_filter = ('status',)
    search_fields = ('user__username', 'item__name')
    
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'style_preference')
    search_fields = ('user__username', 'location', 'style_preference')

