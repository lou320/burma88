from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

from advertisement.models import Advertisement
from .models import KindOfItem, SearchForm, Item, ItemForm, Feedback
from users.models import Users

# Create your views here.
@csrf_exempt
def detail_view(request, item_id):
    item = Item.objects.get(id=item_id)
    comments = Feedback.objects.filter(card_id=item_id).order_by('-id')
    context = {
        'item': item,
        'comments': comments,
        'PRODUCT_CHOICES': KindOfItem.PRODUCT_CHOICES,
    }
    if request.user.is_authenticated:
        context['order_user'] = request.user.id
        context['phone1'] = request.user.phone

    return render(request, 'details.html', context)

@csrf_exempt
def kind_view(request, kind):
    result_items = Item.objects.filter(kind__icontains=kind).order_by('-id')
    paginator = Paginator(result_items, 5)
    page_number = request.GET.get('page')
    if page_number == None:
        page_number= 1
    items = paginator.get_page(page_number)
    number_range = range(int(page_number), int(page_number) + min(4, paginator.num_pages - int(page_number)))

    context = {
        'items': items,
        'number_range': number_range,
        'PRODUCT_CHOICES': KindOfItem.PRODUCT_CHOICES,
        'advertisement': Advertisement.objects.all().order_by('-id')[:3]
    }

    return render(request, 'main/home.html', context)

@csrf_exempt
def search_view(request):
    context = {}
    if request.POST:
        form = SearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            results = Item.objects.filter(item_name__icontains=search_query).order_by('-id')
            paginator = Paginator(results, 5)
            page_number = request.GET.get('page')
            if page_number == None:
                page_number= 1
            items = paginator.get_page(page_number)
            number_range = range(int(page_number), int(page_number) + min(4, paginator.num_pages - int(page_number)))

            context = {
                'items': items,
                'number_range': number_range,
                'PRODUCT_CHOICES': KindOfItem.PRODUCT_CHOICES
            }
            return render(request, 'main/home.html', context)
        else:
            context['error'] = "Something went wrong."
    else:
        context['error'] = "Item not found."

    return render(request, 'main/home.html', context)

@csrf_exempt
def post(request):
    context = {}
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_verified:
                item = form.save(commit=False)
                item.id = None
                item.shop_id = form.cleaned_data['shop_id']
                item.item_name = form.cleaned_data['item_name']
                item.shop_name = form.cleaned_data['shop_name']
                item.price = form.cleaned_data['price']
                item.details = form.cleaned_data['details']
                item.kind = form.cleaned_data['kind']
                item.item_link = form.cleaned_data['item_link']
                item.item_image1 = form.cleaned_data['item_image1']
                item.item_image2 = form.cleaned_data['item_image2']
                item.item_image3 = form.cleaned_data['item_image3']
                item.save()
                items = Item.objects.filter(shop_id=form.cleaned_data['shop_id'])
                user = Users.objects.get(id=form.cleaned_data['shop_id'])
                context = {
                    'form': form,
                    'items': items,
                    'user': user,
                }
                return redirect('/users/' + str(request.user.id))  # Redirect to a success page after saving the form
            else:
                items = Item.objects.order_by('-id')
                paginator = Paginator(items, 5)
                page_number = request.GET.get('page')
                items = paginator.get_page(page_number)
                if page_number == None:
                    page_number = 1
                number_range = range(int(page_number), int(page_number) + min(4, paginator.num_pages - int(page_number)))
                context['items'] = items
                context['advertisement'] = Advertisement.objects.all().order_by('-id')[:3]
                context['number_range'] = number_range
                context['form'] = form
                return render(request, 'main/home.html', context)
        else:
            return redirect('/users/' + str(request.user.id))
    else:
        form = ItemForm()
        items = Item.objects.get(seller_id=form.cleaned_data['shop_id'])
        context = {
            'form': form,
            'items': items
        }
    return redirect('/users/' + str(request.user.id))

@csrf_exempt
def comment(request, *args, **kwargs):
    context = {}
    user = request.user
    card = request.POST.get('card')
    comment = request.POST.get('comment')
    if user.is_authenticated:
        if request.POST:
            new_comment = Feedback(card=Item.objects.get(id=card), user=user, comment=comment)
            new_comment.save()
    else:
        cards = Item.objects.order_by('-id')
        paginator = Paginator(cards, 5)
        page_number = 1
        cards = paginator.get_page(page_number)
        number_range = range(int(page_number), int(page_number) + min(4, paginator.num_pages - int(page_number)))
        context['number_range'] = number_range
        context['items'] = cards
        context['PRODUCT_CHOICES'] = KindOfItem.PRODUCT_CHOICES
        context['advertisement'] = Advertisement.objects.all().order_by('-id')[:3]
        context['error'] = "You need to login first."
        return render(request, "main/home.html", context)
    return redirect("/items/item/" + str(card))


@csrf_exempt
def delete_item(requeset, *args, **kwargs):
    item_id = kwargs.get('item_id')
    item = Item.objects.get(id = item_id)
    item.delete()
    return redirect('home')