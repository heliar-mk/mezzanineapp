# -*-coding:utf-8-*-

from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from app.models import Registration, RegisterInfo

# Register your models here.


class RegistrationAdmin(PageAdmin):
    pass


class RegisterForm(admin.ModelAdmin):
    list_display = ("timestamp", "date", "name", "jobtime", "graduate", "phone", "email",)
    list_filter = ("timestamp", "date", "jobtime",)
    fieldsets = (
        ('学员基本信息', {
            'fields': ('date', 'name', 'jobtime', 'graduate', 'email', 'phone', 'resume')
            }),
        ('学员反馈', {
            'fields': ('question1', 'question2', 'question3')
            }),
        ('备注信息', {
            'fields': ('invoice', 'referrer')
            }),
        )


admin.site.register(Registration, RegistrationAdmin)
admin.site.register(RegisterInfo, RegisterForm)
