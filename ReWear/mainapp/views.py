# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile, ClothingItem, PointWallet, SwapRequest, RedemptionRequest

# Landing Page
def landing_view(request):
    return render(request, 'index.html')

# Signup

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'signup.html', {'error': "Passwords don't match"})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': "Username already taken"})

        user = User.objects.create_user(username=username, email=email, password=password1)
        
        # ✅ Assign user object to ForeignKey field
        UserProfile.objects.create(user=user)
        PointWallet.objects.create(user=user)

        login(request, user)
        return redirect('dashboard')

    return render(request, 'signup.html')



# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


# Logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('landing')


# Dashboard



def dashboard_view(request):
    user = request.user
    profile = get_object_or_404(UserProfile, user=user)
    wallet = get_object_or_404(PointWallet, user=user)

    user_items = ClothingItem.objects.filter(owner=user)
    swap_requests = SwapRequest.objects.filter(to_user=user)

    # Derived values for dashboard stats
    items_listed = user_items.count()
    swap_requests_made = SwapRequest.objects.filter(from_user=user).count()
    swap_requests_completed = SwapRequest.objects.filter(from_user=user, status='accepted').count()
    items_redeemed = RedemptionRequest.objects.filter(user=user).count()
    items_listed = user_items.count()
    swap_requests_made = SwapRequest.objects.filter(from_user=user).count()
    swap_requests_completed = SwapRequest.objects.filter(from_user=user, status='accepted').count()
    items_redeemed = RedemptionRequest.objects.filter(user=user).count()

    context = {
        'profile': profile,
        'wallet': wallet,
        'user_items': user_items,
        'swap_requests': swap_requests,
        'items_listed': items_listed,
        'swap_requests_made': swap_requests_made,
        'swap_requests_completed': swap_requests_completed,
        'items_redeemed': items_redeemed,
    }

    return render(request, 'dashboard.html', context)


# Add Item
def add_item_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        category = request.POST['category']
        size = request.POST['size']
        condition = request.POST['condition']
        tags = request.POST['tags']
        image = request.FILES.get('image')

        ClothingItem.objects.create(
            owner=request.user,
            title=title,
            description=description,
            category=category,
            size=size,
            condition=condition,
            tags=tags,
            image=image,
            is_available=True
        )
        messages.success(request, "Item uploaded.")
        return redirect('dashboard')

    return render(request, 'add_item.html')


# View item detail
def item_detail_view(request, item_id):
    item = get_object_or_404(ClothingItem, id=item_id)
    return render(request, 'item_detail.html', {'item': item})
