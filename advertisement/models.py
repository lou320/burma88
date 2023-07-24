from django.db import models
from users.models import Users
# Create your models here.

class Advertisement(models.Model):
    shop_ads				= models.ImageField(upload_to='ads_images/',max_length=255,null=True, blank=True,)
    ad_shop              = models.ForeignKey(Users, on_delete=models.CASCADE)
    ads_post_date				= models.DateTimeField(auto_now_add=True)
    