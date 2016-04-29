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
    platform = models.ForeignKey(Platform, verbose_name='平台',related_name='status_code')

    def __str__(self):
        return str(self.status_code_value)


class ApiClass(models.Model):
    clas_name = models.CharField(max_length=64, verbose_name='api类别')
    platform = models.ForeignKey(Platform, verbose_name='平台',related_name='api_class')

    def __str__(self):
        return self.clas_name


class Field(models.Model):
    FIELD_TYPE = ((1, 'String'), (2, 'int'), (3, 'long'), (4, 'double'),(5,'对象'))
    field_name = models.CharField(max_length=32, verbose_name='参数名称')
    field_describe = models.TextField(null=True, max_length=1024, verbose_name='参数描述')
    is_must = models.BooleanField(default=False, verbose_name='是否必填')
    field_type = models.IntegerField(choices=FIELD_TYPE, verbose_name='类型')
    field_length = models.IntegerField(blank=True, verbose_name='长度')
    parent_field = models.ForeignKey('self', null=True, blank=True, related_name='children',verbose_name='父参数')
    def __str__(self):
        return self.field_name + Field.FIELD_TYPE[self.field_type][1]


class Api(models.Model):
    HTTP11_METHOD = ((1, 'GET'), (2, 'POST'), (3, 'DELETE'), (4, 'PUT'))
    API_STATUS = ((1, '开通'), (2, '未开通'))
    api_class = models.ForeignKey(ApiClass, verbose_name='api类别',related_name='api')
    api_name = models.CharField(max_length=64, verbose_name='名称')
    api_describe = models.TextField(null=True, max_length=64, verbose_name='描述')
    api_status = models.IntegerField(default=2, choices=API_STATUS, verbose_name='开通状态')
    api_url = models.CharField(max_length=64, verbose_name='URL')
    request_method = models.IntegerField(choices=HTTP11_METHOD, verbose_name='请求方法')
    request_example = models.TextField(max_length=1024, verbose_name='请求示例')
    response_success_example = models.TextField(max_length=1024, verbose_name='请求成功示例')
    response_fail_example = models.TextField(max_length=1024, verbose_name='请求失败示例')

    def __str__(self):
        return self.api_name


class RequestField(Field):
    api_requset = models.ForeignKey(Api, related_name='api_requset_field', verbose_name='api')
    def __str__(self):
        return self.api_requset.api_name+self.field_name +"("+ Field.FIELD_TYPE[self.field_type][1]+")"

class ResponseField(Field):
    api_response = models.ForeignKey(Api, related_name='api_response_field', verbose_name='api')
    def __str__(self):
        return self.api_response.api_name+self.field_name +"("+ Field.FIELD_TYPE[self.field_type][1]+")"