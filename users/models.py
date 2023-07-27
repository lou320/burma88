from django import forms
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.postgres.fields import ArrayField
import secrets
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your models here.
class MyUsersManager(BaseUserManager):
	def create_user(self, username, password=None):
		if not username:
			raise ValueError("user must have a username.")
		user = self.model(
            username = username
        )
		user.set_password(password)
		user.save(using = self._db)
		return user


	def create_superuser(self,  username, password):
		user = self.create_user(
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


def get_profile_image_filepath(self, filename):
	return 'profile_images/' + str(self.username) + '/profile_image.png'

def get_default_profile_image():
	return "https://github.com/lou320/weee_images/blob/main/default/default_image.png?raw=true"



# class Feedback(models.Model):
#     card = models.ForeignKey(Item, on_delete=models.CASCADE)
#     user = models.ForeignKey(Users, on_delete=models.CASCADE)
#     comment = models.TextField()
#     commented_at = models.DateTimeField(auto_now_add=True)






class Users(AbstractBaseUser):
	username 				= models.CharField(max_length=30, unique=True)
	phone					= models.CharField(max_length=20, blank=True)
	social_media_link		= models.CharField(max_length=255, blank=True)
	social_media_choice		= models.CharField(max_length=30, blank=True)
	bought_items            = ArrayField(models.IntegerField(), default=list, blank=True, null=True)
	saved_items 			= ArrayField(models.IntegerField(), default=list, blank=True, null=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	profile_image			= models.CharField(max_length=500, default=get_default_profile_image)
	is_shop					= models.BooleanField(default=False)
	shop_name				= models.CharField(max_length=200, null=True, blank=True)
	is_verified             = models.BooleanField(default=False)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	

	USERNAME_FIELD = 'username'
	# REQUIRED_FIELDS = []

	objects = MyUsersManager()
	def __str__(self):
		return self.username
	
	def get_profile_image_filename(self):
		return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) + "/"):]

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True
	
class SocialMedias(models.Model):
    MEDIA_CHOICES = [
    ('social_media', 'Social Media', [
	    'Facebook',
        'Telegram',
        'Viber',
        'YouTube',
    ]),
]