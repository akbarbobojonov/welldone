from django.contrib import admin

from apps.cprofile.models import CProfile

class CProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email_verified',)
    list_filter = ('email_verified', 'key_expires',)

    # inlines = [
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)

admin.site.register(CProfile, CProfileAdmin)