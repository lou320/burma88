from django.urls import path
from . import views


app_name = "items"

urlpatterns=[
    path('item/<item_id>/', views.detail_view, name="detail"),
    path('delete/<item_id>/', views.delete_item, name="delete"),
    path('edit/<item_id>/', views.edit_item, name="edit"),
    path('kind/<kind>/', views.kind_view, name="kind"),
    path('post/', views.post, name="post"),
    path('comment/', views.comment, name="comment"),
    path('search/', views.search_view, name="search"),

    ]