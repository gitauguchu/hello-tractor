import django
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import redirect, render, get_object_or_404
from sympy.physics.quantum import Operator

from .forms import *
from django.contrib import messages
from django.views import View
import decimal
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator # for Class Based Views


# Create your views here.

def home(request):
    categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
    products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    low_to_high = Product.objects.order_by('price')
    kenyan_deals = Product.objects.filter(country='Kenya')
    above_milli = Product.objects.order_by('price')
    context = {
        'categories': categories,
        'products': products,
        'low_to_high': low_to_high,
        'kenyan_deals': kenyan_deals,
        'above_milli': above_milli,
    }
    return render(request, 'store/index.html', context)


def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.exclude(id=product.id).filter(is_active=True, category=product.category)
    context = {
        'product': product,
        'related_products': related_products,

    }
    return render(request, 'store/detail.html', context)


def all_categories(request):
    categories = Category.objects.filter(is_active=True)
    return render(request, 'store/categories.html', {'categories':categories})


def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(is_active=True, category=category)
    categories = Category.objects.filter(is_active=True)
    locations = Product.objects.order_by().values('location').distinct()
    context = {
        'category': category,
        'products': products,
        'categories': categories,
        'locations': locations
    }
    return render(request, 'store/category_products.html', context)


# Authentication Starts Here

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'account/register.html', {'form': form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations! Registration Successful!")
            form.save()
        return render(request, 'account/register.html', {'form': form})


# class JobApplicationView(View):
#     def get(self, request):
#         jb_form = JobApplicationForm()
#         return render(request, 'account/register.html', {'jb_form': jb_form})
#
#     def post(self, request):
#         jb_form = JobApplicationForm(request.POST)
#         if jb_form.is_valid():
#             messages.success(request, "Successful Application! We will notify you once the company approves it..")
#             jb_form.save()
#         return render(request, 'store/job_posting.html', {'jb_form': jb_form})


def JobPostingView(request):
    if request.method == 'POST':
        jb_form = JobPostingForm(request.POST)
        if jb_form.is_valid():
            jb_form.save()
            messages.success(request, "Job Posted Successfully.")
            return redirect('store:jobs')
            # Redirect or render success page
    else:
        jb_form = JobPostingForm()



    context = {'jb_form': jb_form}
    return render(request, 'store/job_posting.html', context)


def JobApplicationView(request):
    if request.method == 'POST':
        jaf_form = JobApplicationForm(request.POST)
        if jaf_form.is_valid():
            jaf_form.save()
            messages.success(request, "Successful Application! We will notify you once the company approves it..")
            return redirect('store:jobs')
            # Redirect or render success page
    else:
        jaf_form = JobApplicationForm()



    context = {'jaf_form': jaf_form}
    return render(request, 'store/job_application.html', context)

@login_required
def profile(request):
    addresses = Address.objects.filter(user=request.user)
    orders = Order.objects.filter(user=request.user).count()
    products_posted = Product.objects.filter(seller=request.user).count()
    sms = InAppMessage.objects.filter(content=request.user).count()

    context = {
        'addresses':addresses,
        'orders':orders,
        'products_posted': products_posted,
        'sms': sms,
    }
    return render(request, 'account/profile.html', context)


@method_decorator(login_required, name='dispatch')
class AddressView(View):
    def get(self, request):
        form = AddressForm()
        return render(request, 'account/add_address.html', {'form': form})

    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            user=request.user
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            reg = Address(user=user, locality=locality, city=city, state=state)
            reg.save()
            messages.success(request, "New Address Added Successfully.")
        return redirect('store:profile')


@login_required
def remove_address(request, id):
    a = get_object_or_404(Address, user=request.user, id=id)
    a.delete()
    messages.success(request, "Address removed.")
    return redirect('store:profile')

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = get_object_or_404(Product, id=product_id)

    # Check whether the Product is alread in Cart or Not
    item_already_in_cart = Cart.objects.filter(product=product_id, user=user)
    if item_already_in_cart:
        cp = get_object_or_404(Cart, product=product_id, user=user)
        cp.quantity += 1
        cp.save()
    else:
        Cart(user=user, product=product).save()
    
    return redirect('store:cart')


@login_required
def cart(request):
    user = request.user
    cart_products = Cart.objects.filter(user=user)

    # Display Total on Cart Page
    amount = decimal.Decimal(0)
    shipping_amount = decimal.Decimal(10)
    # using list comprehension to calculate total amount based on quantity and shipping
    cp = [p for p in Cart.objects.all() if p.user==user]
    if cp:
        for p in cp:
            temp_amount = (p.quantity * p.product.price)
            amount += temp_amount

    # Customer Addresses
    addresses = Address.objects.filter(user=user)

    context = {
        'cart_products': cart_products,
        'amount': amount,
        'shipping_amount': shipping_amount,
        'total_amount': amount + shipping_amount,
        'addresses': addresses,
    }
    return render(request, 'store/cart.html', context)


@login_required
def remove_cart(request, cart_id):
    if request.method == 'GET':
        c = get_object_or_404(Cart, id=cart_id)
        c.delete()
        messages.success(request, "Item removed from Favourites.")
    return redirect('store:cart')


@login_required
def plus_cart(request, cart_id):
    if request.method == 'GET':
        cp = get_object_or_404(Cart, id=cart_id)
        cp.quantity += 1
        cp.save()
    return redirect('store:cart')


@login_required
def minus_cart(request, cart_id):
    if request.method == 'GET':
        cp = get_object_or_404(Cart, id=cart_id)
        # Remove the Product if the quantity is already 1
        if cp.quantity == 1:
            cp.delete()
        else:
            cp.quantity -= 1
            cp.save()
    return redirect('store:cart')


@login_required
def checkout(request):
    user = request.user
    address_id = request.GET.get('address')
    
    address = get_object_or_404(Address, id=address_id)
    # Get all the products of User in Cart
    cart = Cart.objects.filter(user=user)
    for c in cart:
        # Saving all the products from Cart to Order
        Order(user=user, address=address, product=c.product, quantity=c.quantity).save()
        # And Deleting from Cart
        c.delete()
    return redirect('store:orders')


@login_required
def orders(request):
    all_orders = Order.objects.filter(user=request.user).order_by('-ordered_date')
    return render(request, 'store/orders.html', {'orders': all_orders})



def shop(request):
    return render(request, 'store/shop.html')



def test(request):
    return render(request, 'store/test.html')


def operators(request):
    all_operators = TractorOperator.objects.all()
    context = {
        'all_operators': all_operators,
    }
    return render(request, 'store/operators.html', context)


def jobs(request):
    all_jobs = JobPosting.objects.all().distinct()
    total_jobs = JobPosting.objects.all().count()
    context = {
        'all_jobs': all_jobs,
        'total_jobs': total_jobs,
    }
    return render(request, 'store/jobs.html', context)


def InAppMessageView(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        message_content = request.POST.get("message_content")

        # Get the product
        product = get_object_or_404(Product, id=product_id)

        # Create a new message
        InAppMessage.objects.create(
            product=product,
            sender=request.user,
            recipient=product.seller,
            content=message_content
        )

        # Redirect to the cart or a success page
        return redirect("store:cart")

def product_comparison(request):
    search_products = Product.objects.all()
    product1 = None
    product2 = None

    if request.method == 'POST':
        print("Request Details Here --> ", request.POST)
        product1_id = request.POST.get('product1')  # Get product1 ID from the form
        product2_id = request.POST.get('product2')  # Get product2 ID from the form

        # Fetch products based on selected IDs
        if product1_id:
            product1 = get_object_or_404(Product, id=product1_id)
        if product2_id:
            product2 = get_object_or_404(Product, id=product2_id)

        print("Selected products:", product1, product2)

    context = {
        'search_products': search_products,
        'product1': product1,
        'product2': product2,
    }
    # return redirect('store/product-comparison')
    return render(request, 'store/compare.html', context)

def operator_application(request):
    if request.method == 'POST':
        oaf_form = TractorOperatorForm(request.POST)
        if oaf_form.is_valid():
            oaf_form.save()
            messages.success(request, "Successful Request! Pending Approval from admin...")
            return redirect('store:operators')
            # Redirect or render success page
    else:
        oaf_form = TractorOperatorForm()



    context = {'oaf_form': oaf_form}
    return render(request, 'store/operator_form.html', context)