from django.contrib import admin
from .models import Profile,Questions
from .forms import UserRegisterForm
# Register your models here.
#admin.site.register(profile)

admin.site.register(Profile)
admin.site.register(Questions)
