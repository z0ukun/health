# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AutoDownUpLog(models.Model):
    rq = models.DateField(blank=True, null=True, verbose_name=u"日期")
    down_up = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"上传下载")
    in_factory = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"in_factory")
    status = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"状态")

    class Meta:
        managed = False
        db_table = 'auto_down_up_log'
        verbose_name = u"AutoDownUpLog"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.rq


class BasBgdType(models.Model):
    dm = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"代码")
    mc = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"名称")
    sjdm = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"上级代码")
    jb = models.IntegerField(blank=True, null=True, verbose_name=u"级别")
    yzjf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"有子集否")
    op_datetime = models.DateField(blank=True, null=True, verbose_name=u"数据日期")

    class Meta:
        managed = False
        db_table = 'bas_bgd_type'
        verbose_name = u"BasBgdType"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.dm


class BasChargeItemTs(models.Model):
    item_id = models.CharField(max_length=10, blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    ts = models.CharField(max_length=600, blank=True, null=True)
    ms = models.CharField(max_length=1000, blank=True, null=True)
    zd = models.CharField(max_length=1000, blank=True, null=True)
    trans_status = models.CharField(max_length=1000, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_charge_item_ts'


class BasCode(models.Model):
    table_name = models.CharField(max_length=30, blank=True, null=True)
    field_name = models.CharField(max_length=30, blank=True, null=True)
    code = models.CharField(max_length=1, blank=True, null=True)
    explain = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_code'


# 基础部分
# 客人基本信息
class BasCustInfor(models.Model):
    cid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"健检号")
    xm = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"姓名")
    xb = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"性别")
    csrq = models.DateField(blank=True, null=True, verbose_name=u"出生日期")
    sfzhm = models.CharField(max_length=18, blank=True, null=True, verbose_name=u"身份证号码")
    mz = models.CharField(max_length=4, blank=True, null=True, verbose_name=u"民族")
    whcd = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"文化程度")
    gj = models.CharField(max_length=4, blank=True, null=True, verbose_name=u"国家")
    hyzk = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"婚姻状况")
    jtzz = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"家庭住址")
    yzbm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"邮政编码")
    lxdh = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"联系电话")
    yddh = models.CharField(max_length=11, blank=True, null=True, verbose_name=u"移动电话")
    dwdm = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"单位代码")
    dwmc = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"婚姻状况")
    email = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"邮箱")
    bz = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"是否职工")
    djsj = models.DateField(blank=True, null=True, verbose_name=u"登记时间")
    djr = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"登记人")
    province = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"所属身份")
    city = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"所属城市")
    region = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"所属区域")
    cust_type = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"客户类型")
    zwdm = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"职务代码")
    # 客人所属单位组(属于单位定义的什么组)
    cw = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"客人所属单位组")
    zycd = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"工作职业")
    hycd = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"工作行业")
    khly = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"客户来源")
    zhye = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=u"账户余额")
    member_type = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"确认模式")
    card_code = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"健检号")
    member_card_code = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"会员卡号")
    trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
    op_date = models.DateField(blank=True, null=True, verbose_name=u"修改时间")
    ywydm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"业务员代码")
    gsgddh = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"公司固定电话")
    khtz = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"客人特征")
    gstz = models.CharField(max_length=150, blank=True, null=True, verbose_name=u"公司地址")
    txtz = models.CharField(max_length=150, blank=True, null=True, verbose_name=u"通讯地址")
    # 有效级（0：单店 1：多店)
    yxjb = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"有效级别")
    # 客人区域（1：来源于体检 2：来源于医务室)
    cust_region = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"客人区域")
    k3_item = models.CharField(max_length=80, blank=True, null=True, verbose_name=u"K3公司代码")
    k3_zg_item = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"K3职工代码")
    bgd_lb = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"报告单类别")
    grgz_ye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"挂账余额")
    zzys = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"咨询医生")
    xgsj = models.DateField(blank=True, null=True, verbose_name=u"修改时间")
    user_password = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"用户密码")
    password_xgsj = models.DateField(blank=True, null=True, verbose_name=u"密码修改时间")
    zzhs = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"ZZHS")

    class Meta:
        managed = False
        db_table = 'bas_cust_infor'
        verbose_name = u"BasCustInfor"
        verbose_name_plural = verbose_name


class BasCustType(models.Model):
    dm = models.CharField(max_length=6, blank=True, null=True)
    mc = models.CharField(max_length=10, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)
    sjdm = models.CharField(max_length=4, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    vip_region = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_cust_type'


class BasDepartment(models.Model):
    dept_code = models.CharField(max_length=6, blank=True, null=True)
    dept_name = models.CharField(max_length=40, blank=True, null=True)
    dept_alias = models.CharField(max_length=8, blank=True, null=True)
    dept_type = models.CharField(max_length=12, blank=True, null=True)
    director = models.CharField(max_length=8, blank=True, null=True)
    valid_flag = models.CharField(max_length=1, blank=True, null=True)
    telphone = models.CharField(max_length=30, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    aid_code = models.CharField(max_length=10, blank=True, null=True)
    in_factory = models.CharField(max_length=3, blank=True, null=True)
    op_date = models.DateField(blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)
    cust_type = models.CharField(max_length=1, blank=True, null=True)
    sort_position = models.IntegerField(blank=True, null=True)
    vip_cust = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_department'


class BasDeptItem(models.Model):
    item_id = models.CharField(max_length=6, blank=True, null=True)
    dept_code = models.CharField(max_length=8, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    sfzyxm = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_dept_item'


class BasDeptType(models.Model):
    dept_type = models.CharField(max_length=12, blank=True, null=True)
    type_name = models.CharField(max_length=20, blank=True, null=True)
    sjdm = models.CharField(max_length=8, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    op_date = models.DateField(blank=True, null=True)
    lb = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_dept_type'


class BasDiagnose(models.Model):
    zddm = models.CharField(max_length=4, blank=True, null=True)
    ksdm = models.CharField(max_length=6, blank=True, null=True)
    icddm = models.CharField(max_length=15, blank=True, null=True)
    zdmc = models.CharField(max_length=40, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_diagnose'


class BasFkfs(models.Model):
    dm = models.CharField(max_length=2, blank=True, null=True)
    mc = models.CharField(max_length=40, blank=True, null=True)
    hl = models.IntegerField(blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    sjdm = models.CharField(max_length=2, blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    c3_item = models.CharField(max_length=30, blank=True, null=True)
    xj_bz = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_fkfs'


class BasFq(models.Model):
    dm = models.CharField(max_length=4, blank=True, null=True)
    mc = models.CharField(max_length=20, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    xh = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_fq'


class BasFqDept(models.Model):
    fq = models.CharField(max_length=2, blank=True, null=True)
    dept_code = models.CharField(max_length=6, blank=True, null=True)
    sfkf = models.CharField(max_length=1, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_fq_dept'


class BasGj(models.Model):
    dm = models.CharField(max_length=4, blank=True, null=True)
    mc = models.CharField(max_length=20, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_gj'


class BasHmwhb(models.Model):
    hmmc = models.CharField(max_length=30, blank=True, null=True)
    rq = models.DateField(blank=True, null=True)
    zdhm = models.BigIntegerField(blank=True, null=True)
    hmlx = models.CharField(max_length=1, blank=True, null=True)
    bz = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_hmwhb'


class BasHyzk(models.Model):
    dm = models.CharField(max_length=2, blank=True, null=True)
    mc = models.CharField(max_length=20, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_hyzk'


class BasItemQueue(models.Model):
    dm = models.CharField(max_length=3, blank=True, null=True)
    userobject = models.CharField(max_length=40, blank=True, null=True)
    mc = models.CharField(max_length=40, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    sjdm = models.CharField(max_length=3, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_item_queue'


class BasMemberType(models.Model):
    member_code = models.CharField(max_length=2, blank=True, null=True)
    member_name = models.CharField(max_length=20, blank=True, null=True)
    sjdm = models.CharField(max_length=2, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    vip_region = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_member_type'


class BasMemeberDealType(models.Model):
    deal_code = models.CharField(max_length=2, blank=True, null=True)
    deal_name = models.CharField(max_length=20, blank=True, null=True)
    deal_type = models.CharField(max_length=1, blank=True, null=True)
    sjdm = models.CharField(max_length=2, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    lb = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_memeber_deal_type'


class BasMz(models.Model):
    dm = models.CharField(max_length=4, blank=True, null=True)
    mc = models.CharField(max_length=20, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_mz'


class BasRegionDict(models.Model):
    dm = models.CharField(max_length=12, blank=True, null=True)
    mc = models.CharField(max_length=60, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_region_dict'


class BasTdbgJbDict(models.Model):
    dm = models.IntegerField(blank=True, null=True)
    mc = models.CharField(max_length=60, blank=True, null=True)
    aid_code = models.CharField(max_length=10, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_tdbg_jb_dict'


class BasUserDept(models.Model):
    userid = models.CharField(max_length=6, blank=True, null=True)
    dept_code = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_user_dept'


class BasUserType(models.Model):
    type_code = models.CharField(max_length=6, blank=True, null=True)
    type_name = models.CharField(max_length=20, blank=True, null=True)
    sjdm = models.CharField(max_length=6, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    op_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_user_type'


class BasWhcd(models.Model):
    dm = models.CharField(max_length=4, blank=True, null=True)
    mc = models.CharField(max_length=20, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_whcd'


class BasXb(models.Model):
    dm = models.CharField(max_length=2, blank=True, null=True)
    mc = models.CharField(max_length=4, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_xb'


class BasZwDict(models.Model):
    dm = models.CharField(max_length=12, blank=True, null=True)
    mc = models.CharField(max_length=50, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)
    sjdm = models.CharField(max_length=12, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_zw_dict'


class CommGzhyDict(models.Model):
    dm = models.CharField(max_length=20, blank=True, null=True)
    mc = models.CharField(max_length=60, blank=True, null=True)
    sjdm = models.CharField(max_length=20, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comm_gzhy_dict'


class CommUsertype(models.Model):
    user_id = models.CharField(max_length=6, blank=True, null=True)
    type_code = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comm_usertype'


class CommZwzk(models.Model):
    dm = models.CharField(max_length=4, blank=True, null=True)
    hz = models.CharField(max_length=2, blank=True, null=True)
    bzpym = models.CharField(max_length=12, blank=True, null=True)
    sjhm = models.CharField(max_length=4, blank=True, null=True)
    wbzx = models.CharField(max_length=4, blank=True, null=True)
    hz_ft = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comm_zwzk'


class CommZyDict(models.Model):
    dm = models.CharField(max_length=20, blank=True, null=True)
    mc = models.CharField(max_length=60, blank=True, null=True)
    sjdm = models.CharField(max_length=20, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comm_zy_dict'


class CrmBeforeYypq(models.Model):
    rq = models.DateField(blank=True, null=True)
    lb = models.CharField(max_length=10, blank=True, null=True)
    a1 = models.CharField(max_length=3000, blank=True, null=True)
    a2 = models.CharField(max_length=3000, blank=True, null=True)
    a3 = models.CharField(max_length=3000, blank=True, null=True)
    a4 = models.CharField(max_length=3000, blank=True, null=True)
    a5 = models.CharField(max_length=3000, blank=True, null=True)
    a6 = models.CharField(max_length=3000, blank=True, null=True)
    a7 = models.CharField(max_length=3000, blank=True, null=True)
    a8 = models.CharField(max_length=3000, blank=True, null=True)
    a9 = models.CharField(max_length=3000, blank=True, null=True)
    a10 = models.CharField(max_length=3000, blank=True, null=True)
    a11 = models.CharField(max_length=3000, blank=True, null=True)
    a12 = models.CharField(max_length=3000, blank=True, null=True)
    a13 = models.CharField(max_length=3000, blank=True, null=True)
    a14 = models.CharField(max_length=3000, blank=True, null=True)
    a15 = models.CharField(max_length=3000, blank=True, null=True)
    a16 = models.CharField(max_length=3000, blank=True, null=True)
    a17 = models.CharField(max_length=3000, blank=True, null=True)
    a18 = models.CharField(max_length=3000, blank=True, null=True)
    a19 = models.CharField(max_length=3000, blank=True, null=True)
    a20 = models.CharField(max_length=3000, blank=True, null=True)
    a21 = models.CharField(max_length=3000, blank=True, null=True)
    a22 = models.CharField(max_length=3000, blank=True, null=True)
    a23 = models.CharField(max_length=3000, blank=True, null=True)
    a24 = models.CharField(max_length=3000, blank=True, null=True)
    a25 = models.CharField(max_length=3000, blank=True, null=True)
    a26 = models.CharField(max_length=3000, blank=True, null=True)
    a27 = models.CharField(max_length=3000, blank=True, null=True)
    a28 = models.CharField(max_length=3000, blank=True, null=True)
    a29 = models.CharField(max_length=3000, blank=True, null=True)
    a30 = models.CharField(max_length=3000, blank=True, null=True)
    a31 = models.CharField(max_length=3000, blank=True, null=True)
    bz1 = models.CharField(max_length=3000, blank=True, null=True)
    bz2 = models.CharField(max_length=3000, blank=True, null=True)
    bz3 = models.CharField(max_length=3000, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_before_yypq'


class CrmBeforeYypqList(models.Model):
    billcode = models.CharField(max_length=100, blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    yyrq = models.DateField(blank=True, null=True)
    lb = models.CharField(max_length=10, blank=True, null=True)
    dwdm = models.CharField(max_length=100, blank=True, null=True)
    dwmc = models.CharField(max_length=100, blank=True, null=True)
    item_id = models.CharField(max_length=30, blank=True, null=True)
    pqrs = models.IntegerField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    ywy = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_before_yypq_list'


class CrmCustEqhf(models.Model):
    cid = models.CharField(max_length=12, blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    lx = models.CharField(max_length=2, blank=True, null=True)
    xm = models.CharField(max_length=30, blank=True, null=True)
    xb = models.CharField(max_length=1, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    print_time = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    tzzs = models.IntegerField(blank=True, null=True)
    xy = models.IntegerField(blank=True, null=True)
    gxt_g = models.IntegerField(blank=True, null=True)
    gxt_z = models.IntegerField(blank=True, null=True)
    dgc = models.IntegerField(blank=True, null=True)
    gysz = models.IntegerField(blank=True, null=True)
    dmdzdb = models.IntegerField(blank=True, null=True)
    bc = models.IntegerField(blank=True, null=True)
    fk_time = models.DateField(blank=True, null=True)
    final_time = models.DateField(blank=True, null=True)
    fk_checkoper = models.CharField(max_length=6, blank=True, null=True)
    final_checkoper = models.CharField(max_length=6, blank=True, null=True)
    lxdh = models.CharField(max_length=30, blank=True, null=True)
    yddh = models.CharField(max_length=30, blank=True, null=True)
    hff = models.CharField(max_length=1, blank=True, null=True)
    hfr = models.CharField(max_length=6, blank=True, null=True)
    hfsj = models.DateField(blank=True, null=True)
    ns = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_cust_eqhf'


class CrmGjfs(models.Model):
    dm = models.CharField(max_length=2, blank=True, null=True)
    mc = models.CharField(max_length=30, blank=True, null=True)
    sjdm = models.CharField(max_length=2, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_gjfs'


class CrmGjjg(models.Model):
    dm = models.CharField(max_length=2, blank=True, null=True)
    mc = models.CharField(max_length=30, blank=True, null=True)
    sjdm = models.CharField(max_length=2, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    yxjb = models.CharField(max_length=2, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_gjjg'


class CrmGjmd(models.Model):
    dm = models.CharField(max_length=2, blank=True, null=True)
    mc = models.CharField(max_length=30, blank=True, null=True)
    sjdm = models.CharField(max_length=2, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_gjmd'


class CrmHrfcXx(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    id = models.CharField(max_length=4, blank=True, null=True)
    mc = models.CharField(max_length=60, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    fcsj = models.DateField(blank=True, null=True)
    tzsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_hrfc_xx'


class CrmHtglList(models.Model):
    dh = models.CharField(max_length=12, blank=True, null=True)
    groupid = models.CharField(max_length=6, blank=True, null=True)
    lb = models.CharField(max_length=1, blank=True, null=True)
    bl = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    je = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_htgl_list'


class CrmHtjbqk(models.Model):
    dh = models.CharField(max_length=12, blank=True, null=True)
    htbh = models.CharField(max_length=20, blank=True, null=True)
    f_part = models.CharField(max_length=60, blank=True, null=True)
    s_part = models.CharField(max_length=60, blank=True, null=True)
    t_part = models.CharField(max_length=60, blank=True, null=True)
    contxt = models.CharField(max_length=3000, blank=True, null=True)
    f_person = models.CharField(max_length=10, blank=True, null=True)
    s_person = models.CharField(max_length=10, blank=True, null=True)
    t_person = models.CharField(max_length=60, blank=True, null=True)
    qdrq = models.DateField(blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    lrr = models.CharField(max_length=10, blank=True, null=True)
    shr = models.CharField(max_length=10, blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    djzt = models.CharField(max_length=1, blank=True, null=True)
    bj = models.CharField(max_length=200, blank=True, null=True)
    htzt = models.CharField(max_length=60, blank=True, null=True)
    je = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bdw = models.CharField(max_length=40, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    lx = models.CharField(max_length=1, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    dwdm = models.CharField(max_length=12, blank=True, null=True)
    zfry = models.CharField(max_length=6, blank=True, null=True)
    zfsj = models.DateField(blank=True, null=True)
    qdrq_end = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_htjbqk'


class CrmHycddmb(models.Model):
    dm = models.CharField(max_length=2, blank=True, null=True)
    mc = models.CharField(max_length=10, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_hycddmb'


class CrmMemberYhList(models.Model):
    dh = models.CharField(max_length=12, blank=True, null=True)
    member_code = models.CharField(max_length=2, blank=True, null=True)
    groupid = models.CharField(max_length=6, blank=True, null=True)
    yhbl = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    je = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    lb = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_member_yh_list'


class CrmMemberYhSy(models.Model):
    dh = models.CharField(max_length=12, blank=True, null=True)
    yhzc = models.CharField(max_length=100, blank=True, null=True)
    lrry = models.CharField(max_length=6, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    shry = models.CharField(max_length=6, blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    zfry = models.CharField(max_length=6, blank=True, null=True)
    zfsj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_member_yh_sy'


class CrmOtherYhDict(models.Model):
    dm = models.CharField(max_length=2, blank=True, null=True)
    mc = models.CharField(max_length=60, blank=True, null=True)
    sjdm = models.CharField(max_length=2, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=10, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    hand_select = models.CharField(max_length=1, blank=True, null=True)
    hand_do = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_other_yh_dict'


class CrmOtherYhList(models.Model):
    dh = models.CharField(max_length=12, blank=True, null=True)
    lb = models.CharField(max_length=2, blank=True, null=True)
    dwdm = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    mc = models.CharField(max_length=60, blank=True, null=True)
    bl = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    je = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    yhlb = models.CharField(max_length=1, blank=True, null=True)
    groupid = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_other_yh_list'


class CrmOtherYhSy(models.Model):
    dh = models.CharField(max_length=12, blank=True, null=True)
    yhzc = models.CharField(max_length=100, blank=True, null=True)
    lrry = models.CharField(max_length=6, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    shry = models.CharField(max_length=6, blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    zfry = models.CharField(max_length=6, blank=True, null=True)
    zfsj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_other_yh_sy'


class CrmPreCustRecord(models.Model):
    record_id = models.BigIntegerField(blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=60, blank=True, null=True)
    ywydm = models.CharField(max_length=6, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    lrry = models.CharField(max_length=6, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    gjfs = models.CharField(max_length=2, blank=True, null=True)
    gjmd = models.CharField(max_length=2, blank=True, null=True)
    kssj = models.DateField(blank=True, null=True)
    jzsj = models.DateField(blank=True, null=True)
    jgjg = models.CharField(max_length=2, blank=True, null=True)
    lb = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_pre_cust_record'


class CrmSmsDict(models.Model):
    dm = models.CharField(max_length=9, blank=True, null=True)
    mc = models.CharField(max_length=60, blank=True, null=True)
    sjdm = models.CharField(max_length=8, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)
    yzjf = models.CharField(max_length=9, blank=True, null=True)
    sms_context = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_sms_dict'


class CrmTslbDict(models.Model):
    dm = models.CharField(max_length=6, blank=True, null=True)
    mc = models.CharField(max_length=60, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    sjdm = models.CharField(max_length=6, blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_tslb_dict'


class CrmTthymxb(models.Model):
    dh = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=12, blank=True, null=True)
    lxdh = models.CharField(max_length=20, blank=True, null=True)
    memeber_code = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_tthymxb'


class CrmTthysyb(models.Model):
    dh = models.CharField(max_length=12, blank=True, null=True)
    mc = models.CharField(max_length=100, blank=True, null=True)
    lxrcid = models.CharField(max_length=12, blank=True, null=True)
    lxrxm = models.CharField(max_length=12, blank=True, null=True)
    lx = models.CharField(max_length=2, blank=True, null=True)
    bj = models.CharField(max_length=50, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    lrry = models.CharField(max_length=10, blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    shry = models.CharField(max_length=10, blank=True, null=True)
    djzt = models.CharField(max_length=1, blank=True, null=True)
    zfry = models.CharField(max_length=6, blank=True, null=True)
    zfsj = models.DateField(blank=True, null=True)
    ywydm = models.CharField(max_length=6, blank=True, null=True)
    khly = models.CharField(max_length=6, blank=True, null=True)
    k3_item = models.CharField(max_length=80, blank=True, null=True)
    k3_zg_item = models.CharField(max_length=80, blank=True, null=True)
    k3_zg_name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_tthysyb'


class CrmYqfhCustList(models.Model):
    cid = models.CharField(max_length=12, blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=30, blank=True, null=True)
    xb = models.CharField(max_length=1, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    print_time = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    tzzs = models.IntegerField(blank=True, null=True)
    xy = models.IntegerField(blank=True, null=True)
    ydsy = models.IntegerField(blank=True, null=True)
    bc = models.IntegerField(blank=True, null=True)
    gmd = models.IntegerField(blank=True, null=True)
    fgn = models.IntegerField(blank=True, null=True)
    azb = models.IntegerField(blank=True, null=True)
    md = models.IntegerField(blank=True, null=True)
    zlbzw = models.IntegerField(blank=True, null=True)
    xt = models.IntegerField(blank=True, null=True)
    tg = models.IntegerField(blank=True, null=True)
    gg = models.IntegerField(blank=True, null=True)
    ns = models.IntegerField(blank=True, null=True)
    xz = models.IntegerField(blank=True, null=True)
    zjsj1 = models.DateField(blank=True, null=True)
    zjsj2 = models.DateField(blank=True, null=True)
    zjys1 = models.CharField(max_length=6, blank=True, null=True)
    zjys2 = models.CharField(max_length=6, blank=True, null=True)
    gddh = models.CharField(max_length=30, blank=True, null=True)
    yddh = models.CharField(max_length=30, blank=True, null=True)
    fhsj = models.DateField(blank=True, null=True)
    hff = models.CharField(max_length=1, blank=True, null=True)
    gg2 = models.CharField(max_length=1, blank=True, null=True)
    tg2 = models.CharField(max_length=1, blank=True, null=True)
    zlbzw_apky = models.CharField(max_length=1, blank=True, null=True)
    zlbzw_blasx = models.CharField(max_length=1, blank=True, null=True)
    xz_gysz = models.CharField(max_length=1, blank=True, null=True)
    sz_dmdzdb = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_yqfh_cust_list'


class CrmYwyxxb(models.Model):
    bh = models.CharField(max_length=6, blank=True, null=True)
    xm = models.CharField(max_length=10, blank=True, null=True)
    xb = models.CharField(max_length=1, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    mz = models.CharField(max_length=4, blank=True, null=True)
    zzmm = models.CharField(max_length=10, blank=True, null=True)
    dgsj = models.DateField(blank=True, null=True)
    lgsj = models.DateField(blank=True, null=True)
    ssbm = models.CharField(max_length=10, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    lrr = models.CharField(max_length=10, blank=True, null=True)
    zt = models.CharField(max_length=1, blank=True, null=True)
    lxdh = models.CharField(max_length=15, blank=True, null=True)
    jtzz = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    sfzhm = models.CharField(max_length=20, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)
    zfry = models.CharField(max_length=6, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    ly = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_ywyxxb'


class CrmYxjb(models.Model):
    dm = models.CharField(max_length=2, blank=True, null=True)
    mc = models.CharField(max_length=30, blank=True, null=True)
    sjdm = models.CharField(max_length=2, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_yxjb'


class CrmZycddmb(models.Model):
    dm = models.CharField(max_length=2, blank=True, null=True)
    mc = models.CharField(max_length=10, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_zycddmb'


class CustYyDeleteLog2019(models.Model):
    id = models.CharField(max_length=200, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)
    cid = models.CharField(max_length=100, blank=True, null=True)
    xm = models.CharField(max_length=300, blank=True, null=True)
    czmk = models.CharField(max_length=300, blank=True, null=True)
    dyid = models.CharField(max_length=300, blank=True, null=True)
    czry = models.CharField(max_length=200, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    bz4 = models.CharField(max_length=200, blank=True, null=True)
    bz5 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_yy_delete_log2019'


class CustZdyxList(models.Model):
    cid = models.CharField(max_length=30, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    xb = models.CharField(max_length=10, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    dwdm = models.CharField(max_length=30, blank=True, null=True)
    fgs = models.CharField(max_length=200, blank=True, null=True)
    bm1 = models.CharField(max_length=200, blank=True, null=True)
    bm2 = models.CharField(max_length=200, blank=True, null=True)
    ygh = models.CharField(max_length=100, blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    oper = models.CharField(max_length=30, blank=True, null=True)
    opername = models.CharField(max_length=50, blank=True, null=True)
    zdyx = models.CharField(max_length=800, blank=True, null=True)
    sfzhm = models.CharField(max_length=60, blank=True, null=True)
    lxdh = models.CharField(max_length=100, blank=True, null=True)
    dept_clyj = models.CharField(max_length=500, blank=True, null=True)
    dept_clry = models.CharField(max_length=50, blank=True, null=True)
    dept_clsj = models.DateField(blank=True, null=True)
    hz1_clyj = models.CharField(max_length=500, blank=True, null=True)
    hz1_clry = models.CharField(max_length=50, blank=True, null=True)
    hz1_clsj = models.DateField(blank=True, null=True)
    hz2_clyj = models.CharField(max_length=500, blank=True, null=True)
    hz2_clry = models.CharField(max_length=50, blank=True, null=True)
    hz2_clsj = models.DateField(blank=True, null=True)
    kf_clyj = models.CharField(max_length=500, blank=True, null=True)
    kf_clry = models.CharField(max_length=50, blank=True, null=True)
    kf_clsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_zdyx_list'


class DataExpList(models.Model):
    id = models.CharField(max_length=150, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)
    xm = models.CharField(max_length=150, blank=True, null=True)
    czy = models.CharField(max_length=100, blank=True, null=True)
    lb = models.CharField(max_length=100, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_exp_list'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class FactoryBjList(models.Model):
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    bz = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factory_bj_list'


class FeeWxzfbDict(models.Model):
    appid = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    rsakey = models.CharField(max_length=1500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fee_wxzfb_dict'


class HealthAddItem(models.Model):
    id = models.CharField(max_length=100, blank=True, null=True)
    misid = models.CharField(max_length=100, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)
    groupid = models.CharField(max_length=50, blank=True, null=True)
    groupname = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    lb = models.CharField(max_length=10, blank=True, null=True)
    ispayoff = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    local_vid = models.CharField(max_length=10, blank=True, null=True)
    local_status = models.CharField(max_length=10, blank=True, null=True)
    clry = models.CharField(max_length=100, blank=True, null=True)
    clsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'health_add_item'


class InitCxZj(models.Model):
    id = models.CharField(max_length=6, blank=True, null=True)
    cx_item = models.CharField(max_length=6, blank=True, null=True)
    zj_item = models.CharField(max_length=6, blank=True, null=True)
    yy_item = models.CharField(max_length=6, blank=True, null=True)
    cx_group = models.CharField(max_length=6, blank=True, null=True)
    zj_group = models.CharField(max_length=6, blank=True, null=True)
    yy_group = models.CharField(max_length=6, blank=True, null=True)
    cj_item = models.CharField(max_length=6, blank=True, null=True)
    zj_one_by_one = models.CharField(max_length=1, blank=True, null=True)
    bz1 = models.CharField(max_length=30, blank=True, null=True)
    bz2 = models.CharField(max_length=30, blank=True, null=True)
    bz3 = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'init_cx_zj'


class JdSocketLog(models.Model):
    czsj = models.DateField(blank=True, null=True)
    czy = models.CharField(max_length=6, blank=True, null=True)
    lb = models.CharField(max_length=1, blank=True, null=True)
    bz = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jd_socket_log'


# 系统登录日志
class JjAuthorLog(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    bz_c = models.CharField(max_length=20, blank=True, null=True)
    cid = models.CharField(max_length=30, blank=True, null=True)
    author_oper = models.CharField(max_length=60, blank=True, null=True)
    author_date = models.DateField(blank=True, null=True)
    bz1 = models.CharField(max_length=50, blank=True, null=True)
    bz2 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_author_log'


# 检查结果


# 检查结果日志
class JjCommJcResultsLog(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    cid = models.CharField(max_length=20, blank=True, null=True)
    xm = models.CharField(max_length=20, blank=True, null=True)
    xb = models.CharField(max_length=10, blank=True, null=True)
    dwmc = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=100, blank=True, null=True)
    old_results = models.CharField(max_length=3000, blank=True, null=True)
    new_results = models.CharField(max_length=3000, blank=True, null=True)
    jcr = models.CharField(max_length=30, blank=True, null=True)
    shr = models.CharField(max_length=30, blank=True, null=True)
    xgys = models.CharField(max_length=30, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    column_height = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_comm_jc_results_log'


class JjCookList(models.Model):
    bill_code = models.CharField(max_length=6, blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    cook_name = models.CharField(max_length=50, blank=True, null=True)
    cook_num = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    isrice = models.CharField(max_length=1, blank=True, null=True)
    memo = models.CharField(max_length=30, blank=True, null=True)
    units = models.CharField(max_length=8, blank=True, null=True)
    total_power = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_cook_list'


class JjCookbook(models.Model):
    bill_code = models.CharField(max_length=6, blank=True, null=True)
    cookbook_name = models.CharField(max_length=60, blank=True, null=True)
    operatorno = models.CharField(max_length=6, blank=True, null=True)
    operatordate = models.DateField(blank=True, null=True)
    audit_oper = models.CharField(max_length=6, blank=True, null=True)
    audit_date = models.DateField(blank=True, null=True)
    reject_oper = models.CharField(max_length=6, blank=True, null=True)
    reject_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    cook_type = models.CharField(max_length=1, blank=True, null=True)
    is_use = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_cookbook'


class JjDwyyGroup(models.Model):
    id = models.CharField(max_length=30, blank=True, null=True)
    dm = models.CharField(max_length=4, blank=True, null=True)
    mc = models.CharField(max_length=60, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_dwyy_group'


class JjDwyyRule(models.Model):
    id = models.CharField(max_length=30, blank=True, null=True)
    groupid = models.CharField(max_length=10, blank=True, null=True)
    dj = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    dm = models.CharField(max_length=4, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    bjf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_dwyy_rule'


class JjDwyySy(models.Model):
    id = models.CharField(max_length=30, blank=True, null=True)
    dwdm = models.CharField(max_length=12, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    djr = models.CharField(max_length=6, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    shr = models.CharField(max_length=6, blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    qbgdfs = models.CharField(max_length=10, blank=True, null=True)
    yxjb = models.CharField(max_length=2, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    bz = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_dwyy_sy'


class JjDxysInterface2(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    item_id = models.CharField(max_length=20, blank=True, null=True)
    item_name = models.CharField(max_length=200, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    bz1 = models.CharField(max_length=50, blank=True, null=True)
    bz2 = models.CharField(max_length=50, blank=True, null=True)
    bz3 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_dxys_interface2'


class JjDydPrintLog(models.Model):
    id = models.CharField(max_length=50, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    czy = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_dyd_print_log'


class JjGwycDict(models.Model):
    dm = models.CharField(max_length=200, blank=True, null=True)
    mc = models.CharField(max_length=500, blank=True, null=True)
    lb = models.CharField(max_length=60, blank=True, null=True)
    pdtj = models.CharField(max_length=600, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    yxf = models.CharField(max_length=10, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_gwyc_dict'


class JjHistoryDown2019(models.Model):
    in_factory = models.CharField(max_length=50, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    sfzhm = models.CharField(max_length=100, blank=True, null=True)
    xm = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    sqsj = models.DateField(blank=True, null=True)
    xzsj = models.DateField(blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)
    bz4 = models.CharField(max_length=100, blank=True, null=True)
    bz5 = models.CharField(max_length=100, blank=True, null=True)
    ms = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_history_down2019'


class JjJcysXmPhoto(models.Model):
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    pic = models.BinaryField(blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_jcys_xm_photo'


class JjNotinDict(models.Model):
    dm = models.CharField(max_length=20, blank=True, null=True)
    mc = models.CharField(max_length=150, blank=True, null=True)
    sjdm = models.CharField(max_length=20, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    lb = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_notin_dict'


# 图片传输存储
class JjOtherTpPrint(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    lb = models.CharField(max_length=20, blank=True, null=True)
    filename = models.CharField(max_length=200, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    bz1 = models.CharField(max_length=1000, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)
    in_factory = models.CharField(max_length=100, blank=True, null=True)
    print_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_other_tp_print'


class JjQtdjBzxx(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    bz = models.CharField(max_length=1000, blank=True, null=True)
    czry = models.CharField(max_length=100, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    bz2 = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_qtdj_bzxx'


class JjResultHistory(models.Model):
    cid = models.CharField(max_length=30, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)
    item_name = models.CharField(max_length=60, blank=True, null=True)
    results = models.CharField(max_length=4000, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_result_history'


class JjResultTitle(models.Model):
    result_id = models.CharField(max_length=6, blank=True, null=True)
    result_name = models.CharField(max_length=60, blank=True, null=True)
    result_en = models.CharField(max_length=60, blank=True, null=True)
    result_ft = models.CharField(max_length=60, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    sjdm = models.CharField(max_length=6, blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_result_title'


class JjResultXts2Dict(models.Model):
    item_id = models.CharField(max_length=30, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    nr1 = models.CharField(max_length=2000, blank=True, null=True)
    nr2 = models.CharField(max_length=2000, blank=True, null=True)
    nr3 = models.CharField(max_length=2000, blank=True, null=True)
    nr4 = models.CharField(max_length=2000, blank=True, null=True)
    bz = models.CharField(max_length=100, blank=True, null=True)
    sjdm = models.CharField(max_length=30, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    nr5 = models.CharField(max_length=2000, blank=True, null=True)
    column_height = models.IntegerField(blank=True, null=True)
    nr6 = models.CharField(max_length=2000, blank=True, null=True)
    nr7 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_result_xts_2_dict'


class JjSfmxbAddItemTemp(models.Model):
    vid = models.CharField(max_length=30, blank=True, null=True)
    groupid = models.CharField(max_length=100, blank=True, null=True)
    groupname = models.CharField(max_length=100, blank=True, null=True)
    oldprice = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    czy = models.CharField(max_length=30, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_sfmxb_add_item_temp'


class JjSfmxbCzLog(models.Model):
    billcode = models.CharField(max_length=200, blank=True, null=True)
    lx = models.CharField(max_length=100, blank=True, null=True)
    old_sfmxid = models.CharField(max_length=20, blank=True, null=True)
    vid = models.CharField(max_length=20, blank=True, null=True)
    cid = models.CharField(max_length=20, blank=True, null=True)
    old_groupid = models.CharField(max_length=20, blank=True, null=True)
    old_groupname = models.CharField(max_length=200, blank=True, null=True)
    old_price = models.CharField(max_length=30, blank=True, null=True)
    old_jxf = models.CharField(max_length=10, blank=True, null=True)
    new_sfmxid = models.CharField(max_length=20, blank=True, null=True)
    new_groupid = models.CharField(max_length=20, blank=True, null=True)
    new_groupname = models.CharField(max_length=200, blank=True, null=True)
    new_price = models.CharField(max_length=30, blank=True, null=True)
    new_jxf = models.CharField(max_length=10, blank=True, null=True)
    czy = models.CharField(max_length=30, blank=True, null=True)
    czy_name = models.CharField(max_length=100, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_sfmxb_cz_log'


class JjTsnrList2019(models.Model):
    billcode = models.CharField(max_length=200, blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    point_name = models.CharField(max_length=500, blank=True, null=True)
    sfzhm = models.CharField(max_length=100, blank=True, null=True)
    xm = models.CharField(max_length=200, blank=True, null=True)
    important_status = models.CharField(max_length=200, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    lrry = models.CharField(max_length=100, blank=True, null=True)
    tsnr = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    bz4 = models.CharField(max_length=200, blank=True, null=True)
    bz5 = models.CharField(max_length=200, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_tsnr_list2019'


class JjVidOtherTrans(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    xm = models.CharField(max_length=200, blank=True, null=True)
    xb = models.CharField(max_length=10, blank=True, null=True)
    dwdm = models.CharField(max_length=30, blank=True, null=True)
    zjsj = models.DateField(blank=True, null=True)
    clsj = models.DateField(blank=True, null=True)
    clry = models.CharField(max_length=100, blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)
    bz4 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_vid_other_trans'


class JjYgldbPrint(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    print_opername = models.CharField(max_length=100, blank=True, null=True)
    print_time = models.DateField(blank=True, null=True)
    zjsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_ygldb_print'


class JjYygqdjb(models.Model):
    dh = models.CharField(max_length=12, blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    yysj_o = models.DateField(blank=True, null=True)
    yysj_n = models.DateField(blank=True, null=True)
    lrry = models.CharField(max_length=10, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    shry = models.CharField(max_length=10, blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    djzt = models.CharField(max_length=1, blank=True, null=True)
    bj = models.CharField(max_length=60, blank=True, null=True)
    gqry = models.CharField(max_length=60, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_yygqdjb'


class JjYyqkbXh(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    lsh = models.BigIntegerField(blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)
    bz4 = models.CharField(max_length=100, blank=True, null=True)
    bz5 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_yyqkb_xh'


class JjZczdMszd(models.Model):
    dm = models.CharField(max_length=4, blank=True, null=True)
    mc = models.CharField(max_length=30, blank=True, null=True)
    sjdm = models.CharField(max_length=4, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_zczd_mszd'


class LisAdviceSingle(models.Model):
    bill_code = models.CharField(max_length=20, blank=True, null=True)
    item_id = models.CharField(max_length=6, blank=True, null=True)
    advice_type = models.CharField(max_length=1, blank=True, null=True)
    advice_context = models.CharField(max_length=1000, blank=True, null=True)
    item_value = models.CharField(max_length=100, blank=True, null=True)
    advice_title = models.CharField(max_length=100, blank=True, null=True)
    sfjb = models.CharField(max_length=1, blank=True, null=True)
    zd_title = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_advice_single'


class LisApparatus(models.Model):
    apparatusid = models.CharField(max_length=4, blank=True, null=True)
    apparatusname = models.CharField(max_length=40, blank=True, null=True)
    apparatusmodel = models.CharField(max_length=20, blank=True, null=True)
    filenamehead = models.CharField(max_length=18, blank=True, null=True)
    textrow = models.IntegerField(blank=True, null=True)
    functionname = models.CharField(max_length=18, blank=True, null=True)
    ipaddress = models.CharField(max_length=15, blank=True, null=True)
    port = models.CharField(max_length=1, blank=True, null=True)
    baudrate = models.IntegerField(blank=True, null=True)
    vertify = models.CharField(max_length=1, blank=True, null=True)
    bit = models.NullBooleanField()
    stop = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    checkno = models.IntegerField(blank=True, null=True)
    mcfs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_apparatus'


class LisContainer(models.Model):
    container_id = models.CharField(max_length=4, blank=True, null=True)
    container_name = models.CharField(max_length=20, blank=True, null=True)
    application = models.CharField(max_length=20, blank=True, null=True)
    producer = models.CharField(max_length=48, blank=True, null=True)
    lotno = models.CharField(max_length=10, blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    log_in_date = models.DateField(blank=True, null=True)
    log_in_name = models.CharField(max_length=5, blank=True, null=True)
    log_off_date = models.DateField(blank=True, null=True)
    log_off_name = models.CharField(max_length=5, blank=True, null=True)
    flag_airproof = models.NullBooleanField()
    flag_antisepsis = models.NullBooleanField()
    flag_siliconize = models.NullBooleanField()
    flag_asepsis = models.NullBooleanField()
    unit = models.CharField(max_length=10, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_container'


class LisHi701(models.Model):
    xh = models.IntegerField(blank=True, null=True)
    mc = models.CharField(max_length=30, blank=True, null=True)
    dw = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_hi701'


class LisQcJudgmentruledict(models.Model):
    ruleid = models.CharField(max_length=2, blank=True, null=True)
    rulecoding = models.CharField(max_length=10, blank=True, null=True)
    rulename = models.CharField(max_length=200, blank=True, null=True)
    errortype = models.CharField(max_length=1, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    inputperson = models.CharField(max_length=10, blank=True, null=True)
    inputpersonname = models.CharField(max_length=50, blank=True, null=True)
    states = models.CharField(max_length=1, blank=True, null=True)
    invalidatedate = models.DateField(blank=True, null=True)
    invalidateperson = models.CharField(max_length=10, blank=True, null=True)
    invalidatepersonname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_qc_judgmentruledict'


class LisQcProfiledict(models.Model):
    profileid = models.CharField(max_length=2, blank=True, null=True)
    profilename = models.CharField(max_length=50, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    inputperson = models.CharField(max_length=10, blank=True, null=True)
    inputpersonname = models.CharField(max_length=50, blank=True, null=True)
    states = models.CharField(max_length=1, blank=True, null=True)
    invalidatedate = models.DateField(blank=True, null=True)
    invalidateperson = models.CharField(max_length=10, blank=True, null=True)
    invalidatepersonname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_qc_profiledict'


class LisReference(models.Model):
    reference_id = models.CharField(max_length=6, blank=True, null=True)
    testitem_id = models.CharField(max_length=6, blank=True, null=True)
    testmethod_id = models.CharField(max_length=4, blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True, null=True)
    age_l = models.IntegerField(blank=True, null=True)
    age_h = models.IntegerField(blank=True, null=True)
    nation = models.CharField(max_length=4, blank=True, null=True)
    normal_l = models.CharField(max_length=40, blank=True, null=True)
    normal_h = models.CharField(max_length=40, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    dw = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_reference'


class LisResultChange(models.Model):
    id = models.CharField(max_length=4, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    value = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_result_change'


class LisSampleType(models.Model):
    sample_type_id = models.CharField(max_length=4, blank=True, null=True)
    sample_type_name = models.CharField(max_length=20, blank=True, null=True)
    sample_type_code = models.CharField(max_length=6, blank=True, null=True)
    sample_type_name_e = models.CharField(max_length=20, blank=True, null=True)
    sampling_method = models.CharField(max_length=100, blank=True, null=True)
    container_id = models.CharField(max_length=4, blank=True, null=True)
    storing_method = models.CharField(max_length=48, blank=True, null=True)
    trans_method = models.CharField(max_length=48, blank=True, null=True)
    mini_quatity = models.IntegerField(blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_sample_type'


class LisShLog(models.Model):
    id = models.CharField(max_length=300, blank=True, null=True)
    cid = models.CharField(max_length=100, blank=True, null=True)
    vid = models.CharField(max_length=100, blank=True, null=True)
    item_id = models.CharField(max_length=100, blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    clsj = models.DateField(blank=True, null=True)
    lx = models.CharField(max_length=100, blank=True, null=True)
    czy = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_sh_log'


class LisShYsDict(models.Model):
    begdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    lis_sh_ys = models.CharField(max_length=200, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_sh_ys_dict'


class LisTestMethod(models.Model):
    testmethod_id = models.CharField(max_length=4, blank=True, null=True)
    method_name = models.CharField(max_length=20, blank=True, null=True)
    sampletypeid = models.NullBooleanField()
    quantity_of_sample = models.IntegerField(blank=True, null=True)
    valid_range_l = models.CharField(max_length=8, blank=True, null=True)
    valid_range_h = models.CharField(max_length=8, blank=True, null=True)
    caution = models.CharField(max_length=100, blank=True, null=True)
    method_sen = models.CharField(max_length=20, blank=True, null=True)
    method_precision = models.CharField(max_length=20, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_test_method'


class LisTestProfile(models.Model):
    appid = models.CharField(max_length=10, blank=True, null=True)
    xh = models.CharField(max_length=10, blank=True, null=True)
    mc = models.CharField(max_length=60, blank=True, null=True)
    dw = models.CharField(max_length=30, blank=True, null=True)
    testitemid = models.CharField(max_length=14, blank=True, null=True)
    fjxx = models.CharField(max_length=60, blank=True, null=True)
    bj = models.CharField(max_length=60, blank=True, null=True)
    expression = models.CharField(max_length=60, blank=True, null=True)
    shortname = models.CharField(max_length=50, blank=True, null=True)
    name_c = models.CharField(max_length=50, blank=True, null=True)
    show = models.CharField(max_length=1, blank=True, null=True)
    code = models.CharField(max_length=6, blank=True, null=True)
    aid_code = models.CharField(max_length=6, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    sjdm = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_test_profile'


class LisUploadDetail(models.Model):
    dh = models.CharField(max_length=14, blank=True, null=True)
    shortname = models.CharField(max_length=50, blank=True, null=True)
    item_id = models.CharField(max_length=30, blank=True, null=True)
    results = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_upload_detail'


class LisUploadIndex(models.Model):
    rq = models.CharField(max_length=8, blank=True, null=True)
    appid = models.CharField(max_length=6, blank=True, null=True)
    dh = models.CharField(max_length=14, blank=True, null=True)
    vid = models.CharField(max_length=14, blank=True, null=True)
    accepttime = models.DateField(blank=True, null=True)
    distributetime = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    bj = models.CharField(max_length=50, blank=True, null=True)
    xh = models.IntegerField(blank=True, null=True)
    czy = models.CharField(max_length=6, blank=True, null=True)
    xm = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_upload_index'


class LisWsInterface(models.Model):
    testitem_id = models.CharField(max_length=30, blank=True, null=True)
    bz1 = models.CharField(max_length=50, blank=True, null=True)
    bz2 = models.CharField(max_length=50, blank=True, null=True)
    bz3 = models.CharField(max_length=50, blank=True, null=True)
    bz4 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_ws_interface'


class LisZdyxDict(models.Model):
    billcode = models.CharField(max_length=100, blank=True, null=True)
    testitem_id = models.CharField(max_length=100, blank=True, null=True)
    compare = models.CharField(max_length=100, blank=True, null=True)
    results = models.CharField(max_length=1500, blank=True, null=True)
    bz1 = models.CharField(max_length=600, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    op_datetime = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_zdyx_dict'


class LisZdyxResult(models.Model):
    vid = models.CharField(max_length=100, blank=True, null=True)
    testitem_id = models.CharField(max_length=100, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    xb = models.CharField(max_length=200, blank=True, null=True)
    dwdm = models.CharField(max_length=200, blank=True, null=True)
    dwmc = models.CharField(max_length=200, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    testitem_name_c = models.CharField(max_length=200, blank=True, null=True)
    results = models.CharField(max_length=200, blank=True, null=True)
    normal_l = models.CharField(max_length=200, blank=True, null=True)
    normal_h = models.CharField(max_length=200, blank=True, null=True)
    trans_status = models.CharField(max_length=200, blank=True, null=True)
    djr = models.CharField(max_length=100, blank=True, null=True)
    cid = models.CharField(max_length=100, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    nl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_zdyx_result'


class LisZkPhDict(models.Model):
    id = models.CharField(max_length=10, blank=True, null=True)
    apparatus = models.CharField(max_length=30, blank=True, null=True)
    item_ph = models.CharField(max_length=60, blank=True, null=True)
    kssj = models.DateField(blank=True, null=True)
    jzsj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    zfr_oper = models.CharField(max_length=10, blank=True, null=True)
    zfr_opername = models.CharField(max_length=10, blank=True, null=True)
    bbh = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_zk_ph_dict'


class LisZkResults(models.Model):
    apparatus = models.CharField(max_length=30, blank=True, null=True)
    rq = models.DateField(blank=True, null=True)
    item_ph = models.CharField(max_length=60, blank=True, null=True)
    testitem_id = models.CharField(max_length=30, blank=True, null=True)
    item_value1 = models.CharField(max_length=30, blank=True, null=True)
    item_sd1 = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    item_value2 = models.CharField(max_length=30, blank=True, null=True)
    item_sd2 = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    item_value3 = models.CharField(max_length=30, blank=True, null=True)
    item_sd3 = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    skcl_oper = models.CharField(max_length=30, blank=True, null=True)
    skcl_opername = models.CharField(max_length=60, blank=True, null=True)
    skcl_memo = models.CharField(max_length=200, blank=True, null=True)
    skpj_memo = models.CharField(max_length=200, blank=True, null=True)
    other_memo1 = models.CharField(max_length=200, blank=True, null=True)
    other_memo2 = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    zk_rule = models.CharField(max_length=100, blank=True, null=True)
    zk_skcl = models.CharField(max_length=200, blank=True, null=True)
    clr_oper = models.CharField(max_length=30, blank=True, null=True)
    clr_opername = models.CharField(max_length=30, blank=True, null=True)
    clsj = models.DateField(blank=True, null=True)
    bbh = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_zk_results'


class LisZkZbDict(models.Model):
    id = models.CharField(max_length=10, blank=True, null=True)
    testitem_id = models.CharField(max_length=30, blank=True, null=True)
    testitem_name = models.CharField(max_length=100, blank=True, null=True)
    x_value = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    s_value = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    cv_value = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_zk_zb_dict'


class LogPrintBrowseLog(models.Model):
    id = models.CharField(max_length=250, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)
    cid = models.CharField(max_length=30, blank=True, null=True)
    xm = models.CharField(max_length=200, blank=True, null=True)
    czlx = models.CharField(max_length=200, blank=True, null=True)
    czy = models.CharField(max_length=200, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    cz_computer = models.CharField(max_length=200, blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    bz4 = models.CharField(max_length=200, blank=True, null=True)
    bz5 = models.CharField(max_length=200, blank=True, null=True)
    bz6 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_print_browse_log'


class MnItemLb(models.Model):
    dm = models.CharField(max_length=10, blank=True, null=True)
    mc = models.CharField(max_length=500, blank=True, null=True)
    bzpym = models.CharField(max_length=30, blank=True, null=True)
    lb = models.CharField(max_length=10, blank=True, null=True)
    zyx = models.CharField(max_length=50, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    bz1 = models.CharField(max_length=600, blank=True, null=True)
    bz2 = models.CharField(max_length=600, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    xb = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mn_item_lb'


class MyjyDjList(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    sampleid = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    order_type = models.CharField(max_length=50, blank=True, null=True)
    sample_type = models.CharField(max_length=255, blank=True, null=True)
    kddh = models.CharField(max_length=255, blank=True, null=True)
    kdgs = models.CharField(max_length=255, blank=True, null=True)
    xm = models.CharField(max_length=200, blank=True, null=True)
    xb = models.CharField(max_length=10, blank=True, null=True)
    csrq = models.CharField(max_length=30, blank=True, null=True)
    sfzhm = models.CharField(max_length=100, blank=True, null=True)
    lxdh = models.CharField(max_length=200, blank=True, null=True)
    point_name = models.CharField(max_length=200, blank=True, null=True)
    item_id = models.CharField(max_length=255, blank=True, null=True)
    item_name = models.CharField(max_length=500, blank=True, null=True)
    local_item_id = models.CharField(max_length=10, blank=True, null=True)
    local_item_name = models.CharField(max_length=100, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    djry = models.CharField(max_length=100, blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)
    dwmc = models.CharField(max_length=200, blank=True, null=True)
    qxry = models.CharField(max_length=100, blank=True, null=True)
    qxsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'myjy_dj_list'


class MyjyDzb(models.Model):
    item_id = models.CharField(max_length=255, blank=True, null=True)
    local_item_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'myjy_dzb'


class MyjyItemList(models.Model):
    dm = models.CharField(max_length=250, blank=True, null=True)
    mc = models.CharField(max_length=500, blank=True, null=True)
    yxf = models.CharField(max_length=100, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'myjy_item_list'


class MzMemberCardLog(models.Model):
    id = models.CharField(max_length=200, blank=True, null=True)
    khbh = models.CharField(max_length=200, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    zjlx = models.CharField(max_length=100, blank=True, null=True)
    zjhm = models.CharField(max_length=100, blank=True, null=True)
    xb = models.CharField(max_length=20, blank=True, null=True)
    yddh = models.CharField(max_length=50, blank=True, null=True)
    xf_mzje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    xf_sjje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    qh = models.CharField(max_length=100, blank=True, null=True)
    qje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    qmm = models.CharField(max_length=30, blank=True, null=True)
    cp = models.CharField(max_length=2000, blank=True, null=True)
    zcxzf = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    vid = models.CharField(max_length=20, blank=True, null=True)
    djh = models.CharField(max_length=200, blank=True, null=True)
    bz = models.CharField(max_length=1000, blank=True, null=True)
    czry = models.CharField(max_length=20, blank=True, null=True)
    czry_name = models.CharField(max_length=200, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    ch_czry = models.CharField(max_length=20, blank=True, null=True)
    ch_czry_name = models.CharField(max_length=200, blank=True, null=True)
    chsj = models.DateField(blank=True, null=True)
    cid = models.CharField(max_length=50, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)
    bz4 = models.CharField(max_length=100, blank=True, null=True)
    cardcode = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mz_member_card_log'


class OtherFeeCust(models.Model):
    cust_id = models.CharField(max_length=20, blank=True, null=True)
    member_code = models.CharField(max_length=50, blank=True, null=True)
    tjkrf = models.CharField(max_length=1, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    xb = models.CharField(max_length=3, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    sfzhm = models.CharField(max_length=50, blank=True, null=True)
    dwdm = models.CharField(max_length=50, blank=True, null=True)
    dwmc = models.CharField(max_length=100, blank=True, null=True)
    fgs = models.CharField(max_length=300, blank=True, null=True)
    bm1 = models.CharField(max_length=300, blank=True, null=True)
    bm2 = models.CharField(max_length=300, blank=True, null=True)
    ygh = models.CharField(max_length=100, blank=True, null=True)
    yddh = models.CharField(max_length=20, blank=True, null=True)
    lxdh = models.CharField(max_length=50, blank=True, null=True)
    hyzk = models.CharField(max_length=50, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    djr = models.CharField(max_length=30, blank=True, null=True)
    gj = models.CharField(max_length=50, blank=True, null=True)
    mz = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    yzbm = models.CharField(max_length=50, blank=True, null=True)
    jtzz = models.CharField(max_length=200, blank=True, null=True)
    jws = models.CharField(max_length=3000, blank=True, null=True)
    jbs = models.CharField(max_length=3000, blank=True, null=True)
    bz1 = models.CharField(max_length=3000, blank=True, null=True)
    bz2 = models.CharField(max_length=3000, blank=True, null=True)
    bz3 = models.CharField(max_length=3000, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    ywydm = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    zzys = models.CharField(max_length=30, blank=True, null=True)
    prior_lls = models.CharField(max_length=30, blank=True, null=True)
    prior_mrs = models.CharField(max_length=30, blank=True, null=True)
    cust_kf = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_fee_cust'


class OtherFeeCustDo(models.Model):
    cust_id = models.CharField(max_length=20, blank=True, null=True)
    cust_child_id = models.CharField(max_length=20, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    xb = models.CharField(max_length=3, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    dwdm = models.CharField(max_length=30, blank=True, null=True)
    tjkrf = models.CharField(max_length=1, blank=True, null=True)
    djr = models.CharField(max_length=30, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)
    bz4 = models.CharField(max_length=100, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    llsj = models.DateField(blank=True, null=True)
    ywydm = models.CharField(max_length=20, blank=True, null=True)
    report_status = models.CharField(max_length=20, blank=True, null=True)
    cid = models.CharField(max_length=30, blank=True, null=True)
    zzys = models.CharField(max_length=30, blank=True, null=True)
    cz_dept = models.CharField(max_length=30, blank=True, null=True)
    print_time = models.DateField(blank=True, null=True)
    other_vid = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_fee_cust_do'


class Pbcatcol(models.Model):
    pbc_tnam = models.CharField(max_length=30, blank=True, null=True)
    pbc_tid = models.BigIntegerField(blank=True, null=True)
    pbc_ownr = models.CharField(max_length=30, blank=True, null=True)
    pbc_cnam = models.CharField(max_length=30, blank=True, null=True)
    pbc_cid = models.BigIntegerField(blank=True, null=True)
    pbc_labl = models.CharField(max_length=254, blank=True, null=True)
    pbc_lpos = models.BigIntegerField(blank=True, null=True)
    pbc_hdr = models.CharField(max_length=254, blank=True, null=True)
    pbc_hpos = models.BigIntegerField(blank=True, null=True)
    pbc_jtfy = models.BigIntegerField(blank=True, null=True)
    pbc_mask = models.CharField(max_length=31, blank=True, null=True)
    pbc_case = models.BigIntegerField(blank=True, null=True)
    pbc_hght = models.BigIntegerField(blank=True, null=True)
    pbc_wdth = models.BigIntegerField(blank=True, null=True)
    pbc_ptrn = models.CharField(max_length=31, blank=True, null=True)
    pbc_bmap = models.CharField(max_length=1, blank=True, null=True)
    pbc_init = models.CharField(max_length=254, blank=True, null=True)
    pbc_cmnt = models.CharField(max_length=254, blank=True, null=True)
    pbc_edit = models.CharField(max_length=31, blank=True, null=True)
    pbc_tag = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcatcol'


class Pbcatfmt(models.Model):
    pbf_name = models.CharField(max_length=30, blank=True, null=True)
    pbf_frmt = models.CharField(max_length=254, blank=True, null=True)
    pbf_type = models.BigIntegerField(blank=True, null=True)
    pbf_cntr = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcatfmt'


class Pbcattbl(models.Model):
    pbt_tnam = models.CharField(max_length=30, blank=True, null=True)
    pbt_tid = models.BigIntegerField(blank=True, null=True)
    pbt_ownr = models.CharField(max_length=30, blank=True, null=True)
    pbd_fhgt = models.BigIntegerField(blank=True, null=True)
    pbd_fwgt = models.BigIntegerField(blank=True, null=True)
    pbd_fitl = models.CharField(max_length=1, blank=True, null=True)
    pbd_funl = models.CharField(max_length=1, blank=True, null=True)
    pbd_fchr = models.BigIntegerField(blank=True, null=True)
    pbd_fptc = models.BigIntegerField(blank=True, null=True)
    pbd_ffce = models.CharField(max_length=18, blank=True, null=True)
    pbh_fhgt = models.BigIntegerField(blank=True, null=True)
    pbh_fwgt = models.BigIntegerField(blank=True, null=True)
    pbh_fitl = models.CharField(max_length=1, blank=True, null=True)
    pbh_funl = models.CharField(max_length=1, blank=True, null=True)
    pbh_fchr = models.BigIntegerField(blank=True, null=True)
    pbh_fptc = models.BigIntegerField(blank=True, null=True)
    pbh_ffce = models.CharField(max_length=18, blank=True, null=True)
    pbl_fhgt = models.BigIntegerField(blank=True, null=True)
    pbl_fwgt = models.BigIntegerField(blank=True, null=True)
    pbl_fitl = models.CharField(max_length=1, blank=True, null=True)
    pbl_funl = models.CharField(max_length=1, blank=True, null=True)
    pbl_fchr = models.BigIntegerField(blank=True, null=True)
    pbl_fptc = models.BigIntegerField(blank=True, null=True)
    pbl_ffce = models.CharField(max_length=18, blank=True, null=True)
    pbt_cmnt = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcattbl'


class PwcTemp(models.Model):
    ygh = models.CharField(max_length=30, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pwc_temp'


class QcParameters(models.Model):
    control_id = models.IntegerField(blank=True, null=True)
    traget_yes = models.NullBooleanField()
    control_testid = models.IntegerField(blank=True, null=True)
    control_target = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    control_s = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qc_parameters'


class QcResults(models.Model):
    controldate = models.DateField(blank=True, null=True)
    control_id = models.IntegerField(blank=True, null=True)
    sampleid = models.CharField(max_length=12, blank=True, null=True)
    labsequenceno = models.IntegerField(blank=True, null=True)
    testid = models.IntegerField(blank=True, null=True)
    qc_results = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    testtime = models.DateField(blank=True, null=True)
    qc_operator = models.CharField(max_length=4, blank=True, null=True)
    flag_log = models.NullBooleanField()
    rec_log = models.CharField(max_length=100, blank=True, null=True)
    flag_redo = models.NullBooleanField()
    rec_redo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qc_results'


class QcZkw(models.Model):
    control_id = models.IntegerField(blank=True, null=True)
    control_name = models.CharField(max_length=20, blank=True, null=True)
    control_from = models.CharField(max_length=20, blank=True, null=True)
    control_lotno = models.CharField(max_length=20, blank=True, null=True)
    control_exp = models.DateField(blank=True, null=True)
    log_in_date = models.DateField(blank=True, null=True)
    log_in_name = models.CharField(max_length=4, blank=True, null=True)
    log_off_date = models.DateField(blank=True, null=True)
    log_off_name = models.CharField(max_length=4, blank=True, null=True)
    waylogoff = models.TextField(blank=True, null=True)  # This field type is a guess.
    apparatusid = models.IntegerField(blank=True, null=True)
    zkw_level = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'qc_zkw'


class ReportAbnormityTyyl(models.Model):
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    lb_xh = models.CharField(max_length=10, blank=True, null=True)
    sm_xh = models.CharField(max_length=10, blank=True, null=True)
    sxh = models.CharField(max_length=10, blank=True, null=True)
    xb = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_abnormity_tyyl'


class ReportPrintLog(models.Model):
    id = models.CharField(max_length=200, blank=True, null=True)
    vid = models.CharField(max_length=20, blank=True, null=True)
    lb = models.CharField(max_length=20, blank=True, null=True)
    czry = models.CharField(max_length=200, blank=True, null=True)
    czsj = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_print_log'


class ReportSqList(models.Model):
    billcode = models.CharField(max_length=200, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    sqf = models.CharField(max_length=10, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    czry_oper = models.CharField(max_length=30, blank=True, null=True)
    czry_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    xm = models.CharField(max_length=200, blank=True, null=True)
    xb = models.CharField(max_length=10, blank=True, null=True)
    zfry_oper = models.CharField(max_length=30, blank=True, null=True)
    zfry_name = models.CharField(max_length=100, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)
    bz4 = models.CharField(max_length=100, blank=True, null=True)
    bz5 = models.CharField(max_length=100, blank=True, null=True)
    zfsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_sq_list'


class ReportTjDwList(models.Model):
    dwdm = models.CharField(max_length=30, blank=True, null=True)
    dwmc = models.CharField(max_length=100, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    tjkssj = models.DateField(blank=True, null=True)
    tjjzsj = models.DateField(blank=True, null=True)
    tjrs = models.IntegerField(blank=True, null=True)
    yyid = models.CharField(max_length=30, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    memo = models.CharField(max_length=3000, blank=True, null=True)
    cbgrs = models.IntegerField(blank=True, null=True)
    wdjrs = models.IntegerField(blank=True, null=True)
    man_rs = models.IntegerField(blank=True, null=True)
    woman_rs = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_tj_dw_list'


class ReportTjItemDict(models.Model):
    dm = models.CharField(max_length=30, blank=True, null=True)
    mc = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_tj_item_dict'


class ReportTjItemList(models.Model):
    dwyyid = models.CharField(max_length=30, blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    item_id = models.CharField(max_length=30, blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    item_number = models.BigIntegerField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_tj_item_list'


class ReportTjList(models.Model):
    dwdm = models.CharField(max_length=20, blank=True, null=True)
    dwmc = models.CharField(max_length=100, blank=True, null=True)
    cid = models.CharField(max_length=20, blank=True, null=True)
    vid = models.CharField(max_length=20, blank=True, null=True)
    xm = models.CharField(max_length=60, blank=True, null=True)
    xb = models.CharField(max_length=10, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    xmmc = models.CharField(max_length=100, blank=True, null=True)
    fxmc = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    yyid = models.CharField(max_length=30, blank=True, null=True)
    parent_sxh = models.IntegerField(blank=True, null=True)
    visible = models.CharField(max_length=1, blank=True, null=True)
    results = models.CharField(max_length=100, blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_tj_list'


class ReportZzdyDict(models.Model):
    lb = models.CharField(max_length=200, blank=True, null=True)
    bj = models.CharField(max_length=20, blank=True, null=True)
    je = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_zzdy_dict'


class SaleCustImportLog(models.Model):
    id = models.CharField(max_length=200, blank=True, null=True)
    vid = models.CharField(max_length=20, blank=True, null=True)
    cid = models.CharField(max_length=20, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    xb = models.CharField(max_length=10, blank=True, null=True)
    dwdm = models.CharField(max_length=60, blank=True, null=True)
    dwmc = models.CharField(max_length=200, blank=True, null=True)
    groupid = models.CharField(max_length=100, blank=True, null=True)
    groupname = models.CharField(max_length=200, blank=True, null=True)
    sfzhm = models.CharField(max_length=30, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    czry = models.CharField(max_length=100, blank=True, null=True)
    lx = models.CharField(max_length=100, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)
    other_groupname = models.CharField(max_length=3000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_cust_import_log'


class SaleGroupDetail(models.Model):
    billcode = models.CharField(max_length=30, blank=True, null=True)
    id = models.CharField(max_length=30, blank=True, null=True)
    item_id = models.CharField(max_length=30, blank=True, null=True)
    item_name = models.CharField(max_length=40, blank=True, null=True)
    item_ms = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_group_detail'


class SaleGroupIndex(models.Model):
    billcode = models.CharField(max_length=30, blank=True, null=True)
    id = models.CharField(max_length=30, blank=True, null=True)
    groupname = models.CharField(max_length=100, blank=True, null=True)
    groupid = models.CharField(max_length=60, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.CharField(max_length=1, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    oldprice = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_group_index'


class SaleTjdwCustAddGroup(models.Model):
    billcode = models.CharField(max_length=30, blank=True, null=True)
    cid = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    groupid = models.CharField(max_length=30, blank=True, null=True)
    czry = models.CharField(max_length=100, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    shry = models.CharField(max_length=100, blank=True, null=True)
    shsj = models.CharField(max_length=100, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_tjdw_cust_add_group'


class SmpVddOperationsTable(models.Model):
    request_id = models.IntegerField(blank=True, null=True)
    request_subtype = models.CharField(max_length=128, blank=True, null=True)
    request_type = models.CharField(max_length=128, blank=True, null=True)
    target = models.CharField(max_length=128, blank=True, null=True)
    node = models.CharField(max_length=128, blank=True, null=True)
    user_name = models.CharField(max_length=128, blank=True, null=True)
    owner = models.CharField(max_length=128, blank=True, null=True)
    callback = models.CharField(max_length=128, blank=True, null=True)
    timestamp = models.BigIntegerField(blank=True, null=True)
    outgoing = models.CharField(max_length=1, blank=True, null=True)
    sequence_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdd_operations_table'


class SmpVdeMetricThresholds(models.Model):
    id = models.FloatField(blank=True, null=True)
    metric_id = models.CharField(max_length=2000, blank=True, null=True)
    target_name = models.CharField(max_length=128, blank=True, null=True)
    target_type = models.CharField(max_length=128, blank=True, null=True)
    datasource = models.CharField(max_length=2000, blank=True, null=True)
    event_id = models.FloatField(blank=True, null=True)
    test_id = models.FloatField(blank=True, null=True)
    warning_threshold = models.FloatField(blank=True, null=True)
    alert_threshold = models.FloatField(blank=True, null=True)
    comp_operation = models.FloatField(blank=True, null=True)
    state = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vde_metric_thresholds'


class SmsSend(models.Model):
    id = models.CharField(max_length=200, blank=True, null=True)
    dhhm = models.CharField(max_length=60, blank=True, null=True)
    lx = models.CharField(max_length=60, blank=True, null=True)
    nr = models.CharField(max_length=300, blank=True, null=True)
    oper = models.CharField(max_length=30, blank=True, null=True)
    opername = models.CharField(max_length=100, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    send_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_send'


class SmsSendAgain(models.Model):
    id = models.CharField(max_length=200, blank=True, null=True)
    dhhm = models.CharField(max_length=30, blank=True, null=True)
    lx = models.CharField(max_length=100, blank=True, null=True)
    nr = models.CharField(max_length=1000, blank=True, null=True)
    opername = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    send_date = models.DateField(blank=True, null=True)
    send_opername = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_send_again'


class SmsSendZqbg(models.Model):
    id = models.CharField(max_length=100, blank=True, null=True)
    lb = models.CharField(max_length=1, blank=True, null=True)
    vid = models.CharField(max_length=20, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    sms_date = models.DateField(blank=True, null=True)
    sms_operaname = models.CharField(max_length=100, blank=True, null=True)
    sms_nr = models.CharField(max_length=600, blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_send_zqbg'


class SortRuleOther(models.Model):
    dwdm = models.CharField(max_length=30, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    xmq = models.CharField(max_length=1, blank=True, null=True)
    ch = models.CharField(max_length=1, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sort_rule_other'


class StDamageReason(models.Model):
    dm = models.CharField(max_length=3, blank=True, null=True)
    mc = models.CharField(max_length=30, blank=True, null=True)
    sjdm = models.CharField(max_length=3, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_damage_reason'


class StMaterialCopy(models.Model):
    aid_code = models.CharField(max_length=15, blank=True, null=True)
    dm = models.CharField(max_length=6, blank=True, null=True)
    mc = models.CharField(max_length=80, blank=True, null=True)
    gg = models.CharField(max_length=40, blank=True, null=True)
    dj = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    dw = models.CharField(max_length=10, blank=True, null=True)
    sjdm = models.CharField(max_length=15, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_material_copy'


class StStockAlarm(models.Model):
    ksdm = models.CharField(max_length=6, blank=True, null=True)
    dm = models.CharField(max_length=10, blank=True, null=True)
    zdkc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    zgkc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_stock_alarm'


class StSupply(models.Model):
    dm = models.CharField(max_length=10, blank=True, null=True)
    mc = models.CharField(max_length=80, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    dwdz = models.CharField(max_length=200, blank=True, null=True)
    lxr = models.CharField(max_length=20, blank=True, null=True)
    lxdh = models.CharField(max_length=40, blank=True, null=True)
    yzbm = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_supply'


class SysAutoChange(models.Model):
    lx = models.CharField(max_length=1, blank=True, null=True)
    directory = models.CharField(max_length=400, blank=True, null=True)
    versions = models.CharField(max_length=50, blank=True, null=True)
    is_change = models.CharField(max_length=1, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_auto_change'


class SysBasedict(models.Model):
    moudleid = models.CharField(max_length=6, blank=True, null=True)
    cxsjck = models.CharField(max_length=20, blank=True, null=True)
    llsjck = models.CharField(max_length=20, blank=True, null=True)
    dysjck = models.CharField(max_length=20, blank=True, null=True)
    srsjck = models.CharField(max_length=20, blank=True, null=True)
    jcsjbz = models.CharField(max_length=30, blank=True, null=True)
    zdjs = models.FloatField(blank=True, null=True)
    zdcd = models.FloatField(blank=True, null=True)
    djzdcd = models.FloatField(blank=True, null=True)
    cd1 = models.FloatField(blank=True, null=True)
    cd2 = models.FloatField(blank=True, null=True)
    cd3 = models.FloatField(blank=True, null=True)
    cd4 = models.FloatField(blank=True, null=True)
    cd5 = models.FloatField(blank=True, null=True)
    cd6 = models.FloatField(blank=True, null=True)
    cd7 = models.FloatField(blank=True, null=True)
    cd8 = models.FloatField(blank=True, null=True)
    cd9 = models.FloatField(blank=True, null=True)
    cd10 = models.FloatField(blank=True, null=True)
    sfyjb = models.CharField(max_length=1, blank=True, null=True)
    zjdm = models.CharField(max_length=20, blank=True, null=True)
    zjmc = models.CharField(max_length=20, blank=True, null=True)
    sfzh = models.CharField(max_length=1, blank=True, null=True)
    tablename = models.CharField(max_length=30, blank=True, null=True)
    dkfs = models.CharField(max_length=1, blank=True, null=True)
    op_date = models.DateField(blank=True, null=True)
    record_log = models.CharField(max_length=1, blank=True, null=True)
    move_flag = models.CharField(max_length=1, blank=True, null=True)
    data_column = models.CharField(max_length=20, blank=True, null=True)
    data_code_width = models.FloatField(blank=True, null=True)
    retrieve_type = models.CharField(max_length=1, blank=True, null=True)
    sort_column_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_basedict'


class SysCommReport(models.Model):
    moudleid = models.CharField(max_length=6, blank=True, null=True)
    display_type = models.CharField(max_length=1, blank=True, null=True)
    h_datawindow = models.CharField(max_length=40, blank=True, null=True)
    v_datawindow = models.CharField(max_length=40, blank=True, null=True)
    data_store_name = models.CharField(max_length=40, blank=True, null=True)
    h_datawindow_code = models.CharField(max_length=20, blank=True, null=True)
    h_datawindow_name = models.CharField(max_length=20, blank=True, null=True)
    v_datawindow_code = models.CharField(max_length=20, blank=True, null=True)
    v_datawindow_name = models.CharField(max_length=20, blank=True, null=True)
    data_h_code = models.CharField(max_length=20, blank=True, null=True)
    data_v_code = models.CharField(max_length=20, blank=True, null=True)
    display_code_ornot = models.CharField(max_length=1, blank=True, null=True)
    code_length = models.FloatField(blank=True, null=True)
    name_length = models.FloatField(blank=True, null=True)
    left_space = models.FloatField(blank=True, null=True)
    dec_position = models.FloatField(blank=True, null=True)
    value_length = models.FloatField(blank=True, null=True)
    title_code = models.FloatField(blank=True, null=True)
    rq_title = models.CharField(max_length=50, blank=True, null=True)
    rq_column_start = models.CharField(max_length=30, blank=True, null=True)
    rq_column_end = models.CharField(max_length=30, blank=True, null=True)
    find_dw = models.CharField(max_length=30, blank=True, null=True)
    h_title = models.CharField(max_length=30, blank=True, null=True)
    v_title = models.CharField(max_length=30, blank=True, null=True)
    window_title = models.CharField(max_length=50, blank=True, null=True)
    data_value_column = models.CharField(max_length=30, blank=True, null=True)
    otherwhereclause = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_comm_report'


class SysCooperationConnectparm(models.Model):
    cooperationmechanism = models.CharField(max_length=30, blank=True, null=True)
    connecttype = models.CharField(max_length=30, blank=True, null=True)
    connectdrive = models.CharField(max_length=50, blank=True, null=True)
    connectaddress = models.CharField(max_length=50, blank=True, null=True)
    connecttoname = models.CharField(max_length=50, blank=True, null=True)
    userid = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_cooperation_connectparm'


class SysCzLog2018(models.Model):
    id = models.CharField(max_length=200, blank=True, null=True)
    lx = models.CharField(max_length=100, blank=True, null=True)
    vid = models.CharField(max_length=20, blank=True, null=True)
    cid = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=200, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    czy = models.CharField(max_length=30, blank=True, null=True)
    czy_name = models.CharField(max_length=150, blank=True, null=True)
    nr = models.CharField(max_length=400, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_cz_log2018'


class SysDatawindowSyntax(models.Model):
    datawindowname = models.CharField(max_length=50, blank=True, null=True)
    dwdesc = models.CharField(max_length=200, blank=True, null=True)
    syntax = models.BinaryField(blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    aid_code = models.CharField(max_length=6, blank=True, null=True)
    sjdm = models.CharField(max_length=6, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_datawindow_syntax'


class SysErrorlog(models.Model):
    errorid = models.BigIntegerField(blank=True, null=True)
    errornumber = models.BigIntegerField(blank=True, null=True)
    messagename = models.CharField(max_length=200, blank=True, null=True)
    objectname = models.CharField(max_length=200, blank=True, null=True)
    wherename = models.CharField(max_length=200, blank=True, null=True)
    eventname = models.CharField(max_length=200, blank=True, null=True)
    linename = models.BigIntegerField(blank=True, null=True)
    happendate = models.DateField(blank=True, null=True)
    env = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_errorlog'


class SysFdjTzLog(models.Model):
    id = models.CharField(max_length=200, blank=True, null=True)
    jzdhm = models.CharField(max_length=200, blank=True, null=True)
    vid = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    xb = models.CharField(max_length=50, blank=True, null=True)
    dwdm = models.CharField(max_length=50, blank=True, null=True)
    old_xj = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    old_zp = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    old_xyk = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    old_lpk = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    old_ybk = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    old_gz = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    old_djq = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    old_other1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    old_other2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    new_xj = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    new_zp = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    new_xyk = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    new_lpk = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    new_ybk = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    new_gz = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    new_djq = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    new_other1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    new_other2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    czy = models.CharField(max_length=100, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    yy = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_fdj_tz_log'


class SysFind(models.Model):
    moudleid = models.CharField(max_length=6, blank=True, null=True)
    filterdwname = models.CharField(max_length=30, blank=True, null=True)
    listdwname = models.CharField(max_length=30, blank=True, null=True)
    otherwhereclause = models.CharField(max_length=100, blank=True, null=True)
    dbclickwindow = models.CharField(max_length=30, blank=True, null=True)
    parm1 = models.CharField(max_length=30, blank=True, null=True)
    parm2 = models.CharField(max_length=30, blank=True, null=True)
    parm3 = models.CharField(max_length=30, blank=True, null=True)
    parm4 = models.CharField(max_length=30, blank=True, null=True)
    otherparm = models.CharField(max_length=30, blank=True, null=True)
    windowtitle = models.CharField(max_length=40, blank=True, null=True)
    orientation = models.CharField(max_length=1, blank=True, null=True)
    doubletype = models.CharField(max_length=1, blank=True, null=True)
    op_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_find'


class SysFphmszb(models.Model):
    user_id = models.CharField(max_length=6, blank=True, null=True)
    dqfphm = models.CharField(max_length=15, blank=True, null=True)
    ksfphm = models.CharField(max_length=15, blank=True, null=True)
    zzfphm = models.CharField(max_length=15, blank=True, null=True)
    hmlx = models.CharField(max_length=1, blank=True, null=True)
    lysj = models.DateField(blank=True, null=True)
    bz = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_fphmszb'


class SysItemBw(models.Model):
    item_id = models.CharField(max_length=30, blank=True, null=True)
    bw = models.CharField(max_length=200, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_item_bw'


class SysItemGl(models.Model):
    id = models.CharField(max_length=100, blank=True, null=True)
    item_id = models.CharField(max_length=100, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_item_gl'


class SysJbbLog(models.Model):
    dm = models.CharField(max_length=12, blank=True, null=True)
    table_name = models.CharField(max_length=30, blank=True, null=True)
    col_name = models.CharField(max_length=40, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    pri_name1 = models.CharField(max_length=30, blank=True, null=True)
    pri_key = models.CharField(max_length=30, blank=True, null=True)
    pri_name2 = models.CharField(max_length=30, blank=True, null=True)
    pri_key2 = models.CharField(max_length=40, blank=True, null=True)
    old_value = models.CharField(max_length=60, blank=True, null=True)
    new_value = models.CharField(max_length=60, blank=True, null=True)
    operator = models.CharField(max_length=6, blank=True, null=True)
    operation_time = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=16, blank=True, null=True)
    operator_name = models.CharField(max_length=10, blank=True, null=True)
    machine_name = models.CharField(max_length=20, blank=True, null=True)
    mkid = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_jbb_log'


class SysKhReport(models.Model):
    id = models.CharField(max_length=100, blank=True, null=True)
    js_date = models.DateField(blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    js_name = models.CharField(max_length=50, blank=True, null=True)
    class_code = models.CharField(max_length=8, blank=True, null=True)
    memo = models.CharField(max_length=100, blank=True, null=True)
    memo1 = models.CharField(max_length=100, blank=True, null=True)
    memo2 = models.CharField(max_length=100, blank=True, null=True)
    memo3 = models.CharField(max_length=100, blank=True, null=True)
    operatorno = models.CharField(max_length=50, blank=True, null=True)
    dm = models.CharField(max_length=12, blank=True, null=True)
    table_name = models.CharField(max_length=30, blank=True, null=True)
    col_name = models.CharField(max_length=40, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    pri_key = models.CharField(max_length=30, blank=True, null=True)
    factory = models.CharField(max_length=10, blank=True, null=True)
    operatorname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_kh_report'


class SysLjzxSetup(models.Model):
    code_value = models.CharField(max_length=30, blank=True, null=True)
    sjf = models.CharField(max_length=1, blank=True, null=True)
    dydm = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_ljzx_setup'


class SysMoudle(models.Model):
    moudleid = models.CharField(max_length=6, blank=True, null=True)
    moudlename = models.CharField(max_length=30, blank=True, null=True)
    sjdm = models.CharField(max_length=6, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    mkbz = models.CharField(max_length=100, blank=True, null=True)
    mkckmc = models.CharField(max_length=30, blank=True, null=True)
    dkfs = models.CharField(max_length=1, blank=True, null=True)
    cs1 = models.CharField(max_length=20, blank=True, null=True)
    cs2 = models.CharField(max_length=20, blank=True, null=True)
    sxh = models.FloatField(blank=True, null=True)
    cs_bs = models.CharField(max_length=1, blank=True, null=True)
    op_date = models.DateField(blank=True, null=True)
    orientation = models.CharField(max_length=1, blank=True, null=True)
    print_type = models.CharField(max_length=1, blank=True, null=True)
    paper_size = models.FloatField(blank=True, null=True)
    paper_length = models.FloatField(blank=True, null=True)
    paper_width = models.FloatField(blank=True, null=True)
    left_margin = models.FloatField(blank=True, null=True)
    right_margin = models.FloatField(blank=True, null=True)
    top_margin = models.FloatField(blank=True, null=True)
    bottom_margin = models.FloatField(blank=True, null=True)
    ick_bz = models.CharField(max_length=1, blank=True, null=True)
    token = models.CharField(max_length=1, blank=True, null=True)
    bmpinit = models.BinaryField(blank=True, null=True)
    bmpopen = models.BinaryField(blank=True, null=True)
    bmpselected = models.BinaryField(blank=True, null=True)
    bmp_path = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_moudle'


class SysPaperDict(models.Model):
    paper_size = models.FloatField(blank=True, null=True)
    paper_memo = models.CharField(max_length=80, blank=True, null=True)
    paper_heigth = models.FloatField(blank=True, null=True)
    paper_width = models.CharField(max_length=5, blank=True, null=True)
    is_valid = models.CharField(max_length=1, blank=True, null=True)
    op_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_paper_dict'


class SysPicServerSetup(models.Model):
    ip = models.CharField(max_length=20, blank=True, null=True)
    port_number = models.IntegerField(blank=True, null=True)
    login_user = models.CharField(max_length=20, blank=True, null=True)
    login_pass = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_pic_server_setup'


class SysQueue(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    dept_code = models.CharField(max_length=6, blank=True, null=True)
    item_id = models.CharField(max_length=6, blank=True, null=True)
    settime = models.DateField(blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sort_xm = models.CharField(max_length=20, blank=True, null=True)
    sort_xb = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_queue'


class SysReportTitle(models.Model):
    id = models.FloatField(blank=True, null=True)
    dw_name = models.CharField(max_length=30, blank=True, null=True)
    moudle_name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=60, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    flag = models.CharField(max_length=5, blank=True, null=True)
    moudleid = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_report_title'


class SysRole(models.Model):
    roleid = models.CharField(max_length=6, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_role'


class SysRoleright(models.Model):
    roleid = models.CharField(max_length=6, blank=True, null=True)
    user_type = models.CharField(max_length=1, blank=True, null=True)
    moudleid = models.CharField(max_length=6, blank=True, null=True)
    isselect = models.CharField(max_length=1, blank=True, null=True)
    is_audit = models.CharField(max_length=1, blank=True, null=True)
    is_input = models.CharField(max_length=1, blank=True, null=True)
    is_print = models.CharField(max_length=1, blank=True, null=True)
    op_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_roleright'


class SysRzList(models.Model):
    userid = models.CharField(max_length=20, blank=True, null=True)
    rz_code = models.CharField(max_length=200, blank=True, null=True)
    rq = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    rz_date = models.DateField(blank=True, null=True)
    out_date = models.DateField(blank=True, null=True)
    out_czy = models.CharField(max_length=100, blank=True, null=True)
    mac_address = models.CharField(max_length=300, blank=True, null=True)
    fw_code = models.CharField(max_length=300, blank=True, null=True)
    bz1 = models.CharField(max_length=300, blank=True, null=True)
    bz2 = models.CharField(max_length=300, blank=True, null=True)
    bz3 = models.CharField(max_length=300, blank=True, null=True)
    ct = models.CharField(max_length=1, blank=True, null=True)
    hc = models.CharField(max_length=1, blank=True, null=True)
    fs = models.CharField(max_length=1, blank=True, null=True)
    wj = models.CharField(max_length=1, blank=True, null=True)
    cz_lx1 = models.CharField(max_length=100, blank=True, null=True)
    cz_lx2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_rz_list'


class SysRzNoLimit(models.Model):
    rq = models.CharField(max_length=10, blank=True, null=True)
    in_factory = models.CharField(max_length=10, blank=True, null=True)
    no_limit_code = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_rz_no_limit'


# 预约短信模板
class SysSmsDict(models.Model):
    userid = models.CharField(max_length=50, blank=True, null=True)
    userpass = models.CharField(max_length=50, blank=True, null=True)
    qydm = models.CharField(max_length=50, blank=True, null=True)
    cpbh = models.CharField(max_length=50, blank=True, null=True)
    yy_mb = models.CharField(max_length=700, blank=True, null=True)
    bg_mb = models.CharField(max_length=700, blank=True, null=True)
    qt1_mb = models.CharField(max_length=700, blank=True, null=True)
    qt2_mb = models.CharField(max_length=700, blank=True, null=True)
    qt3_mb = models.CharField(max_length=700, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_sms_dict'


class SysSrControlDict(models.Model):
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    bz1 = models.CharField(max_length=300, blank=True, null=True)
    bz2 = models.CharField(max_length=300, blank=True, null=True)
    bz3 = models.CharField(max_length=300, blank=True, null=True)
    bz4 = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_sr_control_dict'


class SysSyncDict(models.Model):
    sync_ip = models.CharField(max_length=80, blank=True, null=True)
    sync_user = models.CharField(max_length=10, blank=True, null=True)
    sync_passwd = models.CharField(max_length=10, blank=True, null=True)
    sync_status = models.CharField(max_length=1, blank=True, null=True)
    port_number = models.IntegerField(blank=True, null=True)
    emergency = models.CharField(max_length=1, blank=True, null=True)
    vip_sort_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    vip_ornot = models.CharField(max_length=1, blank=True, null=True)
    cxhs_rs = models.IntegerField(blank=True, null=True)
    cxhs_rs_sc = models.IntegerField(blank=True, null=True)
    pt_cyrs = models.IntegerField(blank=True, null=True)
    vip_cyrs = models.IntegerField(blank=True, null=True)
    vip_yjk_number = models.IntegerField(blank=True, null=True)
    sc_change = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_sync_dict'


class SysSystemSync(models.Model):
    path = models.CharField(max_length=100, blank=True, null=True)
    filename = models.CharField(max_length=50, blank=True, null=True)
    op_date = models.DateField(blank=True, null=True)
    sync = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_system_sync'


class SysTableChange(models.Model):
    id = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    bz = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_table_change'


class SysTableDesc(models.Model):
    id = models.CharField(max_length=6, blank=True, null=True)
    table_name = models.CharField(max_length=20, blank=True, null=True)
    table_comment = models.CharField(max_length=30, blank=True, null=True)
    field_name = models.CharField(max_length=30, blank=True, null=True)
    field_comment = models.CharField(max_length=60, blank=True, null=True)
    edit_style = models.CharField(max_length=1, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    zcz_xx = models.CharField(max_length=20, blank=True, null=True)
    zcz_sx = models.CharField(max_length=20, blank=True, null=True)
    font_style = models.CharField(max_length=1, blank=True, null=True)
    fill_stype = models.CharField(max_length=1, blank=True, null=True)
    or_init = models.CharField(max_length=300, blank=True, null=True)
    brf = models.CharField(max_length=1, blank=True, null=True)
    column_type = models.CharField(max_length=1, blank=True, null=True)
    in_results = models.CharField(max_length=1, blank=True, null=True)
    dw = models.CharField(max_length=30, blank=True, null=True)
    column_height = models.IntegerField(blank=True, null=True)
    column_width = models.IntegerField(blank=True, null=True)
    column_sxh = models.IntegerField(blank=True, null=True)
    column_data_type = models.CharField(max_length=10, blank=True, null=True)
    column_format = models.CharField(max_length=15, blank=True, null=True)
    is_print = models.CharField(max_length=1, blank=True, null=True)
    print_height = models.BigIntegerField(blank=True, null=True)
    desc_sex = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_table_desc'


class SysTemplet(models.Model):
    tempid = models.CharField(max_length=20, blank=True, null=True)
    id = models.CharField(max_length=6, blank=True, null=True)
    templetename = models.CharField(max_length=80, blank=True, null=True)
    userid = models.CharField(max_length=6, blank=True, null=True)
    dept_code = models.CharField(max_length=6, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    mbms = models.CharField(max_length=2000, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    sxh = models.FloatField(blank=True, null=True)
    mbms_ft = models.CharField(max_length=2000, blank=True, null=True)
    mbms_english = models.CharField(max_length=2000, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=10, blank=True, null=True)
    templetename_ft = models.CharField(max_length=80, blank=True, null=True)
    templetename_en = models.CharField(max_length=80, blank=True, null=True)
    sjdm = models.CharField(max_length=20, blank=True, null=True)
    advice_type = models.CharField(max_length=1, blank=True, null=True)
    advice_title = models.CharField(max_length=80, blank=True, null=True)
    advice_context = models.CharField(max_length=1000, blank=True, null=True)
    value_xx = models.CharField(max_length=30, blank=True, null=True)
    value_sx = models.CharField(max_length=30, blank=True, null=True)
    sfjb = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_templet'


# 医生模板表
class SysTemplet2014(models.Model):
    tempid = models.CharField(max_length=20, blank=True, null=True)
    id = models.CharField(max_length=6, blank=True, null=True)
    templetename = models.CharField(max_length=200, blank=True, null=True)
    userid = models.CharField(max_length=6, blank=True, null=True)
    dept_code = models.CharField(max_length=6, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    mbms = models.CharField(max_length=2000, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    sxh = models.FloatField(blank=True, null=True)
    mbms_ft = models.CharField(max_length=2000, blank=True, null=True)
    mbms_english = models.CharField(max_length=2000, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=10, blank=True, null=True)
    templetename_ft = models.CharField(max_length=80, blank=True, null=True)
    templetename_en = models.CharField(max_length=80, blank=True, null=True)
    sjdm = models.CharField(max_length=20, blank=True, null=True)
    advice_type = models.CharField(max_length=1, blank=True, null=True)
    advice_title = models.CharField(max_length=80, blank=True, null=True)
    advice_context = models.CharField(max_length=1000, blank=True, null=True)
    value_xx = models.CharField(max_length=30, blank=True, null=True)
    value_sx = models.CharField(max_length=30, blank=True, null=True)
    sfjb = models.CharField(max_length=1, blank=True, null=True)
    ycbw = models.CharField(max_length=200, blank=True, null=True)
    jbbt = models.CharField(max_length=300, blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    temp_bz1 = models.CharField(max_length=300, blank=True, null=True)
    temp_bz2 = models.CharField(max_length=300, blank=True, null=True)
    temp_bz3 = models.CharField(max_length=300, blank=True, null=True)
    temp_bz4 = models.CharField(max_length=300, blank=True, null=True)
    temp_bz5 = models.CharField(max_length=300, blank=True, null=True)
    temp_bz6 = models.CharField(max_length=300, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    temp_bz7 = models.CharField(max_length=300, blank=True, null=True)
    yxlb = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_templet_2014'


class SysTempletXxxxxy(models.Model):
    tempid = models.CharField(max_length=20, blank=True, null=True)
    id = models.CharField(max_length=6, blank=True, null=True)
    templetename = models.CharField(max_length=80, blank=True, null=True)
    userid = models.CharField(max_length=6, blank=True, null=True)
    dept_code = models.CharField(max_length=6, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    mbms = models.CharField(max_length=2000, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    sxh = models.FloatField(blank=True, null=True)
    mbms_ft = models.CharField(max_length=2000, blank=True, null=True)
    mbms_english = models.CharField(max_length=2000, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=10, blank=True, null=True)
    templetename_ft = models.CharField(max_length=80, blank=True, null=True)
    templetename_en = models.CharField(max_length=80, blank=True, null=True)
    sjdm = models.CharField(max_length=20, blank=True, null=True)
    advice_type = models.CharField(max_length=1, blank=True, null=True)
    advice_title = models.CharField(max_length=80, blank=True, null=True)
    advice_context = models.CharField(max_length=1000, blank=True, null=True)
    value_xx = models.CharField(max_length=30, blank=True, null=True)
    value_sx = models.CharField(max_length=30, blank=True, null=True)
    sfjb = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_templet_xxxxxy'


# 传输表描述
class SysTransDict(models.Model):
    aid_code = models.CharField(max_length=20, blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    table_name = models.CharField(max_length=50, blank=True, null=True)
    table_ch_name = models.CharField(max_length=50, blank=True, null=True)
    key_name1 = models.CharField(max_length=30, blank=True, null=True)
    key_name2 = models.CharField(max_length=30, blank=True, null=True)
    key_name3 = models.CharField(max_length=30, blank=True, null=True)
    key_name4 = models.CharField(max_length=30, blank=True, null=True)
    key_name5 = models.CharField(max_length=30, blank=True, null=True)
    down_trans = models.CharField(max_length=1, blank=True, null=True)
    up_trans = models.CharField(max_length=1, blank=True, null=True)
    trans_status_column = models.CharField(max_length=30, blank=True, null=True)
    down_date_column = models.CharField(max_length=30, blank=True, null=True)
    trans_num = models.FloatField(blank=True, null=True)
    trans_type = models.CharField(max_length=1, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    prior_down_date = models.DateField(blank=True, null=True)
    up_whereclause = models.CharField(max_length=250, blank=True, null=True)
    down_whereclause = models.CharField(max_length=250, blank=True, null=True)
    sjdm = models.CharField(max_length=18, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    oper_date = models.DateField(blank=True, null=True)
    index_table_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_trans_dict'


class SysUserRole(models.Model):
    roleid = models.CharField(max_length=6, blank=True, null=True)
    userid = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_role'


class SysUserRz(models.Model):
    userid = models.CharField(max_length=20, blank=True, null=True)
    rz_code = models.CharField(max_length=200, blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_rz'


class SysUserinformation(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    shortname = models.CharField(max_length=50, blank=True, null=True)
    e_mail = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=18, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    fac_fix = models.CharField(max_length=3, blank=True, null=True)
    z_ipaddress = models.CharField(max_length=20, blank=True, null=True)
    z_ftp_user = models.CharField(max_length=20, blank=True, null=True)
    z_ftp_passwd = models.CharField(max_length=20, blank=True, null=True)
    z_file_path = models.CharField(max_length=100, blank=True, null=True)
    f_file_path = models.CharField(max_length=100, blank=True, null=True)
    z_hostname = models.CharField(max_length=30, blank=True, null=True)
    sync_ip = models.CharField(max_length=80, blank=True, null=True)
    sync_user = models.CharField(max_length=10, blank=True, null=True)
    sync_passwd = models.CharField(max_length=10, blank=True, null=True)
    sync_status = models.CharField(max_length=1, blank=True, null=True)
    ftp_port_number = models.IntegerField(blank=True, null=True)
    display_compare = models.CharField(max_length=1, blank=True, null=True)
    other_line = models.CharField(max_length=5, blank=True, null=True)
    sc_change = models.CharField(max_length=1, blank=True, null=True)
    zj_xhshf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_userinformation'


# 用户日志
class SysUserlog(models.Model):
    loginid = models.BigIntegerField(blank=True, null=True)
    userid = models.CharField(max_length=6, blank=True, null=True)
    username = models.CharField(max_length=10, blank=True, null=True)
    logintime = models.DateField(blank=True, null=True)
    logouttime = models.DateField(blank=True, null=True)
    deptno = models.CharField(max_length=6, blank=True, null=True)
    deptname = models.CharField(max_length=40, blank=True, null=True)
    workstation = models.CharField(max_length=30, blank=True, null=True)
    moduleid = models.CharField(max_length=6, blank=True, null=True)
    modulename = models.CharField(max_length=30, blank=True, null=True)
    isnormal = models.CharField(max_length=1, blank=True, null=True)
    ipaddress = models.CharField(max_length=20, blank=True, null=True)
    machinename = models.CharField(max_length=30, blank=True, null=True)
    tcf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_userlog'


class SysValidCode(models.Model):
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    valid_code = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_valid_code'


class SysVersionFile(models.Model):
    userid = models.CharField(max_length=4, blank=True, null=True)
    workstation = models.CharField(max_length=1, blank=True, null=True)
    filepath = models.CharField(max_length=30, blank=True, null=True)
    filename = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_version_file'


class SysVersionSet(models.Model):
    cur_version = models.CharField(max_length=10, blank=True, null=True)
    update_lx = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_version_set'


class SysVersionUpdate(models.Model):
    filename = models.CharField(max_length=30, blank=True, null=True)
    filesize = models.IntegerField(blank=True, null=True)
    version = models.CharField(max_length=10, blank=True, null=True)
    userid = models.CharField(max_length=4, blank=True, null=True)
    workstation = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_version_update'


# 异常部位表
class SysYcBw2014(models.Model):
    bw = models.CharField(max_length=100, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    yxf = models.CharField(max_length=10, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_yc_bw_2014'


class SysZdwhBas(models.Model):
    moudleid = models.CharField(max_length=6, blank=True, null=True)
    whmc = models.CharField(max_length=30, blank=True, null=True)
    dwbrowse = models.CharField(max_length=30, blank=True, null=True)
    dwdict = models.CharField(max_length=30, blank=True, null=True)
    dwgoal = models.CharField(max_length=30, blank=True, null=True)
    browsekey = models.CharField(max_length=20, blank=True, null=True)
    dictkey = models.CharField(max_length=20, blank=True, null=True)
    goalkey1 = models.CharField(max_length=20, blank=True, null=True)
    goalkey2 = models.CharField(max_length=20, blank=True, null=True)
    dictmc = models.CharField(max_length=20, blank=True, null=True)
    goalmc = models.CharField(max_length=20, blank=True, null=True)
    browsemc = models.CharField(max_length=20, blank=True, null=True)
    browsekeymc = models.CharField(max_length=20, blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    parentdw = models.CharField(max_length=20, blank=True, null=True)
    parentkey = models.CharField(max_length=20, blank=True, null=True)
    parentkeymc = models.CharField(max_length=20, blank=True, null=True)
    comparekey = models.CharField(max_length=20, blank=True, null=True)
    multi_row = models.CharField(max_length=1, blank=True, null=True)
    find_type = models.CharField(max_length=1, blank=True, null=True)
    find_dwname = models.CharField(max_length=40, blank=True, null=True)
    op_date = models.DateField(blank=True, null=True)
    expand_column = models.CharField(max_length=30, blank=True, null=True)
    edit_level = models.FloatField(blank=True, null=True)
    record_log = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_zdwh_bas'


class TempRy(models.Model):
    gh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bm = models.CharField(max_length=50, blank=True, null=True)
    xb = models.CharField(max_length=50, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_ry'


class XyTraceLog(models.Model):
    billcode = models.CharField(max_length=200, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)
    item_id = models.CharField(max_length=300, blank=True, null=True)
    czlb = models.CharField(max_length=300, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    point_name = models.CharField(max_length=300, blank=True, null=True)
    cid = models.CharField(max_length=60, blank=True, null=True)
    xm = models.CharField(max_length=300, blank=True, null=True)
    xb = models.CharField(max_length=10, blank=True, null=True)
    czlx = models.CharField(max_length=1000, blank=True, null=True)
    cznr = models.CharField(max_length=4000, blank=True, null=True)
    zkf = models.CharField(max_length=10, blank=True, null=True)
    czry = models.CharField(max_length=200, blank=True, null=True)
    shry = models.CharField(max_length=200, blank=True, null=True)
    trans_status = models.CharField(max_length=200, blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    bz4 = models.CharField(max_length=200, blank=True, null=True)
    bz5 = models.CharField(max_length=200, blank=True, null=True)
    log_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xy_trace_log'


class YyFactoryYyyRs(models.Model):
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    rs = models.BigIntegerField(blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    a = models.BigIntegerField(blank=True, null=True)
    b = models.BigIntegerField(blank=True, null=True)
    c = models.BigIntegerField(blank=True, null=True)
    d = models.BigIntegerField(blank=True, null=True)
    e = models.BigIntegerField(blank=True, null=True)
    f = models.BigIntegerField(blank=True, null=True)
    g = models.BigIntegerField(blank=True, null=True)
    h = models.BigIntegerField(blank=True, null=True)
    qt = models.BigIntegerField(blank=True, null=True)
    cthc_yyy = models.BigIntegerField(blank=True, null=True)
    cthc_kyy = models.BigIntegerField(blank=True, null=True)
    xw_yyy = models.BigIntegerField(blank=True, null=True)
    xw_kyy = models.BigIntegerField(blank=True, null=True)
    hc_yyy = models.BigIntegerField(blank=True, null=True)
    vip_kyy = models.IntegerField(blank=True, null=True)
    vip_yyy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yy_factory_yyy_rs'


class YypqLsyyDict(models.Model):
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    rq = models.DateField(blank=True, null=True)
    lsrs = models.BigIntegerField(blank=True, null=True)
    ls1 = models.CharField(max_length=2000, blank=True, null=True)
    cthc_kyy = models.BigIntegerField(blank=True, null=True)
    xw_kyy = models.BigIntegerField(blank=True, null=True)
    hc_kyy = models.BigIntegerField(blank=True, null=True)
    vip_kyyrs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yypq_lsyy_dict'


class ZjScshGzl(models.Model):
    vid = models.CharField(max_length=30, blank=True, null=True)
    lb = models.CharField(max_length=100, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    opername = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zj_scsh_gzl'


class ZjYsqmDict(models.Model):
    id = models.CharField(max_length=200, blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    kssj = models.DateField(blank=True, null=True)
    jzsj = models.DateField(blank=True, null=True)
    jc_oper = models.CharField(max_length=100, blank=True, null=True)
    audit_oper = models.CharField(max_length=100, blank=True, null=True)
    jc_bmp = models.BinaryField(blank=True, null=True)
    audit_blob = models.BinaryField(blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zj_ysqm_dict'


class ZkccdCzb(models.Model):
    item_id = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"项目ID")
    partid = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"部位ID")

    class Meta:
        managed = False
        db_table = 'zkccd_czb'


class ZkccdPart(models.Model):
    partid = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"部位ID")
    part = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"部位名称")

    class Meta:
        managed = False
        db_table = 'zkccd_part'


class ZyCommJcResult(models.Model):
    item_id = models.CharField(max_length=80, blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    table_id = models.CharField(max_length=6, blank=True, null=True)
    field_comment = models.CharField(max_length=60, blank=True, null=True)
    field_results = models.CharField(max_length=3500, blank=True, null=True)
    zcz_xx = models.CharField(max_length=20, blank=True, null=True)
    zcz_sx = models.CharField(max_length=20, blank=True, null=True)
    dw = models.CharField(max_length=20, blank=True, null=True)
    in_results = models.CharField(max_length=1, blank=True, null=True)
    column_height = models.IntegerField(blank=True, null=True)
    column_width = models.IntegerField(blank=True, null=True)
    column_data_type = models.CharField(max_length=10, blank=True, null=True)
    column_data_format = models.CharField(max_length=15, blank=True, null=True)
    column_sxh = models.IntegerField(blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    init_results = models.CharField(max_length=500, blank=True, null=True)
    sf_yx = models.CharField(max_length=1, blank=True, null=True)
    column_type = models.CharField(max_length=1, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    field_name = models.CharField(max_length=30, blank=True, null=True)
    is_print = models.CharField(max_length=1, blank=True, null=True)
    print_height = models.BigIntegerField(blank=True, null=True)
    table_name = models.CharField(max_length=50, blank=True, null=True)
    table_sxh = models.IntegerField(blank=True, null=True)
    in_factroy = models.CharField(max_length=30, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    czy = models.CharField(max_length=30, blank=True, null=True)
    czy_name = models.CharField(max_length=30, blank=True, null=True)
    cz_dept = models.CharField(max_length=30, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zy_comm_jc_result'


class ZybInterfaceList(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    barcode = models.CharField(max_length=50, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zyb_interface_list'
