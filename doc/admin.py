from django.contrib import admin
from .models import *


# Register your models here.
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('platform_name', 'signature_rule', 'test_root_url', 'formal_root_url')


admin.site.register(Platform, PlatformAdmin)


class StatusCodeAdmin(admin.ModelAdmin):
    list_display = ('status_code_value', 'status_describe', 'platform_id')


admin.site.register(StatusCode, StatusCodeAdmin)


class ApiClassAdmin(admin.ModelAdmin):
    list_display = ('platform', 'class_name')


admin.site.register(ApiClass, ApiClassAdmin)


class ApiAdmin(admin.ModelAdmin):
    list_display = ('api_class', 'api_name', 'request_method', 'api_url', 'api_status')


admin.site.register(Api, ApiAdmin)

