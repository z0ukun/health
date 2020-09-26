# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# 后台用户信息类
class UserProfile(AbstractUser):
    id = models.AutoField(primary_key=True, verbose_name=u"序号")
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default=u"")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    Address = models.CharField(verbose_name=u"家庭住址", default=u"", max_length=100)
    gender = models.CharField(choices=(("male", u"男"), ("female", u"女")), max_length=10, default="male",
                              verbose_name=u"性别", )
    mobile = models.CharField(verbose_name=u"联系电话", max_length=11, null=True, blank=True)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


# # 图片传输存储
# class JjOtherTpPrint(models.Model):
#     vid = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"体检号")
#     lb = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"类别")
#     filename = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"文件名称")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     bz1 = models.CharField(max_length=1000, blank=True, null=True, verbose_name=u"备注1")
#     bz2 = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"备注2")
#     bz3 = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"备注3")
#     in_factory = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"in_factory")
#     print_type = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"打印类型")
#
#     class Meta:
#         managed = False
#         db_table = 'jj_other_tp_print'
#         verbose_name = u"图片传输存储表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 医生模板表
# class SysTemplet2014(models.Model):
#     tempid = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"模板ID")
#     # id = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"ID")
#     templetename = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"模板名称")
#     userid = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"用户ID")
#     dept_code = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"科室代码")
#     yxf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"有效否")
#     mbms = models.CharField(max_length=2000, blank=True, null=True, verbose_name=u"模板描述")
#     czsj = models.DateField(blank=True, null=True, verbose_name=u"操作时间")
#     sxh = models.FloatField(blank=True, null=True, verbose_name=u"顺序号")
#     mbms_ft = models.CharField(max_length=2000, blank=True, null=True, verbose_name=u"模板明细-FT")
#     mbms_english = models.CharField(max_length=2000, blank=True, null=True, verbose_name=u"模板明细-英文")
#     jb = models.IntegerField(blank=True, null=True, verbose_name=u"级别")
#     yzjf = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"有子集否")
#     templetename_ft = models.CharField(max_length=80, blank=True, null=True, verbose_name=u"模板名称-FT")
#     templetename_en = models.CharField(max_length=80, blank=True, null=True, verbose_name=u"模板名称-英文")
#     sjdm = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"上级代码")
#     # 建议类型 1：指标偏高 2：指标偏低  3：固定数值
#     advice_type = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"建议类型")
#     advice_title = models.CharField(max_length=80, blank=True, null=True, verbose_name=u"建议标题")
#     advice_context = models.CharField(max_length=1000, blank=True, null=True, verbose_name=u"建议内容")
#     value_xx = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"结果下限")
#     value_sx = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"结果上限")
#     sfjb = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"是否疾病")
#     ycbw = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"异常部位")
#     jbbt = models.CharField(max_length=300, blank=True, null=True, verbose_name=u"JBBT")
#     trans_status = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"传输状态")
#     temp_bz1 = models.CharField(max_length=300, blank=True, null=True, verbose_name=u"模板备注1")
#     temp_bz2 = models.CharField(max_length=300, blank=True, null=True, verbose_name=u"模板备注2")
#     temp_bz3 = models.CharField(max_length=300, blank=True, null=True, verbose_name=u"模板备注3")
#     temp_bz4 = models.CharField(max_length=300, blank=True, null=True, verbose_name=u"模板备注4")
#     temp_bz5 = models.CharField(max_length=300, blank=True, null=True, verbose_name=u"模板备注5")
#     temp_bz6 = models.CharField(max_length=300, blank=True, null=True, verbose_name=u"模板备注6")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"修改时间")
#     temp_bz7 = models.CharField(max_length=300, blank=True, null=True, verbose_name=u"模板备注7")
#     yxlb = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"YX类别")
#
#     class Meta:
#         managed = False
#         db_table = 'sys_templet_2014'
#         verbose_name = u"医生模板表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.tempid
#
#
# # 异常部位表
# class SysYcBw2014(models.Model):
#     bw = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"部位")
#     sxh = models.IntegerField(blank=True, null=True, verbose_name=u"顺序号")
#     yxf = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"有效否")
#     djsj = models.DateField(blank=True, null=True, verbose_name=u"预约登记时间")
#     trans_status = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"传输状态")
#
#     # id = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"ID")
#
#     class Meta:
#         managed = False
#         db_table = 'sys_yc_bw_2014'
#         verbose_name = u"异常部位表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.bw
#
#
# # 基础部分
# # 客人基本信息
# class BasCustInfor(models.Model):
#     cid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"健检号")
#     xm = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"姓名")
#     xb = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"性别")
#     csrq = models.DateField(blank=True, null=True, verbose_name=u"出生日期")
#     sfzhm = models.CharField(max_length=18, blank=True, null=True, verbose_name=u"身份证号码")
#     mz = models.CharField(max_length=4, blank=True, null=True, verbose_name=u"民族")
#     whcd = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"文化程度")
#     gj = models.CharField(max_length=4, blank=True, null=True, verbose_name=u"国家")
#     hyzk = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"婚姻状况")
#     jtzz = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"家庭住址")
#     yzbm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"邮政编码")
#     lxdh = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"联系电话")
#     yddh = models.CharField(max_length=11, blank=True, null=True, verbose_name=u"移动电话")
#     dwdm = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"单位代码")
#     dwmc = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"婚姻状况")
#     email = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"邮箱")
#     bz = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"是否职工")
#     djsj = models.DateField(blank=True, null=True, verbose_name=u"登记时间")
#     djr = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"登记人")
#     province = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"所属身份")
#     city = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"所属城市")
#     region = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"所属区域")
#     cust_type = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"客户类型")
#     zwdm = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"职务代码")
#     # 客人所属单位组(属于单位定义的什么组)
#     cw = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"客人所属单位组")
#     zycd = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"工作职业")
#     hycd = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"工作行业")
#     khly = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"客户来源")
#     zhye = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=u"账户余额")
#     member_type = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"确认模式")
#     card_code = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"健检号")
#     member_card_code = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"会员卡号")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     op_date = models.DateField(blank=True, null=True, verbose_name=u"修改时间")
#     ywydm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"业务员代码")
#     gsgddh = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"公司固定电话")
#     khtz = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"客人特征")
#     gstz = models.CharField(max_length=150, blank=True, null=True, verbose_name=u"公司地址")
#     txtz = models.CharField(max_length=150, blank=True, null=True, verbose_name=u"通讯地址")
#     # 有效级（0：单店 1：多店)
#     yxjb = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"有效级别")
#     # 客人区域（1：来源于体检 2：来源于医务室)
#     cust_region = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"客人区域")
#     k3_item = models.CharField(max_length=80, blank=True, null=True, verbose_name=u"K3公司代码")
#     k3_zg_item = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"K3职工代码")
#     bgd_lb = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"报告单类别")
#     grgz_ye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"挂账余额")
#     zzys = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"咨询医生")
#     xgsj = models.DateField(blank=True, null=True, verbose_name=u"修改时间")
#     user_password = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"用户密码")
#     password_xgsj = models.DateField(blank=True, null=True, verbose_name=u"密码修改时间")
#     zzhs = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"ZZHS")
#
#     class Meta:
#         managed = False
#         db_table = 'bas_cust_infor'
#         verbose_name = u"客人基本信息"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.cid
#
#
# # 操作员表
# class BasUserPasswd(models.Model):
#     dept_code = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"科室代码")
#     user_id = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"用户ID")
#     username = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"用户")
#     password = models.CharField(max_length=8, blank=True, null=True, verbose_name=u"密码")
#     adm_flag = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"adm_flag")
#     status = models.FloatField(blank=True, null=True, verbose_name=u"状态")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     op_date = models.DateField(blank=True, null=True, verbose_name=u"修改时间")
#     bzpym = models.CharField(max_length=8, blank=True, null=True, verbose_name=u"标准拼音码")
#     in_factory = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"in_factory")
#
#     class Meta:
#         managed = False
#         db_table = 'bas_user_passwd'
#         verbose_name = u"操作员表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.dept_code
#
#
# # 基本套餐表
# class BasChargeGroup(models.Model):
#     groupid = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"组号")
#     groupname = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"组名")
#     price = models.FloatField(blank=True, null=True, verbose_name=u"价格")
#     unit = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"单位")
#     standard = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"规格")
#     sjdm = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"上级代码")
#     jb = models.FloatField(blank=True, null=True, verbose_name=u"级别")
#     yzjf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"有子集否")
#     bzpym = models.CharField(max_length=8, blank=True, null=True, verbose_name=u"标准拼音码")
#     yxf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"有效否")
#     jxf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"继续否")
#     jclb = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"进程类别")
#     print_datawindow = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"打印-时间窗口")
#     aid_code = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"aid_code")
#     in_factory = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"in_factory")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     group_en = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"group_en")
#     group_ft = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"group_ft")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"数据时间")
#
#     class Meta:
#         managed = False
#         db_table = 'bas_charge_group'
#         verbose_name = u"基本套餐表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.groupid
#
#
# # 检查项目表
# class BasChargeItem(models.Model):
#     item_id = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"项目ID")
#     item_name = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"项目名称")
#     item_ename = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"项目英文名")
#     price = models.FloatField(blank=True, null=True, verbose_name=u"价格")
#     unit = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"单位")
#     sfcjyb = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"是否采集样本")
#     standard = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"规格")
#     sjdm = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"上级代码")
#     jb = models.FloatField(blank=True, null=True, verbose_name=u"级别")
#     yzjf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"有子集否")
#     bzpym = models.CharField(max_length=8, blank=True, null=True, verbose_name=u"标准拼音码")
#     yxf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"有效否")
#     userobject = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"用户对象")
#     sfjy = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"数据时间")
#     mcjysj = models.IntegerField(blank=True, null=True, verbose_name=u"mcjysj")
#     sample_type_id = models.CharField(max_length=4, blank=True, null=True, verbose_name=u"简单类型ID")
#     zyphf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"zyphf")
#     sxh = models.IntegerField(blank=True, null=True, verbose_name=u"sxh")
#     aid_code = models.CharField(max_length=15, blank=True, null=True, verbose_name=u"aid_code")
#     xb_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"XB状态")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     in_factory = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"in_factory")
#     is_picture = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"是否拍照")
#     picture_widht = models.BigIntegerField(blank=True, null=True, verbose_name=u"图片宽度")
#     picture_height = models.BigIntegerField(blank=True, null=True, verbose_name=u"图片高度")
#     item_ft = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"数据时间")
#     page_pic_number = models.IntegerField(blank=True, null=True, verbose_name=u"数据时间")
#     total_page = models.IntegerField(blank=True, null=True, verbose_name=u"总页数")
#     before_eat = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"饭前")
#     init_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=u"初始价格")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"数据时间")
#
#     class Meta:
#         managed = False
#         db_table = 'bas_charge_item'
#         verbose_name = u"检查项目表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.item_id
#
#
# # 小贴士字典表
# class JjPrintXts(models.Model):
#     dm = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"代码")
#     mc = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"名称")
#     bzpym = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"标准拼音码")
#     sjdm = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"上级代码")
#     jb = models.IntegerField(blank=True, null=True, verbose_name=u"级别")
#     yzjf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"有子集否")
#     print_datawindow = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"打印数据窗口")
#     print_text = models.CharField(max_length=4000, blank=True, null=True, verbose_name=u"打印内容")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#
#     class Meta:
#         managed = False
#         db_table = 'jj_print_xts'
#         verbose_name = u"小贴士字典表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.dm
#
#
# # 单位信息表
# class BasEntInfo(models.Model):
#     dwdm = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"单位代码")
#     dwmc = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"单位名称")
#     dwdz = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"单位地址")
#     yzbm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"邮政编码")
#     lxr = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"联系人")
#     lxdh = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"联系电话")
#     yddh = models.CharField(max_length=11, blank=True, null=True, verbose_name=u"移动电话")
#     email = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"邮箱地址")
#     dwcz = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"单位传真")
#     fzr = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"负责人")
#     djr = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"预约登记人")
#     djsj = models.DateField(blank=True, null=True, verbose_name=u"登记时间")
#     bzpym = models.CharField(max_length=8, blank=True, null=True, verbose_name=u"标准拼音码")
#     zhye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"账户余额")
#     ywydm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"业务员代码")
#     khly = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"客户来源")
#     gshyye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"公司和约定额余额")
#     gshy_jkye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"公司和约交款余额")
#     k3_item = models.CharField(max_length=80, blank=True, null=True, verbose_name=u"K3项目代码")
#     k3_zg_item = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"K3职工代码")
#     k3_zg_item_name = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"K3职工名称")
#     lxs_ye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"旅行社挂帐余额")
#     hy_ye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"会议挂帐余额")
#     dwgz_ye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"单位普通挂帐余额")
#     gn_1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"港中旅集团有限公司挂帐余额")
#     gn_2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"港中旅国际投资有限公司挂帐余额")
#     gn_3 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"港中旅国际投资内部企业挂帐余额")
#     gn_4 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"港中旅集团非中投企业挂帐余额")
#     zzys = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"个人挂帐余额")
#     prior_dwdm = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"prior_单位代码")
#     dw_password = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"单位密码")
#     password_xgsj = models.DateField(blank=True, null=True, verbose_name=u"密码XGSJ")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     zzhs = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"zzhs")
#     gzhy_dm = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"gzhy_dm")
#
#     class Meta:
#         managed = False
#         db_table = 'bas_ent_info'
#         verbose_name = u"单位信息表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.dwdm
#
#
# # 套餐对应项目
# class BasGroupItem(models.Model):
#     groupid = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"组号")
#     item_id = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"项目ID")
#     yxf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"有效否")
#     in_factory = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"in_factory")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"修改时间")
#     yxjb = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"有效级别")
#     xmmc = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"项目名称")
#     dkdx = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"dkdx")
#
#     class Meta:
#         managed = False
#         db_table = 'bas_group_item'
#         verbose_name = u"套餐对应项目"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.groupid
#
#
# # 检验项目指标表
# class LisGroupItem(models.Model):
#     groupid = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"组号")
#     testitem_id = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"测试项目ID")
#     # 仪器对应值编码(与机器相关的编码)
#     dyzbm = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"仪器对应值编码")
#     sxh = models.IntegerField(blank=True, null=True, verbose_name=u"顺序号")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"修改时间")
#
#     class Meta:
#         managed = False
#         db_table = 'lis_group_item'
#         verbose_name = u"检验项目指标表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.groupid
#
#
# # 检查指标表
# class LisTestItem(models.Model):
#     testitem_id = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"项目编号")
#     testitem_name_e = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"英文名称")
#     testitem_name_c = models.CharField(max_length=150, blank=True, null=True, verbose_name=u"中文名称")
#     testitem_short = models.CharField(max_length=8, blank=True, null=True, verbose_name=u"名称简称")
#     unit = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"单位")
#     testmethod_id = models.CharField(max_length=4, blank=True, null=True, verbose_name=u"检验方法")
#     qc_method_id = models.CharField(max_length=4, blank=True, null=True, verbose_name=u"质控方法")
#     sjdm = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"上级代码")
#     jb = models.FloatField(blank=True, null=True, verbose_name=u"级别")
#     yzjf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"有子集否")
#     bzpym = models.CharField(max_length=8, blank=True, null=True, verbose_name=u"标准拼音码")
#     yxf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"有效否")
#     flag_qc = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"flag_qc")
#     price = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True, verbose_name=u"价格")
#     testitem_ft = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"testitem_ft")
#     init_value = models.CharField(max_length=16, blank=True, null=True, verbose_name=u"init_value")
#     in_factory = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"in_factory")
#     aid_code = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"aid_code")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"修改时间")
#
#     class Meta:
#         managed = False
#         db_table = 'lis_test_item'
#         verbose_name = u"检查指标表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.testitem_id
#
#
# # 检验项目对应仪器表
# class LisGroupApparatus(models.Model):
#     sample_type_id = models.CharField(max_length=4, blank=True, null=True, verbose_name=u"样本类型")
#     apparatusid = models.CharField(max_length=4, blank=True, null=True, verbose_name=u"设备号")
#     groupid = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"组号")
#     sfdlwc = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"sfdlwc")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"修改时间")
#
#     class Meta:
#         managed = False
#         db_table = 'lis_group_apparatus'
#         verbose_name = u"检验项目对应仪器表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.sample_type_id
#
#
# # 检查项目指标表
# class BasJcItemList(models.Model):
#     item_id = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"项目代码")
#     table_id = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"模板ID号")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"修改时间")
#     in_factory = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"in_factory")
#
#     class Meta:
#         managed = False
#         db_table = 'bas_jc_item_list'
#         verbose_name = u"检查项目指标表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.item_id
#
#
# # 数据完整日志表
# class SysDataComplete(models.Model):
#     code_value = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"code_value")
#     lb = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"类别")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"修改时间")
#     in_factory = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"in_factory")
#
#     class Meta:
#         managed = False
#         db_table = 'sys_data_complete'
#         verbose_name = u"数据完整日志表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.code_value
#
#
# # 客人密码变更日志
# class CustChangePassLog(models.Model):
#     cid = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"健检号")
#     change_time = models.DateField(blank=True, null=True, verbose_name=u"修改时间")
#     old_pass = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"旧密码")
#     new_pass = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"新密码")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"数据时间")
#
#     class Meta:
#         managed = False
#         db_table = 'cust_change_pass_log'
#         verbose_name = u"客人密码变更日志"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.cid
#
#
# # 全国订单套餐变更
# class SaleQgddGroup(models.Model):
#     # id = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"ID")
#     billcode = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"单号")
#     dwdm = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"单位代码")
#     lb = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"类别")
#     in_factory = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"in_factory")
#     groupid = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"组号")
#     r_groupid = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"r_groupid")
#     member_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True,
#                                        verbose_name=u"member_price")
#     price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"价格")
#     bz1 = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"备注1")
#     bz2 = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"备注2")
#     bz3 = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"备注3")
#     status = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"状态")
#     trans_status = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"传输状态")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"数据时间")
#     audit_opername = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"audit_opername")
#     item_id = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"项目编号")
#     r_item_id = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"r_item_id")
#
#     class Meta:
#         managed = False
#         db_table = 'sale_qgdd_group'
#         verbose_name = u"全国订单套餐变更"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.billcode
#
#
# # 全国订单范围
# class SaleQgddFw(models.Model):
#     # id = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"ID")
#     billcode = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"单号")
#     in_factory = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"in_factory")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"数据时间")
#     trans_status = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"传输状态")
#     status = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"状态")
#     bz1 = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"备注1")
#     bz2 = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"备注2")
#     bz3 = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"备注3")
#
#     class Meta:
#         managed = False
#         db_table = 'sale_qgdd_fw'
#         verbose_name = u"全国订单范围"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.billcode
#
#
# # CT核磁胃镜统计表
# class JjDxysInterface(models.Model):
#     vid = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"VID")
#     item_id = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"项目编号")
#     item_name = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"项目名称")
#     czsj = models.DateField(blank=True, null=True, verbose_name=u"操作时间")
#     status = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"状态")
#     trans_status = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"传输状态")
#     bz1 = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"备注1")
#     bz2 = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"备注2")
#     bz3 = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"备注3")
#
#     class Meta:
#         managed = False
#         db_table = 'jj_dxys_interface'
#         verbose_name = u"CT核磁胃镜统计表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 集团统计表一
# class JjTraceYclog(models.Model):
#     vid = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"VID")
#     in_factory = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"in_factory")
#     cid = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"健检号")
#     dwdm = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"单位代码")
#     xm = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"姓名")
#     yysj = models.DateField(blank=True, null=True, verbose_name=u"预约时间")
#     status = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"状态")
#     je = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"金额")
#     bz1 = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"备注1")
#     bz2 = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"备注2")
#     bz3 = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"备注3")
#     trans_status = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"传输状态")
#
#     class Meta:
#         managed = False
#         db_table = 'jj_trace_yclog'
#         verbose_name = u"集团统计表一"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 延期放弃列表
# class JjYqfqList(models.Model):
#     vid = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"VID")
#     item_id = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"项目代码")
#     in_factory = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"in_factory")
#     item_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"项目名称")
#     cid = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"健检号")
#     xm = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"姓名")
#     xb = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"性别")
#     csrq = models.DateField(blank=True, null=True, verbose_name=u"出生日期")
#     dwdm = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"单位代码")
#     sfzhm = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"身份证号码")
#     fgs = models.CharField(max_length=300, blank=True, null=True, verbose_name=u"分公司")
#     bm1 = models.CharField(max_length=300, blank=True, null=True, verbose_name=u"部门1")
#     bm2 = models.CharField(max_length=300, blank=True, null=True, verbose_name=u"部门2")
#     ygh = models.CharField(max_length=300, blank=True, null=True, verbose_name=u"员工号")
#     status = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"状态")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     yysj = models.DateField(blank=True, null=True, verbose_name=u"预约时间")
#     clsj = models.DateField(blank=True, null=True, verbose_name=u"处理时间")
#     bz1 = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"备注1")
#     bz2 = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"备注2")
#     bz3 = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"备注3")
#
#     class Meta:
#         managed = False
#         db_table = 'jj_yqfq_list'
#         verbose_name = u"延期放弃列表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 健康问卷
#
#
# # 业务表
# # 客人预约情况表
# class JjYyqkb(models.Model):
#     vid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"VID编号")
#     cid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"健检号")
#     dwdm = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"单位编码")
#     yysj = models.DateField(blank=True, null=True, verbose_name=u"预约时间")
#     yyzh = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"预约组号")
#     yydjr = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"预约登记人")
#     yydjsj = models.DateField(blank=True, null=True, verbose_name=u"预约登记时间")
#     jjzh = models.CharField(max_length=5, blank=True, null=True, verbose_name=u"健检组号")
#     jjlsh = models.FloatField(blank=True, null=True, verbose_name=u"健检流水号")
#     # 状态['0':1:]
#     status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"预约状态")
#     qtdjr = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"前台登记人")
#     qtdjsj = models.DateField(blank=True, null=True, verbose_name=u"前台登记时间")
#     tjsj = models.DateField(blank=True, null=True, verbose_name=u"体检时间")
#     tjzzsj = models.DateField(blank=True, null=True, verbose_name=u"体检终止时间")
#     # 电话通知:1是0否
#     tzf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"停止否")
#     dwjzf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"团体体检否")
#     member_type = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"会员类型")
#     yydhtzr = models.CharField(max_length=25, blank=True, null=True, verbose_name=u"预约电话通知人")
#     # 作为是否当天拿报告单（用)
#     yyth = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"预约电话")
#     zyf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"数据转移否")
#     # 报告单方式（1：自取 2：邮寄 3：送达）
#     jjch = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"报告单方式")
#     print_time = models.DateField(blank=True, null=True, verbose_name=u"打印时间")
#     trans_status = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"传输状态")
#     ywydm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"业务员代码")
#     yqhff = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"一期回访否")
#     erqhff = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"二期回访否")
#     sqhff = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"三期回访否")
#     tcbl = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True, verbose_name=u"VID")
#     dwyyid = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"单位预约ID")
#     cust_name = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"姓名")
#     cust_xb = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"性别")
#     cust_csrq = models.DateField(blank=True, null=True, verbose_name=u"出生日期")
#     temp_bz = models.CharField(max_length=3000, blank=True, null=True, verbose_name=u"临时备注")
#     cust_zy = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"职业")
#     cust_gzhy = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"工作行业")
#     zzys = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"咨询医生")
#     zzhs = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"ZZHS")
#     in_floor = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"制定进入某一层")
#     gzhy_dm = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"工作行业代码")
#     bz_fgs = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注-分公司")
#     bz_bm1 = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注-部门1")
#     bz_bm2 = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注-部门2")
#     bz_ygh = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注-员工号")
#     bz_sfzhm = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注-身份证号码")
#     bz_a = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注-A")
#     bz_b = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注-B")
#     bz_c = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注-C")
#     bz_xj = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"备注-XJ")
#     bz_gz = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"备注-GZ")
#     bz_lpk = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"备注-LQK")
#
#     class Meta:
#         managed = False
#         db_table = 'jj_yyqkb'
#         verbose_name = u"客人预约情况表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 客人检查项目表
# class JjJcmxb(models.Model):
#     vid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"VID")
#     cid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"健检号")
#     groupid = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"组号")
#     groupname = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"组名")
#     item_id = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"项目代码")
#     item_name = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"项目名称")
#     item_ename = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"英文名称")
#     price = models.FloatField(blank=True, null=True, verbose_name=u"价格")
#     unit = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"单位")
#     standard = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"规格 ")
#     begtime = models.DateField(blank=True, null=True, verbose_name=u"开始时间")
#     endtime = models.DateField(blank=True, null=True, verbose_name=u"结束时间")
#     checkoper = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"检查状态")
#     status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"状态")
#     checkdept = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"checkdept")
#     audit_oper = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"audit_oper")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     item_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"项目价格")
#     group_en = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"group_en")
#     group_ft = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"group_ft")
#     item_en = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"item_en")
#     item_ft = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"item_ft")
#     add_number = models.IntegerField(blank=True, null=True, verbose_name=u"add_number")
#     check_opername = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"check_opername")
#     sort_time = models.DateField(blank=True, null=True, verbose_name=u"sort_time")
#     init_price = models.IntegerField(blank=True, null=True, verbose_name=u"init_price")
#
#     class Meta:
#         managed = False
#         db_table = 'jj_jcmxb'
#         verbose_name = u"客人检查项目表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 客人检验项目表
# class LisSampleOrder(models.Model):
#     cid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"健检号")
#     vid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"VID")
#     sampleid = models.CharField(max_length=18, blank=True, null=True, verbose_name=u"样本号")
#     send_to_group = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"发送到组")
#     groupid = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"组号")
#     groupname = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"组名")
#     quatity_of_sample = models.IntegerField(blank=True, null=True, verbose_name=u"样本量")
#     sample_send_time = models.DateField(blank=True, null=True, verbose_name=u"样本发送时间")
#     who_sampling = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"who_sampling")
#     sample_send_dept = models.CharField(max_length=4, blank=True, null=True, verbose_name=u"样本发送科室")
#     sample_receive_time = models.DateField(blank=True, null=True, verbose_name=u"样本接受时间")
#     who_receive = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"接受者")
#     rec_qualified = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"不合格原因")
#     apparatusid = models.CharField(max_length=4, blank=True, null=True, verbose_name=u"设备号")
#     labsequenceno = models.IntegerField(blank=True, null=True, verbose_name=u"检验流水号")
#     extappratus = models.CharField(max_length=4, blank=True, null=True, verbose_name=u"设备扩展编号")
#     expsequence = models.IntegerField(blank=True, null=True, verbose_name=u"扩展流水号")
#     completetime = models.DateField(blank=True, null=True, verbose_name=u"检验完成时间")
#     completeoperator = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"检验人")
#     checktime = models.DateField(blank=True, null=True, verbose_name=u"检查时间")
#     checkoperator = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"检查人")
#     status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"状态")
#     xm = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"姓名")
#     coll_operator = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"coll_operator")
#     coll_time = models.DateField(blank=True, null=True, verbose_name=u"coll_time")
#     sample_type_id = models.CharField(max_length=4, blank=True, null=True, verbose_name=u"样本类型编号")
#     sfgroupid = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"SF组号")
#     jyid = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"jyid")
#     djxhsj = models.DateField(blank=True, null=True, verbose_name=u"djxhsj")
#     djxhry = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"djxhry")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     sample_name = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"样本-名称")
#     sample_xb = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"状态-性别")
#     sample_csrq = models.DateField(blank=True, null=True, verbose_name=u"样本-出生日期")
#     sample_yysj = models.DateField(blank=True, null=True, verbose_name=u"样本-预约时间")
#     item_en = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"项目名称")
#     item_ft = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"item_ft")
#     add_number = models.IntegerField(blank=True, null=True, verbose_name=u"add_number")
#     complete_opername = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"complete_opername")
#     red_green = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"red_green")
#
#     class Meta:
#         managed = False
#         db_table = 'lis_sample_order'
#         verbose_name = u"客人检验项目表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 客人检验结果表
# class LisTestResult(models.Model):
#     cid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"健检号")
#     vid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"VID")
#     sampleid = models.CharField(max_length=18, blank=True, null=True, verbose_name=u"样本号")
#     apparatusid = models.CharField(max_length=4, blank=True, null=True, verbose_name=u"设备号")
#     labsequenceno = models.IntegerField(blank=True, null=True, verbose_name=u"检验流水号")
#     testitem_id = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"检验项目编号")
#     testitem_name_e = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"检验项目英文名称")
#     testitem_name_c = models.CharField(max_length=150, blank=True, null=True, verbose_name=u"检验项目中文名称")
#     testitem_short = models.CharField(max_length=8, blank=True, null=True, verbose_name=u"检验项目简称")
#     results = models.CharField(max_length=400, blank=True, null=True, verbose_name=u"检验结果")
#     unit = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"单位")
#     flag_log_filter = models.NullBooleanField(verbose_name=u"flag_log_filter")
#     rec_log_filter = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"rec_log_filter")
#     flag_qc_filter = models.NullBooleanField(verbose_name=u"flag_qc_filter")
#     rec_qc_filter = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"rec_qc_filter")
#     flag_redo = models.NullBooleanField(verbose_name=u"flag_redo")
#     rec_redo = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"rec_redo")
#     flag_do_more = models.NullBooleanField(verbose_name=u"flag_do_more")
#     rec_do_more = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"rec_do_more")
#     normal_l = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"正常低值")
#     normal_h = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"正常高值")
#     dlms = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True, verbose_name=u"定量描述")
#     sxh = models.IntegerField(blank=True, null=True, verbose_name=u"顺序号")
#     # 0：不能区分或不用区分 1：偏低 2：正常 3：偏高
#     abnormal = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"是否区分")
#     xh = models.IntegerField(blank=True, null=True, verbose_name=u"检查顺序号")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     testitem_ft = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"testitem_ft")
#     bz = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"备注")
#     czsj = models.DateField(blank=True, null=True, verbose_name=u"操作时间")
#
#     class Meta:
#         managed = False
#         db_table = 'lis_test_result'
#         verbose_name = u"客人检验结果表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 外送表
# class JjWsResults(models.Model):
#     vid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"VID")
#     item_id = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"项目编号")
#     xm = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"姓名")
#     xb = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"性别")
#     csrq = models.DateField(blank=True, null=True, verbose_name=u"出生日期")
#     status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"状态")
#     create_date = models.DateField(blank=True, null=True, verbose_name=u"创建时间")
#     create_oper = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"创建人")
#     send_date = models.DateField(blank=True, null=True, verbose_name=u"外送时间")
#     send_oper = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"外送人员")
#     field_results = models.CharField(max_length=1000, blank=True, null=True, verbose_name=u"检查结果")
#     audit_date = models.DateField(blank=True, null=True, verbose_name=u"审核日期")
#     audit_oper = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"审核人员")
#     audit_opername = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"审核人员姓名")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"数据时间")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#
#     class Meta:
#         managed = False
#         db_table = 'jj_ws_results'
#         verbose_name = u"外送表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 健康建议书
#
# # 客人小贴士表
# class JjResultXts2(models.Model):
#     vid = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"VID")
#     item_id = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"项目编号")
#     sxh = models.IntegerField(blank=True, null=True, verbose_name=u"顺序号")
#     cid = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"健检号")
#     xm = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"姓名")
#     xb = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"性别")
#     csrq = models.DateField(blank=True, null=True, verbose_name=u"出生日期")
#     nr1 = models.CharField(max_length=2000, blank=True, null=True, verbose_name=u"nr1")
#     nr2 = models.CharField(max_length=2000, blank=True, null=True, verbose_name=u"nr2")
#     nr3 = models.CharField(max_length=2000, blank=True, null=True, verbose_name=u"nr3")
#     nr4 = models.CharField(max_length=2000, blank=True, null=True, verbose_name=u"nr4")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"数据时间")
#     item_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"项目名称")
#     nr5 = models.CharField(max_length=2000, blank=True, null=True, verbose_name=u"nr5")
#     column_height = models.IntegerField(blank=True, null=True, verbose_name=u"column_height")
#     in_factory = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"in_factory")
#     nr6 = models.CharField(max_length=2000, blank=True, null=True, verbose_name=u"nr6")
#     nr7 = models.CharField(max_length=2000, blank=True, null=True, verbose_name=u"nr7")
#
#     class Meta:
#         managed = False
#         db_table = 'jj_result_xts_2'
#         verbose_name = u"客人小贴士表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 收费明细表
# class JjSfmxb(models.Model):
#     sfmxid = models.CharField(max_length=14, blank=True, null=True, verbose_name=u"收费编码")
#     vid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"VID")
#     cid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"健检号")
#     groupid = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"组号")
#     groupname = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"组名")
#     price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=u"价格")
#     unit = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"单位")
#     standard = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"规格")
#     jzf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"结账否")
#     jzdhm = models.CharField(max_length=14, blank=True, null=True, verbose_name=u"结账单号码")
#     oldprice = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"原价")
#     jxf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"加项否")
#     status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"状态")
#     user_id = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"用户ID")
#     member_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True,
#                                        verbose_name=u"member_price")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     sf_ywydm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"sf_ywydm")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"数据时间")
#
#     class Meta:
#         managed = False
#         db_table = 'jj_sfmxb'
#         verbose_name = u"收费明细表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 结账情况表
# class JjJzqkb(models.Model):
#     vid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"VID")
#     cid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"健检号")
#     jzdhm = models.CharField(max_length=14, blank=True, null=True, verbose_name=u"结账单号码")
#     jzfs = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"结账方式")
#     bzbl = models.FloatField(blank=True, null=True, verbose_name=u"bzbl")
#     fphm = models.CharField(max_length=15, blank=True, null=True, verbose_name=u"发票号码")
#     jzzje = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, verbose_name=u"结账总金额")
#     fpje = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, verbose_name=u"发票金额")
#     jzrdm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"结账人代码")
#     jzsj = models.DateField(blank=True, null=True, verbose_name=u"结账时间")
#     status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"状态")
#     qxrdm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"取消人代码")
#     qxsj = models.DateField(blank=True, null=True, verbose_name=u"取消时间")
#     xjzdhm = models.CharField(max_length=14, blank=True, null=True, verbose_name=u"新结账单代码")
#     bz = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"备注")
#     sfcd = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"是否重打")
#     xfphm = models.CharField(max_length=15, blank=True, null=True, verbose_name=u"新发票号码")
#     cdrdm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"重打人代码")
#     cdsj = models.DateField(blank=True, null=True, verbose_name=u"重打时间")
#     jzfmc = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"结账方名称")
#     jzlx = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"结账类型")
#     kjy = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"账户结余")
#     fpqx = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"发票去向")
#     gcfpry = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"给出发票的人员")
#     tczje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"tczje")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#
#     class Meta:
#         managed = False
#         db_table = 'jj_jzqkb'
#         verbose_name = u"结账情况表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 结账付款明细表
# class JjJzFklist(models.Model):
#     jzdhm = models.CharField(max_length=14, blank=True, null=True, verbose_name=u"结账单号码")
#     xh = models.IntegerField(blank=True, null=True, verbose_name=u"序号")
#     vid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"VID")
#     fkfs = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"付款方式")
#     fkfsje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"付款方式金额")
#     hl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"汇率")
#     zsje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"折算金额")
#     bz = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"备注")
#     ye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"余额")
#     zscs = models.IntegerField(blank=True, null=True, verbose_name=u"折算次数")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     ls_jzsj = models.DateField(blank=True, null=True, verbose_name=u"流水-结账时间")
#     dqjzr = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"单期结账人")
#     other_fkfs = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"其他付款方式")
#
#     class Meta:
#         managed = False
#         db_table = 'jj_jz_fklist'
#         verbose_name = u"结账付款明细表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.jzdhm
#
#
# # 客人体检检查结果表
# class JjCommJcResult(models.Model):
#     item_id = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"项目代码")
#     vid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"VID")
#     table_id = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"模板ID号")
#     field_comment = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"检查名称")
#     field_results = models.CharField(max_length=3500, blank=True, null=True, verbose_name=u"检查结果")
#     zcz_xx = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"正常值下限")
#     zcz_sx = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"正常值上限")
#     dw = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"单位")
#     in_results = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"进入诊断结论否")
#     column_height = models.IntegerField(blank=True, null=True, verbose_name=u"列高度")
#     column_width = models.IntegerField(blank=True, null=True, verbose_name=u"列宽度")
#     # 列的数据类型(1:字符串型 2：数字型 3：日期型 )
#     column_data_type = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"列数据类型")
#     column_data_format = models.CharField(max_length=15, blank=True, null=True, verbose_name=u"数据格式")
#     column_sxh = models.IntegerField(blank=True, null=True, verbose_name=u"列顺序号")
#     trans_status = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"传输状态")
#     init_results = models.CharField(max_length=500, blank=True, null=True, verbose_name=u"初始值")
#     sf_yx = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"是否阳性")
#     column_type = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     cid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"健检号")
#     field_name = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"字段名称")
#     is_print = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"是否打印")
#     print_height = models.BigIntegerField(blank=True, null=True, verbose_name=u"打印高度")
#     table_name = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"表的名字")
#     table_sxh = models.IntegerField(blank=True, null=True, verbose_name=u"表顺序号")
#     in_factroy = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"in_factroy")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"数据时间")
#
#     class Meta:
#         managed = False
#         db_table = 'jj_comm_jc_result'
#         verbose_name = u"客人体检检查结果表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 检查结果图片表
# class JjResultPicture(models.Model):
#     vid = models.CharField(max_length=12, blank=True, null=True)
#     cid = models.CharField(max_length=12, blank=True, null=True)
#     xm = models.CharField(max_length=20, blank=True, null=True)
#     xb = models.CharField(max_length=20, blank=True, null=True)
#     csrq = models.DateField(blank=True, null=True)
#     item_id = models.CharField(max_length=6, blank=True, null=True)
#     item_name = models.CharField(max_length=60, blank=True, null=True)
#     pic_id = models.IntegerField(blank=True, null=True)
#     trans_status = models.CharField(max_length=1, blank=True, null=True)
#     bmp_path = models.CharField(max_length=100, blank=True, null=True)
#     file_name1 = models.CharField(max_length=100, blank=True, null=True)
#     file_name2 = models.CharField(max_length=100, blank=True, null=True)
#     file_name3 = models.CharField(max_length=100, blank=True, null=True)
#     file_name4 = models.CharField(max_length=100, blank=True, null=True)
#     file_name5 = models.CharField(max_length=100, blank=True, null=True)
#     file_name6 = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'jj_result_picture'
#         verbose_name = u"客人体检检查结果表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 网上办公人员列表
# class BasOperatorInfor(models.Model):
#     aid_code = models.CharField(max_length=20, blank=True, null=True)
#     user_id = models.CharField(max_length=6, blank=True, null=True)
#     username = models.CharField(max_length=10, blank=True, null=True)
#     password = models.CharField(max_length=6, blank=True, null=True)
#     ywyf = models.CharField(max_length=1, blank=True, null=True)
#     lrsj = models.DateField(blank=True, null=True)
#     op_datetime = models.DateField(blank=True, null=True)
#     bzpym = models.CharField(max_length=8, blank=True, null=True)
#     in_factory = models.CharField(max_length=20, blank=True, null=True)
#     sjdm = models.CharField(max_length=20, blank=True, null=True)
#     jb = models.IntegerField(blank=True, null=True)
#     yzjf = models.CharField(max_length=1, blank=True, null=True)
#     rylb = models.CharField(max_length=20, blank=True, null=True)
#     yxf = models.CharField(max_length=1, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bas_operator_infor'
#         verbose_name = u"客人体检检查结果表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 潜在单位列表
# class BasEntInfoPre(models.Model):
#     dwdm = models.CharField(max_length=12, blank=True, null=True)
#     dwmc = models.CharField(max_length=60, blank=True, null=True)
#     dwdz = models.CharField(max_length=60, blank=True, null=True)
#     yzbm = models.CharField(max_length=6, blank=True, null=True)
#     lxr = models.CharField(max_length=10, blank=True, null=True)
#     lxdh = models.CharField(max_length=30, blank=True, null=True)
#     yddh = models.CharField(max_length=11, blank=True, null=True)
#     email = models.CharField(max_length=30, blank=True, null=True)
#     dwcz = models.CharField(max_length=20, blank=True, null=True)
#     fzr = models.CharField(max_length=10, blank=True, null=True)
#     djr = models.CharField(max_length=6, blank=True, null=True)
#     djsj = models.DateField(blank=True, null=True)
#     op_datetime = models.DateField(blank=True, null=True)
#     bzpym = models.CharField(max_length=8, blank=True, null=True)
#     ywydm = models.CharField(max_length=6, blank=True, null=True)
#     khly = models.CharField(max_length=6, blank=True, null=True)
#     status = models.CharField(max_length=1, blank=True, null=True)
#     dwrs = models.IntegerField(blank=True, null=True)
#     xgr = models.CharField(max_length=6, blank=True, null=True)
#     sjdwdm = models.CharField(max_length=12, blank=True, null=True)
#     bz = models.CharField(max_length=255, blank=True, null=True)
#     trans_status = models.CharField(max_length=1, blank=True, null=True)
#     gzhy_dm = models.CharField(max_length=20, blank=True, null=True)
#     region_dm = models.CharField(max_length=30, blank=True, null=True)
#     dw_password = models.CharField(max_length=20, blank=True, null=True)
#     in_factory = models.CharField(max_length=30, blank=True, null=True)
#     gjz1 = models.CharField(max_length=200, blank=True, null=True)
#     gjz2 = models.CharField(max_length=200, blank=True, null=True)
#     gjz3 = models.CharField(max_length=200, blank=True, null=True)
#     bz1 = models.CharField(max_length=200, blank=True, null=True)
#     bz2 = models.CharField(max_length=200, blank=True, null=True)
#     bz3 = models.CharField(max_length=200, blank=True, null=True)
#     bz4 = models.CharField(max_length=200, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bas_ent_info_pre'
#         verbose_name = u"客人体检检查结果表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 单位帐户明细表
# class AccCustAccountList(models.Model):
#     billcode = models.CharField(max_length=14, blank=True, null=True, verbose_name=u"单号")
#     cid = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"健检号")
#     xm = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"姓名")
#     xb = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"性别")
#     # 操作类型'01','交纳预交款', '02','结帐冲减预交款', '03', '冲帐还原预交款','04', '挂帐', '05', '冲帐挂帐还原'
#     czlx = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"操作类型")
#     zjbz = models.IntegerField(blank=True, null=True, verbose_name=u"增减标记")
#     fkfs = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"付款方式")
#     jnje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"缴纳金额")
#     hl = models.IntegerField(blank=True, null=True, verbose_name=u"汇率")
#     czje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"操作金额")
#     ye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"账户余额")
#     czy = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"操作员")
#     czsj = models.DateField(blank=True, null=True, verbose_name=u"操作时间")
#     fphm = models.CharField(max_length=14, blank=True, null=True, verbose_name=u"发票号码")
#     dydh = models.CharField(max_length=14, blank=True, null=True, verbose_name=u"对应单号")
#     dyf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"对应法")
#     dyr = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"对应人")
#     dysj = models.DateField(blank=True, null=True, verbose_name=u"对应时间")
#     # 单位或者个人（1：个人 2：单位）
#     dw_gr = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"单位或个人")
#     lb = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"类别")
#     sjje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"姓名")
#     ywydm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"业务员代码")
#     khly = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"客户来源")
#     # 与付款方式保持一致00：预交款 04：合约单位等 、员工挂帐、单位内部挂帐等 （这里面不包含礼品卡消费情况)
#     deal_type = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"付款方式")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     other_bl = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True, verbose_name=u"其他比例")
#     in_factory = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"in_factory")
#
#     class Meta:
#         managed = False
#         db_table = 'acc_cust_account_list'
#         verbose_name = u"AccCustAccountList"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.billcode
#
#
# # 客户来源代码表
# class CrmKhlydmb(models.Model):
#     dm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"代码")
#     mc = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"名称")
#     sjdm = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"上级代码")
#     bzpym = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"标准拼音码")
#     jb = models.IntegerField(blank=True, null=True, verbose_name=u"级别")
#     yzjf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"有子集否")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"数据时间")
#     tcfs = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"套餐方式")
#
#     class Meta:
#         managed = False
#         db_table = 'crm_khlydmb'
#         verbose_name = u"客户来源代码表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.mc
#
#
# # 物料表
# class StMaterial(models.Model):
#     aid_code = models.CharField(max_length=15, blank=True, null=True, verbose_name=u"辅助编码")
#     dm = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"材料代码")
#     mc = models.CharField(max_length=80, blank=True, null=True, verbose_name=u"材料名称")
#     gg = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"材料规格")
#     dj = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True, verbose_name=u"材料单价")
#     dw = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"单位")
#     sjdm = models.CharField(max_length=15, blank=True, null=True, verbose_name=u"上级代码")
#     jb = models.IntegerField(blank=True, null=True, verbose_name=u"级别")
#     yzjf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"有子集否")
#     yxf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"有效否")
#     bzpym = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"标准拼音码")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"数据时间")
#     add_jx = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"add_jx")
#     add_jl = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"add_jl")
#     add_fydw = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"add_fydw")
#     st_bz1 = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"st_bz1")
#     st_bz2 = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"st_bz2")
#
#     class Meta:
#         managed = False
#         db_table = 'st_material'
#         verbose_name = u"物料表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.aid_code
#
#
# # 仓库明细表
# class StStock(models.Model):
#     ksdm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"科室代码")
#     dm = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"代码")
#     scph = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"scph")
#     zsl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"zsl")
#     dj = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True, verbose_name=u"单价")
#     czsj = models.DateField(blank=True, null=True, verbose_name=u"操作时间")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#
#     class Meta:
#         managed = False
#         db_table = 'st_stock'
#         verbose_name = u"仓库明细表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.ksdm
#
#
# # 进销主表
# class StBill(models.Model):
#     dh = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"单号")
#     ksdm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"科室代码")
#     ywlx = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"ywlx")
#     dyksdm = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"打印科室代码")
#     lrry = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"录入人员")
#     lrsj = models.DateField(blank=True, null=True, verbose_name=u"录入日期")
#     shry = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"审核人员")
#     shsj = models.DateField(blank=True, null=True, verbose_name=u"审核时间")
#     wcbz = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"完成备注")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     slr_oper = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"申领人")
#     slr_opername = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"申领人名称")
#     dyksmc = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"打印科室名称")
#     lrry_name = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"录入人员-姓名")
#     shry_name = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"审核人员-姓名")
#
#     class Meta:
#         managed = False
#         db_table = 'st_bill'
#         verbose_name = u"进销主表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.dh
#
#
# # 进销明细表
# class StBills(models.Model):
#     dh = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"单号")
#     ksdm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"科室代码")
#     ywlx = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"ywlx")
#     dm = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"代码")
#     mc = models.CharField(max_length=80, blank=True, null=True, verbose_name=u"名称")
#     gg = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"规格")
#     scph = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"scph")
#     clsl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"clsl")
#     sjsl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"sjsl")
#     kysl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"kysl")
#     kysl = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True, verbose_name=u"kysl")
#     lsj = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True, verbose_name=u"lsj")
#     dw = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"单位")
#     kcsl = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=u"kcsl")
#     bsbfyy = models.CharField(max_length=3, blank=True, null=True, verbose_name=u"bsbfyy")
#     newlsj = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True, verbose_name=u"newlsj")
#     trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
#     sccj = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"sccj")
#     sxq = models.DateField(blank=True, null=True, verbose_name=u"sxq")
#
#     class Meta:
#         managed = False
#         db_table = 'st_bills'
#         verbose_name = u"进销明细表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.dh
#
#
# # 投诉基本信息表
# class CrmTsjbxx(models.Model):
#     dh = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"单号")
#     xm = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"姓名")
#     cid = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"健检号")
#     zt = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"")
#     tsrq = models.DateField(blank=True, null=True, verbose_name=u"投诉日期")
#     tsdx = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"投诉对象")
#     tsnr = models.CharField(max_length=400, blank=True, null=True, verbose_name=u"投诉内容")
#     lry = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"录入员")
#     lryxm = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"录入人姓名")
#     clr = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"处理人")
#     clrxm = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"处理人姓名")
#     cljg = models.CharField(max_length=400, blank=True, null=True, verbose_name=u"处理结果")
#     djzt = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"登记状态")
#     clsj = models.DateField(blank=True, null=True, verbose_name=u"处理时间")
#     tsrlxfs = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"投诉人联系方式")
#     shr = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"售后人")
#     shsj = models.DateField(blank=True, null=True, verbose_name=u"审核时间")
#     tsbm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"投诉编码")
#     tslb = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"投诉类别")
#     op_datetime = models.DateField(blank=True, null=True, verbose_name=u"数据时间")
#     trans_status = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"传输状态")
#
#     class Meta:
#         managed = False
#         db_table = 'crm_tsjbxx'
#         verbose_name = u"投诉基本信息表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.dh
#
#
# # 体检单位列表
# class SaleTjdwList(models.Model):
#     billcode = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"单号")
#     dwdm = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"单位代码")
#     dwmc = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"单位名称")
#     ywydm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"业务员代码")
#     lxr = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"联系人")
#     lxdh = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"联系电话")
#     lxdz = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"联系地址")
#     email = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"邮箱")
#     djsj = models.DateField(blank=True, null=True, verbose_name=u"登记时间")
#     jgxx = models.CharField(max_length=3000, blank=True, null=True, verbose_name=u"价格信息")
#     sfjzsj = models.DateField(blank=True, null=True, verbose_name=u"收费结账时间")
#     xsyq = models.CharField(max_length=3000, blank=True, null=True, verbose_name=u"销售延期")
#     ywy_zg = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"业务员主管")
#     ywy_zg_shsj = models.DateField(blank=True, null=True, verbose_name=u"业务员主管审核时间")
#     zrhs = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"主任护师")
#     zrys = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"主任医师")
#     ywb_zg_shsj = models.DateField(blank=True, null=True, verbose_name=u"业务部主管审核时间")
#     zxfw = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"zxfw")
#     yj = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"业绩")
#     lcctf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"")
#     tdhf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"")
#     xsbyj = models.CharField(max_length=3000, blank=True, null=True, verbose_name=u"")
#     xsbdjr = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"")
#     xsbdjsj = models.DateField(blank=True, null=True, verbose_name=u"")
#     lcksyj = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"")
#     lcdjr = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"")
#     lcdjsj = models.DateField(blank=True, null=True, verbose_name=u"")
#     wctjsj = models.DateField(blank=True, null=True, verbose_name=u"")
#     wctjrs = models.IntegerField(blank=True, null=True, verbose_name=u"")
#     wcbgrs = models.IntegerField(blank=True, null=True, verbose_name=u"")
#     zxwcsj = models.DateField(blank=True, null=True, verbose_name=u"")
#     jzwcsj = models.DateField(blank=True, null=True, verbose_name=u"")
#     zj_zrr = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"")
#     zj_qzsj = models.DateField(blank=True, null=True, verbose_name=u"")
#     zj_bz = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"")
#     status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"状态")
#     status1 = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"状态1")
#     status2 = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"状态2")
#     status3 = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"状态3")
#     status4 = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"状态4")
#     status5 = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"状态5")
#     ywb_zg = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"业务部主管")
#     zlpg_shry = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"")
#     zlpg_shsj = models.DateField(blank=True, null=True, verbose_name=u"")
#     zjbz_zrr = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"")
#     zjbz_qzsj = models.DateField(blank=True, null=True, verbose_name=u"")
#     htsj = models.DateField(blank=True, null=True, verbose_name=u"合同时间")
#     qbgdfs = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"")
#     fkfs = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"付款方式")
#     read_ornot = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"是否读取")
#
#     class Meta:
#         managed = False
#         db_table = 'sale_tjdw_list'
#         verbose_name = u"体检单位列表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.billcode
#
#
# # 凭证卡表
#
# # 凭证卡操作日志
#
# # 单位特别提醒
# class SaleTjdwTbtx(models.Model):
#     dwdm = models.CharField(max_length=30, blank=True, null=True)
#     billcode = models.CharField(max_length=60, blank=True, null=True)
#     userobject = models.CharField(max_length=100, blank=True, null=True)
#     # id = models.CharField(max_length=100, blank=True, null=True)
#     kssj = models.DateField(blank=True, null=True)
#     jzsj = models.DateField(blank=True, null=True)
#     nr = models.CharField(max_length=500, blank=True, null=True)
#     status = models.CharField(max_length=1, blank=True, null=True)
#     trans_status = models.CharField(max_length=1, blank=True, null=True)
#     op_datetime = models.DateField(blank=True, null=True)
#     in_factory = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sale_tjdw_tbtx'
#         verbose_name = u"单位特别提醒"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.dwdm
#
#
# # EHO 表
# class SaleEhoList(models.Model):
#     dwdm = models.CharField(max_length=30, blank=True, null=True)
#     ygh = models.CharField(max_length=30, blank=True, null=True)
#     xm = models.CharField(max_length=50, blank=True, null=True)
#     xb = models.CharField(max_length=10, blank=True, null=True)
#     hyzk = models.CharField(max_length=10, blank=True, null=True)
#     csrq = models.DateField(blank=True, null=True)
#     sfzhm = models.CharField(max_length=30, blank=True, null=True)
#     fgs = models.CharField(max_length=100, blank=True, null=True)
#     bm1 = models.CharField(max_length=100, blank=True, null=True)
#     bm2 = models.CharField(max_length=100, blank=True, null=True)
#     lxdh = models.CharField(max_length=60, blank=True, null=True)
#     yyrq = models.DateField(blank=True, null=True)
#     groupid = models.CharField(max_length=30, blank=True, null=True)
#     in_factory = models.CharField(max_length=30, blank=True, null=True)
#     op_datetime = models.DateField(blank=True, null=True)
#     add_item = models.CharField(max_length=1000, blank=True, null=True)
#     bz = models.CharField(max_length=100, blank=True, null=True)
#     email = models.CharField(max_length=100, blank=True, null=True)
#     lxdz = models.CharField(max_length=200, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sale_eho_list'
#         verbose_name = u"EHO 表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.dwdm
#
#
# # 网络预约加项
#
#
# # 中医体质辨识
# class ZyTzpsResults(models.Model):
#     cid = models.CharField(max_length=30, blank=True, null=True)
#     vid = models.CharField(max_length=30, blank=True, null=True)
#     zy_1 = models.CharField(max_length=10, blank=True, null=True)
#     zy_2 = models.CharField(max_length=10, blank=True, null=True)
#     zy_3 = models.CharField(max_length=10, blank=True, null=True)
#     zy_4 = models.CharField(max_length=10, blank=True, null=True)
#     zy_5 = models.CharField(max_length=10, blank=True, null=True)
#     zy_6 = models.CharField(max_length=10, blank=True, null=True)
#     zy_7 = models.CharField(max_length=10, blank=True, null=True)
#     zy_8 = models.CharField(max_length=10, blank=True, null=True)
#     zy_9 = models.CharField(max_length=10, blank=True, null=True)
#     zy_10 = models.CharField(max_length=10, blank=True, null=True)
#     zy_11 = models.CharField(max_length=10, blank=True, null=True)
#     zy_12 = models.CharField(max_length=10, blank=True, null=True)
#     zy_13 = models.CharField(max_length=10, blank=True, null=True)
#     zy_14 = models.CharField(max_length=10, blank=True, null=True)
#     zy_15 = models.CharField(max_length=10, blank=True, null=True)
#     zy_16 = models.CharField(max_length=10, blank=True, null=True)
#     zy_17 = models.CharField(max_length=10, blank=True, null=True)
#     zy_18 = models.CharField(max_length=10, blank=True, null=True)
#     zy_19 = models.CharField(max_length=10, blank=True, null=True)
#     zy_20 = models.CharField(max_length=10, blank=True, null=True)
#     zy_21 = models.CharField(max_length=10, blank=True, null=True)
#     zy_22 = models.CharField(max_length=10, blank=True, null=True)
#     zy_23 = models.CharField(max_length=10, blank=True, null=True)
#     zy_24 = models.CharField(max_length=10, blank=True, null=True)
#     zy_25 = models.CharField(max_length=10, blank=True, null=True)
#     zy_26 = models.CharField(max_length=10, blank=True, null=True)
#     zy_27 = models.CharField(max_length=10, blank=True, null=True)
#     zy_28 = models.CharField(max_length=10, blank=True, null=True)
#     zy_29 = models.CharField(max_length=10, blank=True, null=True)
#     zy_30 = models.CharField(max_length=10, blank=True, null=True)
#     zy_31 = models.CharField(max_length=10, blank=True, null=True)
#     zy_32 = models.CharField(max_length=10, blank=True, null=True)
#     zy_33 = models.CharField(max_length=10, blank=True, null=True)
#     zy_34 = models.CharField(max_length=10, blank=True, null=True)
#     zy_35 = models.CharField(max_length=10, blank=True, null=True)
#     zy_36 = models.CharField(max_length=10, blank=True, null=True)
#     zy_37 = models.CharField(max_length=10, blank=True, null=True)
#     zy_38 = models.CharField(max_length=10, blank=True, null=True)
#     zy_39 = models.CharField(max_length=10, blank=True, null=True)
#     zy_40 = models.CharField(max_length=10, blank=True, null=True)
#     zy_41 = models.CharField(max_length=10, blank=True, null=True)
#     zy_42 = models.CharField(max_length=10, blank=True, null=True)
#     zy_43 = models.CharField(max_length=10, blank=True, null=True)
#     zy_44 = models.CharField(max_length=10, blank=True, null=True)
#     zy_45 = models.CharField(max_length=10, blank=True, null=True)
#     zy_46 = models.CharField(max_length=10, blank=True, null=True)
#     zy_47 = models.CharField(max_length=10, blank=True, null=True)
#     zy_48 = models.CharField(max_length=10, blank=True, null=True)
#     zy_49 = models.CharField(max_length=10, blank=True, null=True)
#     zy_50 = models.CharField(max_length=10, blank=True, null=True)
#     zy_51 = models.CharField(max_length=10, blank=True, null=True)
#     zy_52 = models.CharField(max_length=10, blank=True, null=True)
#     zy_53 = models.CharField(max_length=10, blank=True, null=True)
#     zy_54 = models.CharField(max_length=10, blank=True, null=True)
#     zy_55 = models.CharField(max_length=10, blank=True, null=True)
#     zy_56 = models.CharField(max_length=10, blank=True, null=True)
#     sz_1 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
#     sz_2 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
#     sz_3 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
#     sz_4 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
#     sz_5 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
#     sz_6 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
#     sz_7 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
#     sz_8 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
#     zycp_results = models.CharField(max_length=500, blank=True, null=True)
#     trans_status = models.CharField(max_length=1, blank=True, null=True)
#     op_datetime = models.DateField(blank=True, null=True)
#     lr_oper = models.CharField(max_length=30, blank=True, null=True)
#     lr_opername = models.CharField(max_length=60, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'zy_tzps_results'
#         verbose_name = u"中医体质辨识"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 重大阳性表
# class CustZdyxList(models.Model):
#     cid = models.CharField(max_length=30, blank=True, null=True)
#     vid = models.CharField(max_length=30, blank=True, null=True)
#     xm = models.CharField(max_length=50, blank=True, null=True)
#     xb = models.CharField(max_length=10, blank=True, null=True)
#     csrq = models.DateField(blank=True, null=True)
#     dwdm = models.CharField(max_length=30, blank=True, null=True)
#     fgs = models.CharField(max_length=200, blank=True, null=True)
#     bm1 = models.CharField(max_length=200, blank=True, null=True)
#     bm2 = models.CharField(max_length=200, blank=True, null=True)
#     ygh = models.CharField(max_length=100, blank=True, null=True)
#     in_factory = models.CharField(max_length=30, blank=True, null=True)
#     yysj = models.DateField(blank=True, null=True)
#     status = models.CharField(max_length=1, blank=True, null=True)
#     trans_status = models.CharField(max_length=1, blank=True, null=True)
#     op_datetime = models.DateField(blank=True, null=True)
#     oper = models.CharField(max_length=30, blank=True, null=True)
#     opername = models.CharField(max_length=50, blank=True, null=True)
#     zdyx = models.CharField(max_length=800, blank=True, null=True)
#     sfzhm = models.CharField(max_length=60, blank=True, null=True)
#     lxdh = models.CharField(max_length=100, blank=True, null=True)
#     dept_clyj = models.CharField(max_length=500, blank=True, null=True)
#     dept_clry = models.CharField(max_length=50, blank=True, null=True)
#     dept_clsj = models.DateField(blank=True, null=True)
#     hz1_clyj = models.CharField(max_length=500, blank=True, null=True)
#     hz1_clry = models.CharField(max_length=50, blank=True, null=True)
#     hz1_clsj = models.DateField(blank=True, null=True)
#     hz2_clyj = models.CharField(max_length=500, blank=True, null=True)
#     hz2_clry = models.CharField(max_length=50, blank=True, null=True)
#     hz2_clsj = models.DateField(blank=True, null=True)
#     kf_clyj = models.CharField(max_length=500, blank=True, null=True)
#     kf_clry = models.CharField(max_length=50, blank=True, null=True)
#     kf_clsj = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'cust_zdyx_list'
#         verbose_name = u"重大阳性表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 口腔付款表
#
# # 订单跟踪表
#
# # 预约排期表
# class SaleYypqInput(models.Model):
#     bill_code = models.CharField(max_length=12, blank=True, null=True)
#     # id = models.CharField(max_length=20, blank=True, null=True)
#     yyrq = models.DateField(blank=True, null=True)
#     in_factory = models.CharField(max_length=20, blank=True, null=True)
#     pqzh = models.CharField(max_length=20, blank=True, null=True)
#     dwdm = models.CharField(max_length=12, blank=True, null=True)
#     dwmc = models.CharField(max_length=60, blank=True, null=True)
#     pqrs = models.BigIntegerField(blank=True, null=True)
#     bz = models.CharField(max_length=500, blank=True, null=True)
#     status = models.CharField(max_length=1, blank=True, null=True)
#     isselect = models.CharField(max_length=1, blank=True, null=True)
#     op_datetime = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sale_yypq_input'
#         verbose_name = u"预约排期表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.bill_code
#
#
# # 团队要求表
# class SaleTjdwTdyq(models.Model):
#     billcode = models.CharField(max_length=12, blank=True, null=True)
#     tdyq_dm = models.CharField(max_length=20, blank=True, null=True)
#     yqkssj = models.DateField(blank=True, null=True)
#     yqjzsj = models.DateField(blank=True, null=True)
#     status = models.CharField(max_length=1, blank=True, null=True)
#     shr = models.CharField(max_length=6, blank=True, null=True)
#     shsj = models.DateField(blank=True, null=True)
#     bz = models.CharField(max_length=200, blank=True, null=True)
#     cqyxf = models.CharField(max_length=1, blank=True, null=True)
#     op_datetime = models.DateField(blank=True, null=True)
#     dwdm = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sale_tjdw_tdyq'
#         verbose_name = u"团队要求表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.billcode
#
#
# # 散户预约登记表
# class SaleShYy(models.Model):
#     cust_name = models.CharField(max_length=30, blank=True, null=True)
#     company = models.CharField(max_length=60, blank=True, null=True)
#     yysj = models.DateField(blank=True, null=True)
#     cust_sex = models.CharField(max_length=2, blank=True, null=True)
#     bz = models.CharField(max_length=200, blank=True, null=True)
#     djr = models.CharField(max_length=50, blank=True, null=True)
#     djsj = models.DateField(blank=True, null=True)
#     in_factory = models.CharField(max_length=30, blank=True, null=True)
#     dwdm = models.CharField(max_length=30, blank=True, null=True)
#     # id = models.CharField(max_length=50, blank=True, null=True)
#     groupid = models.CharField(max_length=50, blank=True, null=True)
#     csrq = models.DateField(blank=True, null=True)
#     fkfs = models.CharField(max_length=1, blank=True, null=True)
#     jsf = models.CharField(max_length=1, blank=True, null=True)
#     ygh = models.CharField(max_length=30, blank=True, null=True)
#     fgs = models.CharField(max_length=100, blank=True, null=True)
#     bz1 = models.CharField(max_length=50, blank=True, null=True)
#     bz2 = models.CharField(max_length=50, blank=True, null=True)
#     bz3 = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sale_sh_yy'
#         verbose_name = u"散户预约登记表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.cust_name
#
#
# # 单位预约付款方式变更
# class SaleTjdwFkfsChange(models.Model):
#     billcode = models.CharField(max_length=30, blank=True, null=True)
#     dwdm = models.CharField(max_length=30, blank=True, null=True)
#     dwmc = models.CharField(max_length=100, blank=True, null=True)
#     kssj = models.DateField(blank=True, null=True)
#     fkfs = models.CharField(max_length=10, blank=True, null=True)
#     lrry = models.CharField(max_length=20, blank=True, null=True)
#     lrsj = models.DateField(blank=True, null=True)
#     in_factory = models.CharField(max_length=30, blank=True, null=True)
#     status = models.CharField(max_length=1, blank=True, null=True)
#     zfry = models.CharField(max_length=10, blank=True, null=True)
#     zfsj = models.DateField(blank=True, null=True)
#     op_datetime = models.DateField(blank=True, null=True)
#     bz1 = models.CharField(max_length=30, blank=True, null=True)
#     bz2 = models.CharField(max_length=30, blank=True, null=True)
#     bz3 = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sale_tjdw_fkfs_change'
#         verbose_name = u"单位预约付款方式变更"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.billcode
#
#
# # 复合检验建议表
# class JjCustJyMultiJy(models.Model):
#     # id = models.CharField(max_length=100, blank=True, null=True)
#     jybt = models.CharField(max_length=500, blank=True, null=True)
#     jxys = models.CharField(max_length=1000, blank=True, null=True)
#     yyhg = models.CharField(max_length=1000, blank=True, null=True)
#     yxjy = models.CharField(max_length=1000, blank=True, null=True)
#     ycbw = models.CharField(max_length=100, blank=True, null=True)
#     jbnr = models.CharField(max_length=100, blank=True, null=True)
#     sfjb = models.CharField(max_length=100, blank=True, null=True)
#     yxf = models.CharField(max_length=10, blank=True, null=True)
#     djsj = models.DateField(blank=True, null=True)
#     trans_status = models.CharField(max_length=10, blank=True, null=True)
#     item_id_1 = models.CharField(max_length=100, blank=True, null=True)
#     abnormal_1 = models.CharField(max_length=100, blank=True, null=True)
#     item_id_2 = models.CharField(max_length=100, blank=True, null=True)
#     abnormal_2 = models.CharField(max_length=100, blank=True, null=True)
#     item_id_3 = models.CharField(max_length=100, blank=True, null=True)
#     abnormal_3 = models.CharField(max_length=100, blank=True, null=True)
#     item_id_4 = models.CharField(max_length=100, blank=True, null=True)
#     abnormal_4 = models.CharField(max_length=100, blank=True, null=True)
#     item_id_5 = models.CharField(max_length=100, blank=True, null=True)
#     abnormal_5 = models.CharField(max_length=100, blank=True, null=True)
#     item_id_6 = models.CharField(max_length=100, blank=True, null=True)
#     abnormal_6 = models.CharField(max_length=100, blank=True, null=True)
#     item_id_7 = models.CharField(max_length=100, blank=True, null=True)
#     abnormal_7 = models.CharField(max_length=100, blank=True, null=True)
#     item_id_8 = models.CharField(max_length=100, blank=True, null=True)
#     abnormal_8 = models.CharField(max_length=100, blank=True, null=True)
#     item_id_9 = models.CharField(max_length=100, blank=True, null=True)
#     abnormal_9 = models.CharField(max_length=100, blank=True, null=True)
#     item_id_10 = models.CharField(max_length=100, blank=True, null=True)
#     abnormal_10 = models.CharField(max_length=100, blank=True, null=True)
#     item_num = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'jj_cust_jy_multi_jy'
#         verbose_name = u"复合检验建议表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.id
#
#
# # 集团项目指标表
# class LisJtTestItem(models.Model):
#     lb = models.CharField(max_length=50, blank=True, null=True)
#     jt_item_id = models.CharField(max_length=100, blank=True, null=True)
#     jt_item_name = models.CharField(max_length=200, blank=True, null=True)
#     local_item_id = models.CharField(max_length=100, blank=True, null=True)
#     local_item_id_2 = models.CharField(max_length=100, blank=True, null=True)
#     in_factory = models.CharField(max_length=100, blank=True, null=True)
#     trans_status = models.CharField(max_length=10, blank=True, null=True)
#     djsj = models.DateField(blank=True, null=True)
#     op_datetime = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'lis_jt_test_item'
#         verbose_name = u"集团项目指标表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.lb
#
#
# # 检查异常建议表
# class JjCustYcDict2014(models.Model):
#     # id = models.CharField(max_length=100, blank=True, null=True)
#     item_ms_zb = models.CharField(max_length=100, blank=True, null=True)
#     item_id = models.CharField(max_length=100, blank=True, null=True)
#     lb = models.CharField(max_length=100, blank=True, null=True)
#     jybt = models.CharField(max_length=300, blank=True, null=True)
#     jxjs = models.CharField(max_length=1000, blank=True, null=True)
#     yyhg = models.CharField(max_length=1000, blank=True, null=True)
#     yxjy = models.CharField(max_length=1000, blank=True, null=True)
#     trans_status = models.CharField(max_length=10, blank=True, null=True)
#     djsj = models.DateField(blank=True, null=True)
#     yxjg = models.CharField(max_length=100, blank=True, null=True)
#     pg_pd = models.CharField(max_length=100, blank=True, null=True)
#     value_l = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
#     value_h = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
#     yxf = models.CharField(max_length=10, blank=True, null=True)
#     sxh = models.IntegerField(blank=True, null=True)
#     sfmrjy = models.CharField(max_length=10, blank=True, null=True)
#     yxgjz = models.CharField(max_length=500, blank=True, null=True)
#     ycbw_sz = models.CharField(max_length=500, blank=True, null=True)
#     yxnr = models.CharField(max_length=500, blank=True, null=True)
#     bz2 = models.CharField(max_length=500, blank=True, null=True)
#     item_id_a = models.CharField(max_length=100, blank=True, null=True)
#     sfjb = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'jj_cust_yc_dict2014'
#         verbose_name = u"检查异常建议表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.id
#
#
# # 诊断内容表
# class JjCustZdnrResult(models.Model):
#     vid = models.CharField(max_length=12, blank=True, null=True)
#     item_id = models.CharField(max_length=30, blank=True, null=True)
#     item_ms = models.CharField(max_length=30, blank=True, null=True)
#     item_ms_zb = models.CharField(max_length=30, blank=True, null=True)
#     zd_nr = models.CharField(max_length=200, blank=True, null=True)
#     sxh = models.IntegerField(blank=True, null=True)
#     bz1 = models.CharField(max_length=200, blank=True, null=True)
#     bz2 = models.CharField(max_length=100, blank=True, null=True)
#     bz3 = models.CharField(max_length=200, blank=True, null=True)
#     mbnr = models.CharField(max_length=1000, blank=True, null=True)
#     sfjb = models.CharField(max_length=100, blank=True, null=True)
#     jbnb = models.CharField(max_length=200, blank=True, null=True)
#     jybt = models.CharField(max_length=200, blank=True, null=True)
#     yxjs = models.CharField(max_length=1000, blank=True, null=True)
#     yyhg = models.CharField(max_length=1000, blank=True, null=True)
#     yxjy = models.CharField(max_length=1000, blank=True, null=True)
#     lb = models.CharField(max_length=10, blank=True, null=True)
#     trans_status1 = models.CharField(max_length=10, blank=True, null=True)
#     trans_status2 = models.CharField(max_length=10, blank=True, null=True)
#     djsj = models.DateField(blank=True, null=True)
#     bz4 = models.CharField(max_length=1000, blank=True, null=True)
#     bz5 = models.CharField(max_length=1000, blank=True, null=True)
#     bz6 = models.CharField(max_length=1000, blank=True, null=True)
#     ycbw = models.CharField(max_length=200, blank=True, null=True)
#     in_factory = models.CharField(max_length=200, blank=True, null=True)
#     czys = models.CharField(max_length=100, blank=True, null=True)
#     results = models.CharField(max_length=2000, blank=True, null=True)
#     fw = models.CharField(max_length=500, blank=True, null=True)
#     item_id_a = models.CharField(max_length=100, blank=True, null=True)
#     tdbg_bt = models.CharField(max_length=200, blank=True, null=True)
#     abnormal = models.CharField(max_length=10, blank=True, null=True)
#     sz = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
#     jt_bm = models.CharField(max_length=100, blank=True, null=True)
#     jb_bm_mc = models.CharField(max_length=200, blank=True, null=True)
#     zy_bz = models.CharField(max_length=200, blank=True, null=True)
#     table_sxh = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
#     item_sxh = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'jj_cust_zdnr_result'
#         verbose_name = u"诊断内容表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 诊断建议表
# class JjCustZdjyResult(models.Model):
#     vid = models.CharField(max_length=12, blank=True, null=True)
#     item_id = models.CharField(max_length=30, blank=True, null=True)
#     item_ms = models.CharField(max_length=30, blank=True, null=True)
#     item_ms_zb = models.CharField(max_length=30, blank=True, null=True)
#     zd_nr = models.CharField(max_length=200, blank=True, null=True)
#     sxh = models.IntegerField(blank=True, null=True)
#     bz1 = models.CharField(max_length=200, blank=True, null=True)
#     bz2 = models.CharField(max_length=100, blank=True, null=True)
#     bz3 = models.CharField(max_length=200, blank=True, null=True)
#     mbnr = models.CharField(max_length=1000, blank=True, null=True)
#     sfjb = models.CharField(max_length=100, blank=True, null=True)
#     jbnb = models.CharField(max_length=200, blank=True, null=True)
#     jybt = models.CharField(max_length=200, blank=True, null=True)
#     yxjs = models.CharField(max_length=1000, blank=True, null=True)
#     yyhg = models.CharField(max_length=1000, blank=True, null=True)
#     yxjy = models.CharField(max_length=1000, blank=True, null=True)
#     lb = models.CharField(max_length=10, blank=True, null=True)
#     trans_status1 = models.CharField(max_length=10, blank=True, null=True)
#     trans_status2 = models.CharField(max_length=10, blank=True, null=True)
#     djsj = models.DateField(blank=True, null=True)
#     bz4 = models.CharField(max_length=1000, blank=True, null=True)
#     bz5 = models.CharField(max_length=1000, blank=True, null=True)
#     bz6 = models.CharField(max_length=1000, blank=True, null=True)
#     ycbw = models.CharField(max_length=200, blank=True, null=True)
#     in_factory = models.CharField(max_length=200, blank=True, null=True)
#     czys = models.CharField(max_length=100, blank=True, null=True)
#     results = models.CharField(max_length=2000, blank=True, null=True)
#     fw = models.CharField(max_length=500, blank=True, null=True)
#     item_id_a = models.CharField(max_length=100, blank=True, null=True)
#     tdbg_bt = models.CharField(max_length=200, blank=True, null=True)
#     abnormal = models.CharField(max_length=10, blank=True, null=True)
#     sz = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
#     jt_bm = models.CharField(max_length=100, blank=True, null=True)
#     jb_bm_mc = models.CharField(max_length=200, blank=True, null=True)
#     zy_bz = models.CharField(max_length=200, blank=True, null=True)
#     table_sxh = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
#     item_sxh = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'jj_cust_zdjy_result'
#         verbose_name = u"诊断建议表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 异常部位表
# class JjYcbwResults(models.Model):
#     vid = models.CharField(max_length=10, blank=True, null=True)
#     t = models.CharField(max_length=10, blank=True, null=True)
#     yj = models.CharField(max_length=10, blank=True, null=True)
#     ebh = models.CharField(max_length=10, blank=True, null=True)
#     kq = models.CharField(max_length=10, blank=True, null=True)
#     jdm = models.CharField(max_length=10, blank=True, null=True)
#     xz = models.CharField(max_length=10, blank=True, null=True)
#     jzyz = models.CharField(max_length=10, blank=True, null=True)
#     xq = models.CharField(max_length=10, blank=True, null=True)
#     ybjc = models.CharField(max_length=10, blank=True, null=True)
#     nk = models.CharField(max_length=10, blank=True, null=True)
#     wk = models.CharField(max_length=10, blank=True, null=True)
#     qt = models.CharField(max_length=10, blank=True, null=True)
#     jzx = models.CharField(max_length=10, blank=True, null=True)
#     rf = models.CharField(max_length=10, blank=True, null=True)
#     g = models.CharField(max_length=10, blank=True, null=True)
#     d = models.CharField(max_length=10, blank=True, null=True)
#     y = models.CharField(max_length=10, blank=True, null=True)
#     p = models.CharField(max_length=10, blank=True, null=True)
#     s = models.CharField(max_length=10, blank=True, null=True)
#     wc = models.CharField(max_length=10, blank=True, null=True)
#     fk = models.CharField(max_length=10, blank=True, null=True)
#     zgfj = models.CharField(max_length=10, blank=True, null=True)
#     ny = models.CharField(max_length=10, blank=True, null=True)
#     zlxy = models.CharField(max_length=10, blank=True, null=True)
#     qtxy = models.CharField(max_length=10, blank=True, null=True)
#     qlx = models.CharField(max_length=10, blank=True, null=True)
#     pgsng = models.CharField(max_length=10, blank=True, null=True)
#     bz1 = models.CharField(max_length=10, blank=True, null=True)
#     bz2 = models.CharField(max_length=10, blank=True, null=True)
#     bz3 = models.CharField(max_length=10, blank=True, null=True)
#     bz4 = models.CharField(max_length=10, blank=True, null=True)
#     bz5 = models.CharField(max_length=10, blank=True, null=True)
#     in_factory = models.CharField(max_length=10, blank=True, null=True)
#     trans_status = models.CharField(max_length=10, blank=True, null=True)
#     djsj = models.DateField(blank=True, null=True)
#     xb = models.CharField(max_length=10, blank=True, null=True)
#     tzzs = models.CharField(max_length=10, blank=True, null=True)
#     xy = models.CharField(max_length=10, blank=True, null=True)
#     xt = models.CharField(max_length=10, blank=True, null=True)
#     x_xz = models.CharField(max_length=10, blank=True, null=True)
#     sg = models.CharField(max_length=10, blank=True, null=True)
#     gg = models.CharField(max_length=10, blank=True, null=True)
#     zl = models.CharField(max_length=10, blank=True, null=True)
#     zcf = models.CharField(max_length=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'jj_ycbw_results'
#         verbose_name = u"异常部位表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 检查客人检查部位表
# class JjCustJtBwItemResult(models.Model):
#     vid = models.CharField(max_length=20, blank=True, null=True)
#     lb = models.CharField(max_length=20, blank=True, null=True)
#     item_id = models.CharField(max_length=100, blank=True, null=True)
#     item_name = models.CharField(max_length=200, blank=True, null=True)
#     num = models.BigIntegerField(blank=True, null=True)
#     trans_status = models.CharField(max_length=10, blank=True, null=True)
#     djsj = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'jj_cust_jt_bw_item_result'
#         verbose_name = u"检查客人检查部位表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 团体报告客人表
# class JjYyqkbTdbgList(models.Model):
#     vid = models.CharField(max_length=20, blank=True, null=True)
#     xm = models.CharField(max_length=100, blank=True, null=True)
#     xb = models.CharField(max_length=10, blank=True, null=True)
#     hyzk = models.CharField(max_length=100, blank=True, null=True)
#     csrq = models.DateField(blank=True, null=True)
#     sfzhm = models.CharField(max_length=50, blank=True, null=True)
#     fgs = models.CharField(max_length=300, blank=True, null=True)
#     bm1 = models.CharField(max_length=300, blank=True, null=True)
#     bm2 = models.CharField(max_length=300, blank=True, null=True)
#     ygh = models.CharField(max_length=300, blank=True, null=True)
#     dwdm = models.CharField(max_length=50, blank=True, null=True)
#     dwyyid = models.CharField(max_length=100, blank=True, null=True)
#     yysj = models.DateField(blank=True, null=True)
#     trans_status = models.CharField(max_length=10, blank=True, null=True)
#     djsj = models.DateField(blank=True, null=True)
#     bz1 = models.CharField(max_length=100, blank=True, null=True)
#     bz2 = models.CharField(max_length=100, blank=True, null=True)
#     bz3 = models.CharField(max_length=100, blank=True, null=True)
#     bz4 = models.CharField(max_length=100, blank=True, null=True)
#     bz5 = models.CharField(max_length=100, blank=True, null=True)
#     bz6 = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'jj_yyqkb_tdbg_list'
#         verbose_name = u"团体报告客人表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 脏器切除或手术登记表
#
# # 重大阳性登记表2019
# class JjGwycList2019(models.Model):
#     billcode = models.CharField(max_length=200, blank=True, null=True)
#     cid = models.CharField(max_length=100, blank=True, null=True)
#     vid = models.CharField(max_length=20, blank=True, null=True)
#     xm = models.CharField(max_length=200, blank=True, null=True)
#     xb = models.CharField(max_length=20, blank=True, null=True)
#     dwdm = models.CharField(max_length=100, blank=True, null=True)
#     yysj = models.DateField(blank=True, null=True)
#     in_factory = models.CharField(max_length=30, blank=True, null=True)
#     lr_factory = models.CharField(max_length=30, blank=True, null=True)
#     lb = models.CharField(max_length=100, blank=True, null=True)
#     dm = models.CharField(max_length=200, blank=True, null=True)
#     mc = models.CharField(max_length=500, blank=True, null=True)
#     mc_detail = models.CharField(max_length=800, blank=True, null=True)
#     dept_code = models.CharField(max_length=100, blank=True, null=True)
#     lr_opername = models.CharField(max_length=200, blank=True, null=True)
#     lr_date = models.DateField(blank=True, null=True)
#     yxf = models.CharField(max_length=10, blank=True, null=True)
#     bz1 = models.CharField(max_length=500, blank=True, null=True)
#     bz2 = models.CharField(max_length=500, blank=True, null=True)
#     bz3 = models.CharField(max_length=500, blank=True, null=True)
#     bz4 = models.CharField(max_length=500, blank=True, null=True)
#     bz5 = models.CharField(max_length=500, blank=True, null=True)
#     read_ornot = models.CharField(max_length=10, blank=True, null=True)
#     read_opername = models.CharField(max_length=100, blank=True, null=True)
#     sh_opername = models.CharField(max_length=100, blank=True, null=True)
#     sh_date = models.DateField(blank=True, null=True)
#     status = models.CharField(max_length=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'jj_gwyc_list2019'
#         verbose_name = u"重大阳性登记表2019"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.vid
#
#
# # 襄阳美年大健康襄州分院
# # 检查结果表
#
# # 检查明细表
#
# # 小贴士一
#
# # 小贴士二表
#
# # 客人图片表
# class JjCustPhoto(models.Model):
#     cid = models.CharField(max_length=12, blank=True, null=True)
#     cid_photo = models.BinaryField(blank=True, null=True)
#     trans_status = models.CharField(max_length=1, blank=True, null=True)
#     op_datetime = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'jj_cust_photo'
#         verbose_name = u"客人图片表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.cid
#
#
# # 数据统一表
# class SysDataComplete2(models.Model):
#     code_value = models.CharField(max_length=30, blank=True, null=True)
#     lb = models.CharField(max_length=2, blank=True, null=True)
#     trans_status = models.CharField(max_length=1, blank=True, null=True)
#     op_datetime = models.DateField(blank=True, null=True)
#     in_factory = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sys_data_complete_2'
#         verbose_name = u"数据统一表"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.code_value

# 检验结果表

# 检验样本表

# 预约情况表

# 客人基本信息表

# 宫颈刮片表

# 诊断内容结果

# 异常部位

# 建议表

# 重大阳性随访表2019
