from django.contrib import admin
from .models import profile
# Register your models here.

class BookAdmin(admin.ModelAdmin):
	list_display=['__str__','contact']
	class Meta:
		model=profile

admin.site.register(profile,BookAdmin)
