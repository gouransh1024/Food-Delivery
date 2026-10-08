from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product, Profile
from .forms import CreateUserForm, ProfileForm
from .decorators import unauthenticated_user


@login_required(login_url='login')
def edit(request):
    return profilePage(request)

@login_required(login_url='login')
def profilePage(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your Profile is Updated')
            return redirect("/profile/")   
    else:
        form = ProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'edit.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, You are logged in.')
            return redirect("/")
        else:
            messages.info(request, 'Wrong password or username')
            return redirect('/login/')
    return render(request, 'login.html')

@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account is created.')
            return redirect('/login/')
        else:
            context = {'form': form}
            messages.info(request, 'Invalid credentials')
            return render(request, 'signin.html', context)

    context = {'form': form}
    return render(request, 'signin.html', context)

@login_required(login_url='login')
def logOut(request):
    logout(request)
    messages.info(request, 'You logged out successfully')
    return redirect('/login/')



def new(request):
    return render(request, "home.html")


def home(request):
    if request.method == "POST": 
        product_id = request.POST.get('product')
        if product_id:
            product = str(product_id)
            cart = request.session.get('cart', {})
            cart[product] = cart.get(product, 0) + 1
            request.session['cart'] = cart
            request.session.modified = True
            messages.success(request, 'Item added to cart!')
        return redirect('home')

    prs = Product.get_all_products()
    return render(request, 'menu.html', {"product": prs})

@login_required(login_url='login')
def cart_view(request):
    cart = request.session.get('cart', {})

    product_id_to_remove = request.POST.get('remove_product_id')
    if product_id_to_remove:
        if str(product_id_to_remove) in cart:
            del cart[str(product_id_to_remove)]
            request.session['cart'] = cart
            request.session.modified = True
            messages.success(request, 'Product removed from the cart.')
        return redirect('cart_view')

    product_ids = [pid for pid in cart.keys() if str(pid).isdigit()]
    products_in_cart = Product.objects.filter(id__in=product_ids)
    
    cart_with_details = {}
    total_price = 0
    for product in products_in_cart:
        qty = cart.get(str(product.id), 1)
        subtotal = float(product.price) * qty
        total_price += subtotal
        cart_with_details[product.id] = {
            'name': product.name,
            'image': product.image.url if product.image else '',
            'price': product.price,
            'quantity': qty,
            'subtotal': subtotal,
        }
    
    return render(request, 'cart.html', {'cart': cart_with_details, 'total_price': total_price})
