# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-09-26 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasCustInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(blank=True, max_length=12, null=True, verbose_name='健检号')),
                ('xm', models.CharField(blank=True, max_length=50, null=True, verbose_name='姓名')),
                ('xb', models.CharField(blank=True, max_length=1, null=True, verbose_name='性别')),
                ('csrq', models.DateField(blank=True, null=True, verbose_name='出生日期')),
                ('sfzhm', models.CharField(blank=True, max_length=18, null=True, verbose_name='身份证号码')),
                ('mz', models.CharField(blank=True, max_length=4, null=True, verbose_name='民族')),
                ('whcd', models.CharField(blank=True, max_length=2, null=True, verbose_name='文化程度')),
                ('gj', models.CharField(blank=True, max_length=4, null=True, verbose_name='国家')),
                ('hyzk', models.CharField(blank=True, max_length=2, null=True, verbose_name='婚姻状况')),
                ('jtzz', models.CharField(blank=True, max_length=200, null=True, verbose_name='家庭住址')),
                ('yzbm', models.CharField(blank=True, max_length=6, null=True, verbose_name='邮政编码')),
                ('lxdh', models.CharField(blank=True, max_length=40, null=True, verbose_name='联系电话')),
                ('yddh', models.CharField(blank=True, max_length=11, null=True, verbose_name='移动电话')),
                ('dwdm', models.CharField(blank=True, max_length=12, null=True, verbose_name='单位代码')),
                ('dwmc', models.CharField(blank=True, max_length=60, null=True, verbose_name='婚姻状况')),
                ('email', models.CharField(blank=True, max_length=20, null=True, verbose_name='邮箱')),
                ('bz', models.CharField(blank=True, max_length=50, null=True, verbose_name='是否职工')),
                ('djsj', models.DateField(blank=True, null=True, verbose_name='登记时间')),
                ('djr', models.CharField(blank=True, max_length=6, null=True, verbose_name='登记人')),
                ('province', models.CharField(blank=True, max_length=12, null=True, verbose_name='所属身份')),
                ('city', models.CharField(blank=True, max_length=12, null=True, verbose_name='所属城市')),
                ('region', models.CharField(blank=True, max_length=12, null=True, verbose_name='所属区域')),
                ('cust_type', models.CharField(blank=True, max_length=6, null=True, verbose_name='客户类型')),
                ('zwdm', models.CharField(blank=True, max_length=12, null=True, verbose_name='职务代码')),
                ('cw', models.CharField(blank=True, max_length=20, null=True, verbose_name='客人所属单位组')),
                ('zycd', models.CharField(blank=True, max_length=20, null=True, verbose_name='工作职业')),
                ('hycd', models.CharField(blank=True, max_length=20, null=True, verbose_name='工作行业')),
                ('khly', models.CharField(blank=True, max_length=6, null=True, verbose_name='客户来源')),
                ('zhye', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='账户余额')),
                ('member_type', models.CharField(blank=True, max_length=2, null=True, verbose_name='确认模式')),
                ('card_code', models.CharField(blank=True, max_length=12, null=True, verbose_name='健检号')),
                ('member_card_code', models.CharField(blank=True, max_length=12, null=True, verbose_name='会员卡号')),
                ('trans_status', models.CharField(blank=True, max_length=1, null=True, verbose_name='传输状态')),
                ('op_date', models.DateField(blank=True, null=True, verbose_name='修改时间')),
                ('ywydm', models.CharField(blank=True, max_length=6, null=True, verbose_name='业务员代码')),
                ('gsgddh', models.CharField(blank=True, max_length=20, null=True, verbose_name='公司固定电话')),
                ('khtz', models.CharField(blank=True, max_length=200, null=True, verbose_name='客人特征')),
                ('gstz', models.CharField(blank=True, max_length=150, null=True, verbose_name='公司地址')),
                ('txtz', models.CharField(blank=True, max_length=150, null=True, verbose_name='通讯地址')),
                ('yxjb', models.CharField(blank=True, max_length=2, null=True, verbose_name='有效级别')),
                ('cust_region', models.CharField(blank=True, max_length=1, null=True, verbose_name='客人区域')),
                ('k3_item', models.CharField(blank=True, max_length=80, null=True, verbose_name='K3公司代码')),
                ('k3_zg_item', models.CharField(blank=True, max_length=40, null=True, verbose_name='K3职工代码')),
                ('bgd_lb', models.CharField(blank=True, max_length=1, null=True, verbose_name='报告单类别')),
                ('grgz_ye', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='挂账余额')),
                ('zzys', models.CharField(blank=True, max_length=6, null=True, verbose_name='咨询医生')),
                ('xgsj', models.DateField(blank=True, null=True, verbose_name='修改时间')),
                ('user_password', models.CharField(blank=True, max_length=20, null=True, verbose_name='用户密码')),
                ('password_xgsj', models.DateField(blank=True, null=True, verbose_name='密码修改时间')),
                ('zzhs', models.CharField(blank=True, max_length=6, null=True, verbose_name='ZZHS')),
            ],
            options={
                'verbose_name': '基本信息',
                'verbose_name_plural': '基本信息',
                'db_table': 'bas_cust_infor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JjYyqkb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', models.CharField(blank=True, max_length=12, null=True, verbose_name='VID编号')),
                ('cid', models.CharField(blank=True, max_length=12, null=True, verbose_name='健检号')),
                ('dwdm', models.CharField(blank=True, max_length=12, null=True, verbose_name='单位编码')),
                ('yysj', models.DateField(blank=True, null=True, verbose_name='预约时间')),
                ('yyzh', models.CharField(blank=True, max_length=2, null=True, verbose_name='预约组号')),
                ('yydjr', models.CharField(blank=True, max_length=6, null=True, verbose_name='预约登记人')),
                ('yydjsj', models.DateField(blank=True, null=True, verbose_name='预约登记时间')),
                ('jjzh', models.CharField(blank=True, max_length=5, null=True, verbose_name='健检组号')),
                ('jjlsh', models.FloatField(blank=True, null=True, verbose_name='健检流水号')),
                ('status', models.CharField(blank=True, max_length=1, null=True, verbose_name='预约状态')),
                ('qtdjr', models.CharField(blank=True, max_length=6, null=True, verbose_name='前台登记人')),
                ('qtdjsj', models.DateField(blank=True, null=True, verbose_name='前台登记时间')),
                ('tjsj', models.DateField(blank=True, null=True, verbose_name='体检时间')),
                ('tjzzsj', models.DateField(blank=True, null=True, verbose_name='体检终止时间')),
                ('tzf', models.CharField(blank=True, max_length=1, null=True, verbose_name='停止否')),
                ('dwjzf', models.CharField(blank=True, max_length=1, null=True, verbose_name='团体体检否')),
                ('member_type', models.CharField(blank=True, max_length=2, null=True, verbose_name='会员类型')),
                ('yydhtzr', models.CharField(blank=True, max_length=25, null=True, verbose_name='预约电话通知人')),
                ('yyth', models.CharField(blank=True, max_length=12, null=True, verbose_name='预约电话')),
                ('zyf', models.CharField(blank=True, max_length=1, null=True, verbose_name='数据转移否')),
                ('jjch', models.CharField(blank=True, max_length=12, null=True, verbose_name='报告单方式')),
                ('print_time', models.DateField(blank=True, null=True, verbose_name='打印时间')),
                ('trans_status', models.CharField(blank=True, max_length=10, null=True, verbose_name='传输状态')),
                ('ywydm', models.CharField(blank=True, max_length=6, null=True, verbose_name='业务员代码')),
                ('yqhff', models.CharField(blank=True, max_length=1, null=True, verbose_name='一期回访否')),
                ('erqhff', models.CharField(blank=True, max_length=1, null=True, verbose_name='二期回访否')),
                ('sqhff', models.CharField(blank=True, max_length=1, null=True, verbose_name='三期回访否')),
                ('tcbl', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True, verbose_name='VID')),
                ('dwyyid', models.CharField(blank=True, max_length=30, null=True, verbose_name='单位预约ID')),
                ('cust_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='姓名')),
                ('cust_xb', models.CharField(blank=True, max_length=2, null=True, verbose_name='性别')),
                ('cust_csrq', models.DateField(blank=True, null=True, verbose_name='出生日期')),
                ('temp_bz', models.CharField(blank=True, max_length=3000, null=True, verbose_name='临时备注')),
                ('cust_zy', models.CharField(blank=True, max_length=20, null=True, verbose_name='职业')),
                ('cust_gzhy', models.CharField(blank=True, max_length=20, null=True, verbose_name='工作行业')),
                ('zzys', models.CharField(blank=True, max_length=6, null=True, verbose_name='咨询医生')),
                ('zzhs', models.CharField(blank=True, max_length=6, null=True, verbose_name='ZZHS')),
                ('in_floor', models.CharField(blank=True, max_length=10, null=True, verbose_name='制定进入某一层')),
                ('gzhy_dm', models.CharField(blank=True, max_length=20, null=True, verbose_name='工作行业代码')),
                ('bz_fgs', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注-分公司')),
                ('bz_bm1', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注-部门1')),
                ('bz_bm2', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注-部门2')),
                ('bz_ygh', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注-员工号')),
                ('bz_sfzhm', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注-身份证号码')),
                ('bz_a', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注-A')),
                ('bz_b', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注-B')),
                ('bz_c', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注-C')),
                ('bz_xj', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='备注-XJ')),
                ('bz_gz', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='备注-GZ')),
                ('bz_lpk', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='备注-LQK')),
            ],
            options={
                'verbose_name': '预约详情',
                'verbose_name_plural': '预约详情',
                'db_table': 'jj_yyqkb',
                'managed': False,
            },
        ),
    ]
