# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-07-16 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseInfo',
            fields=[
                ('Crt_Time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('Upd_Time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('expense_id', models.AutoField(primary_key=True, serialize=False, verbose_name='表ID')),
                ('bill_id', models.IntegerField(verbose_name='账单记录id')),
                ('expense_name', models.CharField(max_length=20, verbose_name='消费记录名')),
                ('expense_type', models.CharField(max_length=20, verbose_name='消费类型')),
                ('expense_time', models.DateTimeField(verbose_name='消费时间')),
                ('expense_cost', models.DecimalField(decimal_places=3, max_digits=12, verbose_name='消费金额')),
                ('expense_content', models.CharField(max_length=100, verbose_name='消费备注')),
            ],
            options={
                'verbose_name': '消费记录表',
                'verbose_name_plural': '消费记录表',
                'db_table': 'TAB_EXPENSE',
            },
        ),
    ]