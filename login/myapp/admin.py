from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Student, Practitioner

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('User Type', {'fields': ('is_student', 'is_practitioner')}),
    )
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_student', 'is_practitioner', 'is_staff', 'date_joined', 'last_login')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_first_name', 'get_last_name', 'get_email')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email')
    ordering = ('user__username',)

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.admin_order_field = 'user__first_name'
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.admin_order_field = 'user__last_name'
    get_last_name.short_description = 'Last Name'

    def get_email(self, obj):
        return obj.user.email
    get_email.admin_order_field = 'user__email'
    get_email.short_description = 'Email'

class PractitionerAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_first_name', 'get_last_name', 'get_email')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email')
    ordering = ('user__username',)

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.admin_order_field = 'user__first_name'
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.admin_order_field = 'user__last_name'
    get_last_name.short_description = 'Last Name'

    def get_email(self, obj):
        return obj.user.email
    get_email.admin_order_field = 'user__email'
    get_email.short_description = 'Email'

admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Practitioner, PractitionerAdmin)
