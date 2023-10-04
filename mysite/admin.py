from django.contrib import admin
from mysite.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','pub_date')#讓管理者可以看到這些
    
admin.site.register(Post,PostAdmin) #之後連到 http://localhost:8000/admin
