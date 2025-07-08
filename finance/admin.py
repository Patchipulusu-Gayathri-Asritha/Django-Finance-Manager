from django.contrib import admin
from .models import Addmoney_info, UserProfile
from django.contrib.sessions.models import Session

# Register your models here.
class Addmoney_infoAdmin(admin.ModelAdmin):
    list_display = ("user", "quantity", "Date", "Category", "add_money")

admin.site.register(Addmoney_info, Addmoney_infoAdmin)

admin.site.register(UserProfile)

admin.site.register(Session)