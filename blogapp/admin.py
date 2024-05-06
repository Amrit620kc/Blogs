from django.contrib import admin
from blogapp.models import Category, Post,Contact,Comment

# Register your models here.
class CatAdmin(admin.ModelAdmin):
    list_display=('image_tag','name')
admin.site.register(Category,CatAdmin)


admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Comment)


