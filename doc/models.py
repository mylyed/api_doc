from django.db import models


# Create your models here.
# 平台
class Platform(models.Model):
    # 平台名称
    # 签名规则
    # 测试地址
    # 正式地址
    platform_name = models.CharField(max_length=64, verbose_name='平台名称')
    signature_rule = models.TextField(max_length=1024, verbose_name='签名规则')
    test_root_url = models.CharField(max_length=64, verbose_name='测试根地址')
    formal_root_url = models.CharField(max_length=64, verbose_name='正式根地址')

    def __str__(self):
        return self.platform_name


class StatusCode(models.Model):
    # -状态码
    status_code_value = models.IntegerField(verbose_name='状态码')
    # -状态描述
    status_describe = models.TextField(max_length=1024, verbose_name='状态码描述')
    platform = models.ForeignKey(Platform, verbose_name='平台', related_name='status_code')

    def __str__(self):
        return str(self.status_code_value)


class ApiClass(models.Model):
    class_name = models.CharField(max_length=64, verbose_name='api类别')
    platform = models.ForeignKey(Platform, verbose_name='平台', related_name='api_class')

    def __str__(self):
        return self.class_name


class Api(models.Model):
    HTTP11_METHOD = ((1, 'GET'), (2, 'POST'), (3, 'DELETE'), (4, 'PUT'))
    API_STATUS = ((1, '开通'), (2, '未开通'))
    api_class = models.ForeignKey(ApiClass, verbose_name='api类别', related_name='api')
    api_name = models.CharField(max_length=64, verbose_name='名称')
    api_describe = models.TextField(null=True, max_length=64, verbose_name='描述')
    api_status = models.IntegerField(default=2, choices=API_STATUS, verbose_name='开通状态')
    api_url = models.CharField(max_length=64, verbose_name='URL')
    request_method = models.IntegerField(choices=HTTP11_METHOD, verbose_name='请求方法')
    request_fields = models.TextField(max_length=1024, verbose_name='请求参数')
    request_example = models.TextField(max_length=1024, verbose_name='请求示例')
    response_fields = models.TextField(max_length=1024, verbose_name='返回参数')
    response_success_example = models.TextField(null=True, max_length=1024, verbose_name='请求成功示例')
    response_fail_example = models.TextField(null=True, max_length=1024, verbose_name='请求失败示例')

    def __str__(self):
        return self.api_name
