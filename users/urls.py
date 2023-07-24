from django.urls import path
from . import views


app_name = "users"

urlpatterns=[
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('registration/', views.register_view, name="registration"),
    path('verify-email/<str:token>/', views.verify_email, name='verify_email'),
    path('save/<item_id>', views.save_item, name="save"),
    path('saved/saved_item/', views.saved_item_view, name="saved"),
    path('<user_id>/', views.profile_view , name="profile"),
    path('<user_id>/update/', views.update_view , name="update"),
    ]