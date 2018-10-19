from django.contrib import admin

# Register your models here.

from .models import Thurtle, Cards

admin.site.register(Thurtle)


admin.site.register(Cards)