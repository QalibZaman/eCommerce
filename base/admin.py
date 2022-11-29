from django.contrib import admin
from .models import UserDetails, Following, Sharing
# Register your models here.
admin.site.register(UserDetails)
admin.site.register(Following)
admin.site.register(Sharing)