from django.contrib import admin

# Register your models here.

from api.models import memberProfile, category, newsAndHighlight,contactMsg

class memberAdmin(admin.ModelAdmin):
    list_filter = [
        "playing_in",
    ]
    list_display = [
        'user' , 'first_name', 'last_name', 'gender','contact_number', 'age', 'paid_registration_fee','approved', 'fee_pending'
    ]



admin.site.register(memberProfile, memberAdmin)
admin.site.register(category)
admin.site.register(newsAndHighlight)
admin.site.register(contactMsg)




admin.site.site_header = 'Pinaka Rifle Shooting Club | ADMIN'