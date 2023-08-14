from django.db import models
from django import forms
from users.models import Users
# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    shop_id = models.IntegerField()
    item_name = models.CharField(max_length=30)
    shop_name = models.CharField(max_length=20)
    price = models.IntegerField()
    item_link = models.CharField(max_length=500)
    details = models.CharField(max_length=500)
    item_image1 = models.CharField(max_length=500, default='https://github.com/lou320/weee_images/blob/main/noimage.jpg?raw=true')
    item_image2 = models.CharField(max_length=500, default='https://github.com/lou320/weee_images/blob/main/noimage.jpg?raw=true')
    item_image3 = models.CharField(max_length=500, default='https://github.com/lou320/weee_images/blob/main/noimage.jpg?raw=true')
    date_posted= models.DateTimeField(verbose_name="card_date", auto_now_add=True)
    kind = models.CharField(max_length=100, null=False, default='nokind')
    discount = models.CharField(max_length=200, blank=True, null=True)
    # visit_count = models.IntegerField(default=0)

class ItemForm(forms.ModelForm):
    details = forms.CharField(widget=forms.Textarea)
    item_image1 = forms.CharField(required=False)
    item_image2 = forms.CharField(required=False)
    item_image3 = forms.CharField(required=False)
    class Meta:
        model = Item
        fields = ("id", "shop_id", "item_name", "shop_name", 'discount',"price","details","kind",'item_link',"item_image1", "item_image2", "item_image3")

class Feedback(models.Model):
    card = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)

class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search')

class KindOfItem(models.Model):
    PRODUCT_CHOICES = [
    ('Weed', 'Weed', [
        'Mango',
        'Purple mango',
        'Og',
        'Kyout',
        'Green Crack',
        'Lemon Press',
        'Kush',
        'Og',
        'Apple Banana',
        'Wedding Cake',
        'Northern Light'
        
    ]),
    ('chemical', 'Chemicals', [
        'LSD',
        'DMDT',
        'K',
        'E'
    ]),
    ('mushroom', 'Mushroom', [
        'Golden Teacher',
        'Melmac',
        'Albino Penis Envy',
        'African Transkei',
        'DK 60',
        'Z',
        'Nut Cracker',
        'Malabar'
    ]),
]
