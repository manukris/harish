from django.contrib import admin

# Register your models here.

from .models import One,Two, Login

admin.site.register(One)

admin.site.register(Two)


admin.site.register(Login)