from django.contrib import admin
from .models import Item, Feedback
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
	list_display = ("id","item_name", "shop_name", "price","kind")
	search_fields = ('phone1','username','item')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
admin.site.register(Item, ItemAdmin)
class FeedbackAdmin(admin.ModelAdmin):
	list_display = ("user",'comment')
	search_fields = ('user',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
admin.site.register(Feedback, FeedbackAdmin)