from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# from .forms import Signupform
from .models import User, Vacancy

# class CustomUserAdmin(UserAdmin):
#     model = User
#     add_form = Signupform
#     form = CustomUserChangeForm

# Register your models here.
admin.site.register(User) 
admin.site.register(Vacancy)
