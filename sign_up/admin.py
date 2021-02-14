from django.contrib import admin

from . import models

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	# fields = ("login", )
	exclude = ("login", )

admin.site.register(models.User, UserAdmin)
