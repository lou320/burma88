from django.db import models
from django import forms
from users.models import Users
from cloudinary.models import CloudinaryField

# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    shop_id = models.IntegerField()
    item_name = models.CharField(max_length=30)
    shop_name = models.CharField(max_length=20)
    price = models.IntegerField()
    item_link = models.CharField(max_length=500)
    details = models.TextField()
    gram = models.IntegerField()
    item_image1 = CloudinaryField('image_1', null=True, blank=True)
    item_image2 = CloudinaryField('image_2', null=True, blank=True)
    item_image3 = CloudinaryField('image_3', null=True, blank=True)
    date_posted= models.DateTimeField(verbose_name="card_date", auto_now_add=True)
    kind = models.CharField(max_length=100, null=False, default='nokind')
    discount = models.CharField(max_length=200, blank=True, null=True)
    # visit_count = models.IntegerField(default=0)

class ItemForm(forms.ModelForm):
    details = forms.Textarea()
    item_image1 = CloudinaryField()
    item_image2 = CloudinaryField()
    item_image3 = CloudinaryField()
    class Meta:
        model = Item
        fields = ("id", "shop_id", "item_name", "shop_name", 'discount',"price","details","gram","kind",'item_link',"item_image1", "item_image2", "item_image3")

class ItemEditForm(forms.ModelForm):
    details = forms.Textarea()
    item_image1 = CloudinaryField()
    item_image2 = CloudinaryField()
    item_image3 = CloudinaryField()
    class Meta:
        model = Item
        fields = ("id", "shop_id", "item_name", "shop_name", 'discount',"price","details","gram","kind",'item_link',"item_image1", "item_image2", "item_image3")
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
        'THC pen',
        'Local',
        'Press',
        'Mid Grade',
        'Exotic',
    ]),
    ('chemical', 'Chemicals', [
        'LSD',
        'DMDT',
        'Lean',
    ]),
    ('mushroom', 'Mushroom', [
        'Microdose',
        'Golden Teacher',
        'Melmac',
        'Albino Penis Envy',
        'African Transkei',
        'DK 60',
        'Z',
        'Nut Cracker',
        'Malabar'
    ]),
    ('blue_lotus', 'Blue Lotus', [
        'Blue Lotus',
    ]),
    ('accessories', 'Accessories',[
        'Mushroom Grower Kit'
    ])
]

# class ImageStore(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.CharField(max_length=255)
#     image = CloudinaryField('image')
