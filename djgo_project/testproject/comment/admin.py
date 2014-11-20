from django.contrib import admin

# Register your models here.

from comment.models import Users

class UserAdmin(admin.ModelAdmin):
    #changing order
    #fields = [
    #           'name',
    #           'email',
    #           'active',
    #           'register_date',
    #]
    fieldsets = [
    	(None, {'fields' : ['name', 'email']}),
        ('Date Info', {'fields' : ['register_date', 'active']}),
    ]

admin.site.register(Users, UserAdmin )


