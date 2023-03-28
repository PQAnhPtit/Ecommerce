from django.contrib import admin
from customer_model.models import user_registration

class UserAdmin(admin.ModelAdmin):
    list_display = ('fname','lname','email','mobile','password','address')

admin.site.register(user_registration, UserAdmin)
