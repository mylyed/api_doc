# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-29 02:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0002_auto_20160429_0045'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestField',
            fields=[
                ('field_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='doc.Field')),
            ],
            bases=('doc.field',),
        ),
        migrations.CreateModel(
            name='ResponseField',
            fields=[
                ('field_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='doc.Field')),
            ],
            bases=('doc.field',),
        ),
        migrations.RemoveField(
            model_name='api',
            name='request_field',
        ),
        migrations.RemoveField(
            model_name='api',
            name='response_field',
        ),
        migrations.RemoveField(
            model_name='field',
            name='field_escribe',
        ),
        migrations.AddField(
            model_name='field',
            name='field_describe',
            field=models.TextField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='api',
            name='request_method',
            field=models.IntegerField(choices=[('GET', 1), ('POST', 2), ('DELETE', 3), ('PUT', 4)]),
        ),
        migrations.AlterField(
            model_name='field',
            name='field_type',
            field=models.IntegerField(choices=[('String', 1), ('int', 2), ('long', 3), ('double', 4)]),
        ),
        migrations.AlterField(
            model_name='statuscode',
            name='status_describe',
            field=models.TextField(max_length=64),
        ),
        migrations.DeleteModel(
            name='DataDict',
        ),
        migrations.AddField(
            model_name='responsefield',
            name='api_response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='api_response', to='doc.Api'),
        ),
        migrations.AddField(
            model_name='requestfield',
            name='api_requset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='api_requset', to='doc.Api'),
        ),
    ]
