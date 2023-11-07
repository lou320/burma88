from django.shortcuts import render
from items.models import Item, KindOfItem
from django.core.paginator import Paginator
from advertisement.models import Advertisement
from django.contrib.auth import get_user_model
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page

@cache_page(60)
def cached(request):
    user_model = get_user_model()
    all_users = user_model.objects.all()
    return HttpResponse('<html><body><h1>{0} users.. cached</h1></body></html>'.format(len(all_users)))


def cacheless(request):
    user_model = get_user_model()
    all_users = user_model.objects.all()
    return HttpResponse('<html><body><h1>{0} users.. cacheless</h1></body></html>'.format(len(all_users)))

@csrf_exempt
def home_screen_view(request, *args, **kwargs):
    context = {}
    cards = Item.objects.order_by('-id')
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
    context['advertisement'] = Advertisement.objects.all().order_by('-id')[:3]
    return render(request, 'main/home.html', context)