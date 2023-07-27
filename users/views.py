from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UsersAuthenticationForm, RegistrationForm, UsersUpdateForm
from django.contrib.auth import login, authenticate, logout
from .models import Users, SocialMedias
from items.models import Feedback, Item, KindOfItem
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def profile_view(request, *args, **kwargs):
    context = {}
    user_id = kwargs.get("user_id")
    try:
        account = Users.objects.get(pk=user_id)
    except Users.DoesNotExist:
        return HttpResponse("Something went wrong.")
        
    if account:
        context['id'] = account.id
        context['username'] = account.username
        context['profile_image'] = account.profile_image
        context['phone'] = account.phone
        context['user'] = Users.objects.get(id = account.id)
        context['shop_name'] = account.shop_name
        items = Item.objects.filter(shop_id = user_id)
        context['SocialMedias'] = SocialMedias.MEDIA_CHOICES
        context['social_media_choice'] = account.social_media_choice
        context['social_media_link'] = account.social_media_link
        context['items'] = items
        context['PRODUCT_CHOICES'] = KindOfItem.PRODUCT_CHOICES
        
        is_self = True
        cards = items.order_by('-id')
        paginator = Paginator(cards, 6)

        page_number = request.GET.get('page')
        cards = paginator.get_page(page_number)
        if page_number is not None and page_number != '':
            page_number = int(page_number)
        else:
            page_number = 0
        number_range = 0
        if paginator.num_pages > page_number +4:
            number_range = range(page_number, page_number + 4)
        elif paginator.num_pages > page_number +3:
            number_range = range(page_number, page_number + 3)
        elif paginator.num_pages > page_number +2:
            number_range = range(page_number, page_number + 2)
        elif paginator.num_pages > page_number +1:
            number_range = range(page_number, page_number + 1)
        else:
            number_range = range(page_number, page_number)
        context['items'] = cards
        context['number_range'] = number_range
        user = request.user
        if user.is_authenticated and user != account:
            is_self = False
        elif not user.is_authenticated:
            is_self = False

        context['is_self'] = is_self
        context['BASE_URL'] = settings.BASE_URL
        
        return render(request, "users/profile.html", context)
    return render(request, "users/profile.html", context)

@csrf_exempt
def update_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login")
    user_id = kwargs.get("user_id")
    try:
        account = Users.objects.get(pk=user_id)
    except Users.DoesNotExist:
        return HttpResponse("Something went wrong.")

    if account.pk != request.user.pk:
        return HttpResponse("You cannot edit someone elses profile")
    context = {}
    if request.POST:
        form = UsersUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile', user_id= user_id)
        else:
            context['errors'] = form.errors
            form = UsersUpdateForm(initial={
                "id": account.pk,
                "username": account.username,
                "phone": account.phone,
                "profile_image": account.profile_image,
                "social_media_choice": account.social_media_choice,
                "social_media_link": account.social_media_link
            })
            context['form'] = form
            return render(request, "users/update.html", context)
    else:
        
        form = UsersUpdateForm(request.POST, instance=request.user, initial={
                "id": account.pk,
                "username": account.username,
                "phone": account.phone,
                "profile_image": account.profile_image,
                "social_media_choice": account.social_media_choice,
                "social_media_link": account.social_media_link
            })
        context['form'] = form
    return redirect("/users/"+ str(user_id))
@csrf_exempt
def save_item(request, item_id):
    context = {}
    user = request.user
    item = Item.objects.get(id=item_id)
    comments = Feedback.objects.filter(card_id = item_id).order_by('-id')
    context = {
        'item': item,
        'comments': comments
    }
    context['PRODUCT_CHOICES'] = KindOfItem.PRODUCT_CHOICES
    context['order_user'] = user.id
    user_obj = Users.objects.get(pk = user.id)
    user_obj.saved_items.append(item.id)
    user_obj.save()
    return render(request, 'details.html', context)
@csrf_exempt
def saved_item_view(request):
    context = {}
    user = request.user
    items_list = user.saved_items
    cards = Item.objects.filter(id__in=items_list).order_by('-id')
    paginator = Paginator(cards, 10)

    page_number = request.GET.get('page')
    cards = paginator.get_page(page_number)
    if page_number is not None and page_number != '':
        page_number = int(page_number)
    else:
        page_number = 0
    number_range = 0
    if paginator.num_pages > page_number +4:
        number_range = range(page_number, page_number + 4)
    elif paginator.num_pages > page_number +3:
        number_range = range(page_number, page_number + 3)
    elif paginator.num_pages > page_number +2:
        number_range = range(page_number, page_number + 2)
    elif paginator.num_pages > page_number +1:
        number_range = range(page_number, page_number + 1)
    else:
        number_range = range(page_number, page_number)
    context['number_range'] = number_range
    context['items'] = cards
    context['PRODUCT_CHOICES'] = KindOfItem.PRODUCT_CHOICES
    return render(request, 'main/home.html', context)

@csrf_exempt
def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"You are already authenicated as {user.username}.\nPlease logout first.")
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            
            account = authenticate(username =username, password = raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect("home")
        else:
            context['registration_form'] = form
    return render(request, "users/registration.html", context)

@csrf_exempt
def login_view(request, *args, **kwargs):
    context={}
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    
    destination = get_redirect_if_exists(request)

    if request.POST:
        form = UsersAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect("/users/"+ str(user.id))
        else:
            context['login_form'] = form
    return render(request, 'users/login.html', context)

@csrf_exempt
def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect

@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('/')
