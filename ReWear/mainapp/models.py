

# Create your models here.from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User




CATEGORY_CHOICES = [
    ('Topwear', 'Topwear'),
    ('Bottomwear', 'Bottomwear'),
    ('Footwear', 'Footwear'),
    ('Accessories', 'Accessories'),
    ('Outerwear', 'Outerwear'),
    ('Other', 'Other'),
]

SIZE_CHOICES = [
    ('XS', 'Extra Small'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
    ('XXL', 'XX-Large'),
    ('Free', 'Free Size'),
]

CONDITION_CHOICES = [
    ('New', 'Brand New'),
    ('Like New', 'Like New'),
    ('Used', 'Used - Good'),
    ('Worn', 'Worn - Fair'),
]

SWAP_STATUS = [
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
    ('completed', 'Completed'),
]

REDEEM_STATUS = [
    ('pending', 'Pending'),
    ('fulfilled', 'Fulfilled'),
    ('cancelled', 'Cancelled'),
]



class ClothingItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clothing_items')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    size = models.CharField(max_length=5, choices=SIZE_CHOICES)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    available = models.BooleanField(default=True)
    is_redeemable = models.BooleanField(default=True)
    listed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.owner.username})"


class PointWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet')
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.points} pts"

class SwapRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='swap_requests_sent')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='swap_requests_received')
    offered_item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE, related_name='offered_in_swaps')
    requested_item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE, related_name='requested_in_swaps')
    status = models.CharField(max_length=20, choices=SWAP_STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    responded_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.from_user.username} offers {self.offered_item.name} for {self.to_user.username}'s {self.requested_item.name}"



class RedemptionRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='redemption_requests')
    item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE, related_name='redemption_requests')
    status = models.CharField(max_length=20, choices=REDEEM_STATUS, default='pending')
    requested_on = models.DateTimeField(auto_now_add=True)
    fulfilled_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} requested {self.item.name} [{self.status}]"
    
    
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    contact_number = models.CharField(max_length=15, blank=True)
    style_preference = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Casual')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

