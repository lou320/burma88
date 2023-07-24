from django.contrib import admin
from .models import Advertisement
# Register your models here.
class AdvertisementAmin(admin.ModelAdmin):
	list_display = ('ad_shop','ads_post_date')
	search_fields = ('ad_shop','ads_post_date')
	readonly_fields=('ads_post_date',)
	raw_id_fields = ['ad_shop']
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Advertisement, AdvertisementAmin)
