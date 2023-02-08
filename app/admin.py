from django.contrib import admin
from .models import User,Page
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','user_name','password']
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=['id','page_name','page_catalog','publication_date']