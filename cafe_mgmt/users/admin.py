from django.contrib import admin
from users.models.user_details import UserDetails


class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'mob_number', 'status']
    list_display_links = ('id', 'email')
    search_fields = ('id', 'first_name', 'last_name', 'mob_number', 'email')
    readonly_fields=('first_name', 'last_name', 'mob_number', 'email', 'password')
    list_per_page = 20

admin.site.register(UserDetails, UserDetailsAdmin)

