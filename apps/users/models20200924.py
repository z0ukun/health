# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


#
class AccCustAccountList(models.Model):
    billcode = models.CharField(max_length=14, blank=True, null=True)
    cid = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"CID")
    xm = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"姓名")
    xb = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"性别")
    czlx = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"姓名")
    zjbz = models.IntegerField(blank=True, null=True, verbose_name=u"姓名")
    fkfs = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"姓名")
    jnje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"姓名")
    hl = models.IntegerField(blank=True, null=True, verbose_name=u"姓名")
    czje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"姓名")
    ye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"姓名")
    czy = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"姓名")
    czsj = models.DateField(blank=True, null=True, verbose_name=u"姓名")
    fphm = models.CharField(max_length=14, blank=True, null=True, verbose_name=u"姓名")
    dydh = models.CharField(max_length=14, blank=True, null=True, verbose_name=u"姓名")
    dyf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"姓名")
    dyr = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"姓名")
    dysj = models.DateField(blank=True, null=True, verbose_name=u"姓名")
    dw_gr = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"姓名")
    lb = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"姓名")
    sjje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"姓名")
    ywydm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"姓名")
    khly = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"姓名")
    deal_type = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"姓名")
    trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"姓名")
    other_bl = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True, verbose_name=u"姓名")
    in_factory = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"姓名")

    class Meta:
        managed = False
        db_table = 'acc_cust_account_list'
        verbose_name = u"AccCustAccountList"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.billcode


class AccountGiftCard(models.Model):
    card_code = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=60, blank=True, null=True)
    ye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    scclsj = models.DateField(blank=True, null=True)
    scclje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    memo = models.CharField(max_length=20, blank=True, null=True)
    zjbz = models.IntegerField(blank=True, null=True)
    kmje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ywydm = models.CharField(max_length=6, blank=True, null=True)
    hhly = models.CharField(max_length=6, blank=True, null=True)
    card_type = models.CharField(max_length=1, blank=True, null=True)
    groupid = models.CharField(max_length=6, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    user_password = models.CharField(max_length=10, blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_gift_card'


class AccountGiftList(models.Model):
    billcode = models.CharField(max_length=14, blank=True, null=True)
    card_code = models.CharField(max_length=12, blank=True, null=True)
    bz = models.CharField(max_length=20, blank=True, null=True)
    je = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lx = models.CharField(max_length=2, blank=True, null=True)
    dydh = models.CharField(max_length=14, blank=True, null=True)
    czry = models.CharField(max_length=6, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    kye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    zjbz = models.IntegerField(blank=True, null=True)
    fkfs = models.CharField(max_length=2, blank=True, null=True)
    sjje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    card_type = models.CharField(max_length=1, blank=True, null=True)
    kjcs = models.IntegerField(blank=True, null=True)
    sjcs = models.IntegerField(blank=True, null=True)
    groupid = models.CharField(max_length=6, blank=True, null=True)
    ywydm = models.CharField(max_length=6, blank=True, null=True)
    khly = models.CharField(max_length=6, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    dwdm = models.CharField(max_length=20, blank=True, null=True)
    dwmc = models.CharField(max_length=100, blank=True, null=True)
    dwgz_ye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bl = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    ywyzkf = models.CharField(max_length=1, blank=True, null=True)
    ywyzkye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_gift_list'


class AccountJdgz(models.Model):
    account_number = models.CharField(max_length=20, blank=True, null=True)
    room_number = models.CharField(max_length=20, blank=True, null=True)
    gzje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    kjje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    lb = models.CharField(max_length=2, blank=True, null=True)
    k3_item = models.CharField(max_length=80, blank=True, null=True)
    k3_item_name = models.CharField(max_length=80, blank=True, null=True)
    k3_zg_item = models.CharField(max_length=80, blank=True, null=True)
    k3_zg_item_name = models.CharField(max_length=80, blank=True, null=True)
    bz = models.CharField(max_length=20, blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_jdgz'


class AccountMemberList(models.Model):
    bill_code = models.CharField(max_length=14, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    xb = models.CharField(max_length=1, blank=True, null=True)
    deal_code = models.CharField(max_length=2, blank=True, null=True)
    deal_type = models.CharField(max_length=2, blank=True, null=True)
    je = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    lrry = models.CharField(max_length=6, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    memo = models.CharField(max_length=40, blank=True, null=True)
    fkfs = models.CharField(max_length=2, blank=True, null=True)
    lb = models.CharField(max_length=1, blank=True, null=True)
    rs = models.IntegerField(blank=True, null=True)
    ywydm = models.CharField(max_length=6, blank=True, null=True)
    khly = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_member_list'


class AutoDownUpLog(models.Model):
    rq = models.DateField(blank=True, null=True)
    down_up = models.CharField(max_length=20, blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_down_up_log'


class BasBgdType(models.Model):
    dm = models.CharField(max_length=10, blank=True, null=True)
    mc = models.CharField(max_length=60, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_bgd_type'


class BasCardType(models.Model):
    dm = models.CharField(max_length=6, blank=True, null=True)
    mc = models.CharField(max_length=40, blank=True, null=True)
    sjdm = models.CharField(max_length=6, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    ahead_code = models.CharField(max_length=10, blank=True, null=True)
    after_code = models.CharField(max_length=10, blank=True, null=True)
    ickf = models.CharField(max_length=1, blank=True, null=True)
    code_length = models.IntegerField(blank=True, null=True)
    ms = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_card_type'


class BasChargeGroup(models.Model):
    groupid = models.CharField(max_length=10, blank=True, null=True)
    groupname = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    standard = models.CharField(max_length=20, blank=True, null=True)
    sjdm = models.CharField(max_length=30, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    jxf = models.CharField(max_length=1, blank=True, null=True)
    jclb = models.CharField(max_length=2, blank=True, null=True)
    print_datawindow = models.CharField(max_length=40, blank=True, null=True)
    aid_code = models.CharField(max_length=20, blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    group_en = models.CharField(max_length=50, blank=True, null=True)
    group_ft = models.CharField(max_length=50, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_charge_group'


class BasChargeItem(models.Model):
    item_id = models.CharField(max_length=6, blank=True, null=True)
    item_name = models.CharField(max_length=40, blank=True, null=True)
    item_ename = models.CharField(max_length=40, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    sfcjyb = models.CharField(max_length=1, blank=True, null=True)
    standard = models.CharField(max_length=20, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    userobject = models.CharField(max_length=30, blank=True, null=True)
    sfjy = models.CharField(max_length=1, blank=True, null=True)
    mcjysj = models.IntegerField(blank=True, null=True)
    sample_type_id = models.CharField(max_length=4, blank=True, null=True)
    zyphf = models.CharField(max_length=1, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    aid_code = models.CharField(max_length=15, blank=True, null=True)
    xb_status = models.CharField(max_length=1, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    is_picture = models.CharField(max_length=1, blank=True, null=True)
    picture_widht = models.BigIntegerField(blank=True, null=True)
    picture_height = models.BigIntegerField(blank=True, null=True)
    item_ft = models.CharField(max_length=40, blank=True, null=True)
    page_pic_number = models.IntegerField(blank=True, null=True)
    total_page = models.IntegerField(blank=True, null=True)
    before_eat = models.CharField(max_length=10, blank=True, null=True)
    init_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_charge_item'


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


class BasChzd(models.Model):
    dm = models.CharField(max_length=2, blank=True, null=True)
    mc = models.CharField(max_length=20, blank=True, null=True)
    sjdm = models.CharField(max_length=2, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_chzd'


class BasCode(models.Model):
    table_name = models.CharField(max_length=30, blank=True, null=True)
    field_name = models.CharField(max_length=30, blank=True, null=True)
    code = models.CharField(max_length=1, blank=True, null=True)
    explain = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_code'


class BasCustImage(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    xh = models.IntegerField(blank=True, null=True)
    img = models.BinaryField(blank=True, null=True)
    trans_status1 = models.CharField(max_length=6, blank=True, null=True)
    trans_status2 = models.CharField(max_length=6, blank=True, null=True)
    bz1 = models.CharField(max_length=500, blank=True, null=True)
    bz2 = models.CharField(max_length=500, blank=True, null=True)
    bz3 = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_cust_image'


class BasCustInfor(models.Model):
    cid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"CID")
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
    bz = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"备注")
    djsj = models.DateField(blank=True, null=True, verbose_name=u"对接时间")
    djr = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"对接人")
    province = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"身份")
    city = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"所属城市")
    region = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"所属城区")
    cust_type = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"客户类型")
    zwdm = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"职务代码")
    cw = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"财务")
    zycd = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"职业")
    hycd = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"ZWDM")
    khly = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"ZWDM")
    zhye = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=u"ZWDM")
    member_type = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"确认模式")
    card_code = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"CARD_CODE")
    member_card_code = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"MEMBER_CARD_CODE")
    trans_status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"传输状态")
    op_date = models.DateField(blank=True, null=True, verbose_name=u"OP日期")
    ywydm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"ZWDM")
    gsgddh = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"ZWDM")
    khtz = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"ZWDM")
    gstz = models.CharField(max_length=150, blank=True, null=True, verbose_name=u"ZWDM")
    txtz = models.CharField(max_length=150, blank=True, null=True, verbose_name=u"ZWDM")
    yxjb = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"ZWDM")
    cust_region = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"自定义城区")
    k3_item = models.CharField(max_length=80, blank=True, null=True, verbose_name=u"K3项目")
    k3_zg_item = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"KS_ZG项目")
    bgd_lb = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"报告单LB")
    grgz_ye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"ZWDM")
    zzys = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"主治医生")
    xgsj = models.DateField(blank=True, null=True, verbose_name=u"修改时间")
    user_password = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"用户密码")
    password_xgsj = models.DateField(blank=True, null=True, verbose_name=u"密码修改时间")
    zzhs = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"ZWDM")

    class Meta:
        managed = False
        db_table = 'bas_cust_infor'
        verbose_name = u""
        verbose_name_plural = verbose_name


class BasCustInforPre(models.Model):
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    xb = models.CharField(max_length=1, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    sfzhm = models.CharField(max_length=18, blank=True, null=True)
    mz = models.CharField(max_length=4, blank=True, null=True)
    whcd = models.CharField(max_length=2, blank=True, null=True)
    gj = models.CharField(max_length=4, blank=True, null=True)
    hyzk = models.CharField(max_length=2, blank=True, null=True)
    jtzz = models.CharField(max_length=60, blank=True, null=True)
    yzbm = models.CharField(max_length=6, blank=True, null=True)
    lxdh = models.CharField(max_length=40, blank=True, null=True)
    yddh = models.CharField(max_length=11, blank=True, null=True)
    dwdm = models.CharField(max_length=12, blank=True, null=True)
    dwmc = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    bz = models.CharField(max_length=50, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    djr = models.CharField(max_length=6, blank=True, null=True)
    province = models.CharField(max_length=12, blank=True, null=True)
    city = models.CharField(max_length=12, blank=True, null=True)
    region = models.CharField(max_length=12, blank=True, null=True)
    cust_type = models.CharField(max_length=6, blank=True, null=True)
    zwdm = models.CharField(max_length=12, blank=True, null=True)
    cw = models.CharField(max_length=2, blank=True, null=True)
    zycd = models.CharField(max_length=2, blank=True, null=True)
    hycd = models.CharField(max_length=2, blank=True, null=True)
    khly = models.CharField(max_length=6, blank=True, null=True)
    zhye = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    member_type = models.CharField(max_length=2, blank=True, null=True)
    card_code = models.CharField(max_length=12, blank=True, null=True)
    djzt = models.CharField(max_length=1, blank=True, null=True)
    ywydm = models.CharField(max_length=6, blank=True, null=True)
    member_card_code = models.CharField(max_length=12, blank=True, null=True)
    move_oper = models.CharField(max_length=6, blank=True, null=True)
    move_time = models.DateField(blank=True, null=True)
    gsgddh = models.CharField(max_length=20, blank=True, null=True)
    khtz = models.CharField(max_length=200, blank=True, null=True)
    gstz = models.CharField(max_length=150, blank=True, null=True)
    txtz = models.CharField(max_length=150, blank=True, null=True)
    yxjb = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_cust_infor_pre'


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


class BasDeptDict(models.Model):
    dm = models.CharField(max_length=6, blank=True, null=True)
    mc = models.CharField(max_length=30, blank=True, null=True)
    sjdm = models.CharField(max_length=6, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_dept_dict'


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


class BasEntInfo(models.Model):
    dwdm = models.CharField(max_length=12, blank=True, null=True)
    dwmc = models.CharField(max_length=60, blank=True, null=True)
    dwdz = models.CharField(max_length=60, blank=True, null=True)
    yzbm = models.CharField(max_length=6, blank=True, null=True)
    lxr = models.CharField(max_length=10, blank=True, null=True)
    lxdh = models.CharField(max_length=30, blank=True, null=True)
    yddh = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    dwcz = models.CharField(max_length=20, blank=True, null=True)
    fzr = models.CharField(max_length=10, blank=True, null=True)
    djr = models.CharField(max_length=6, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    zhye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ywydm = models.CharField(max_length=6, blank=True, null=True)
    khly = models.CharField(max_length=6, blank=True, null=True)
    gshyye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    gshy_jkye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    k3_item = models.CharField(max_length=80, blank=True, null=True)
    k3_zg_item = models.CharField(max_length=20, blank=True, null=True)
    k3_zg_item_name = models.CharField(max_length=20, blank=True, null=True)
    lxs_ye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    hy_ye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    dwgz_ye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    gn_1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    gn_2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    gn_3 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    gn_4 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    zzys = models.CharField(max_length=6, blank=True, null=True)
    prior_dwdm = models.CharField(max_length=12, blank=True, null=True)
    dw_password = models.CharField(max_length=20, blank=True, null=True)
    password_xgsj = models.DateField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    zzhs = models.CharField(max_length=6, blank=True, null=True)
    gzhy_dm = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_ent_info'


class BasEntInfoPre(models.Model):
    dwdm = models.CharField(max_length=12, blank=True, null=True)
    dwmc = models.CharField(max_length=60, blank=True, null=True)
    dwdz = models.CharField(max_length=60, blank=True, null=True)
    yzbm = models.CharField(max_length=6, blank=True, null=True)
    lxr = models.CharField(max_length=10, blank=True, null=True)
    lxdh = models.CharField(max_length=30, blank=True, null=True)
    yddh = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    dwcz = models.CharField(max_length=20, blank=True, null=True)
    fzr = models.CharField(max_length=10, blank=True, null=True)
    djr = models.CharField(max_length=6, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    ywydm = models.CharField(max_length=6, blank=True, null=True)
    khly = models.CharField(max_length=6, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    dwrs = models.IntegerField(blank=True, null=True)
    xgr = models.CharField(max_length=6, blank=True, null=True)
    sjdwdm = models.CharField(max_length=12, blank=True, null=True)
    bz = models.CharField(max_length=255, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    gzhy_dm = models.CharField(max_length=20, blank=True, null=True)
    region_dm = models.CharField(max_length=30, blank=True, null=True)
    dw_password = models.CharField(max_length=20, blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    gjz1 = models.CharField(max_length=200, blank=True, null=True)
    gjz2 = models.CharField(max_length=200, blank=True, null=True)
    gjz3 = models.CharField(max_length=200, blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    bz4 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_ent_info_pre'


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


class BasGroupItem(models.Model):
    groupid = models.CharField(max_length=10, blank=True, null=True)
    item_id = models.CharField(max_length=6, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    yxjb = models.CharField(max_length=10, blank=True, null=True)
    xmmc = models.CharField(max_length=100, blank=True, null=True)
    dkdx = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_group_item'


class BasGxzd(models.Model):
    dm = models.CharField(max_length=2, blank=True, null=True)
    mc = models.CharField(max_length=20, blank=True, null=True)
    sjdm = models.CharField(max_length=2, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_gxzd'


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


class BasJcItemList(models.Model):
    item_id = models.CharField(max_length=6, blank=True, null=True)
    table_id = models.CharField(max_length=6, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_jc_item_list'


class BasJjzh(models.Model):
    groupid = models.CharField(max_length=2, blank=True, null=True)
    groupname = models.CharField(max_length=20, blank=True, null=True)
    bzrs = models.FloatField(blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    qssj = models.DateField(blank=True, null=True)
    zzsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_jjzh'


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


class BasOperatorInfor(models.Model):
    aid_code = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.CharField(max_length=6, blank=True, null=True)
    username = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=6, blank=True, null=True)
    ywyf = models.CharField(max_length=1, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    sjdm = models.CharField(max_length=20, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    rylb = models.CharField(max_length=20, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_operator_infor'


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


class BasUserPasswd(models.Model):
    dept_code = models.CharField(max_length=6, blank=True, null=True)
    user_id = models.CharField(max_length=6, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=8, blank=True, null=True)
    adm_flag = models.CharField(max_length=1, blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_date = models.DateField(blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_user_passwd'


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


class BjeyLisInterfaceDict(models.Model):
    dm = models.CharField(max_length=20, blank=True, null=True)
    mc = models.CharField(max_length=100, blank=True, null=True)
    sjdm = models.CharField(max_length=20, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bjey_lis_interface_dict'


class BjeyLisInterfaceList(models.Model):
    groupid = models.CharField(max_length=60, blank=True, null=True)
    dm = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bjey_lis_interface_list'


class CallCenterParm(models.Model):
    mn_userid = models.CharField(max_length=100, blank=True, null=True)
    userid = models.CharField(max_length=100, blank=True, null=True)
    userpass = models.CharField(max_length=100, blank=True, null=True)
    zjhm = models.CharField(max_length=100, blank=True, null=True)
    zxhm = models.CharField(max_length=100, blank=True, null=True)
    appid = models.CharField(max_length=100, blank=True, null=True)
    zzhlx = models.CharField(max_length=100, blank=True, null=True)
    zzhid = models.CharField(max_length=100, blank=True, null=True)
    zzhtoken = models.CharField(max_length=100, blank=True, null=True)
    pzhlx = models.CharField(max_length=100, blank=True, null=True)
    pzhid = models.CharField(max_length=100, blank=True, null=True)
    pzhtoken = models.CharField(max_length=100, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'call_center_parm'


class CardHealthAddItem(models.Model):
    billcode = models.CharField(max_length=300, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)
    paymethod = models.CharField(max_length=50, blank=True, null=True)
    paytime = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    sy_price = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    czry = models.CharField(max_length=200, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    sfzhm = models.CharField(max_length=200, blank=True, null=True)
    card_code = models.CharField(max_length=200, blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    bz4 = models.CharField(max_length=200, blank=True, null=True)
    bz5 = models.CharField(max_length=200, blank=True, null=True)
    jfry = models.CharField(max_length=200, blank=True, null=True)
    jfsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_health_add_item'


class CardYyDj(models.Model):
    billcode = models.CharField(max_length=200, blank=True, null=True)
    dwdm = models.CharField(max_length=100, blank=True, null=True)
    begin_code = models.CharField(max_length=100, blank=True, null=True)
    end_code = models.CharField(max_length=100, blank=True, null=True)
    lb = models.CharField(max_length=10, blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    do_in_factory = models.CharField(max_length=300, blank=True, null=True)
    groupid = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    djry = models.CharField(max_length=200, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_yy_dj'


class CardYydj2018(models.Model):
    billcode = models.CharField(max_length=200, blank=True, null=True)
    card_code = models.CharField(max_length=100, blank=True, null=True)
    card_pass = models.CharField(max_length=100, blank=True, null=True)
    card_bz = models.CharField(max_length=300, blank=True, null=True)
    dwdm = models.CharField(max_length=100, blank=True, null=True)
    card_lb = models.CharField(max_length=10, blank=True, null=True)
    groupid = models.CharField(max_length=1000, blank=True, null=True)
    do_in_factory = models.CharField(max_length=500, blank=True, null=True)
    swxw = models.CharField(max_length=10, blank=True, null=True)
    in_factory = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    djry = models.CharField(max_length=200, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    zfry = models.CharField(max_length=200, blank=True, null=True)
    zfsj = models.DateField(blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    bz4 = models.CharField(max_length=200, blank=True, null=True)
    bz5 = models.CharField(max_length=200, blank=True, null=True)
    bz6 = models.CharField(max_length=200, blank=True, null=True)
    bz7 = models.CharField(max_length=200, blank=True, null=True)
    bz8 = models.CharField(max_length=200, blank=True, null=True)
    bz9 = models.CharField(max_length=200, blank=True, null=True)
    shry = models.CharField(max_length=200, blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_yydj2018'


class CardYydj2018GroupLimit(models.Model):
    billcode = models.CharField(max_length=200, blank=True, null=True)
    groupid = models.CharField(max_length=30, blank=True, null=True)
    begdate = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    bz1 = models.CharField(max_length=50, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_yydj2018_group_limit'


class CmDydCircle(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    cid = models.CharField(max_length=20, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    xb = models.CharField(max_length=10, blank=True, null=True)
    dwdm = models.CharField(max_length=100, blank=True, null=True)
    dwmc = models.CharField(max_length=200, blank=True, null=True)
    dept_name = models.CharField(max_length=200, blank=True, null=True)
    dept_code = models.CharField(max_length=200, blank=True, null=True)
    djr = models.CharField(max_length=100, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)
    bz4 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cm_dyd_circle'


class CmItemPaper(models.Model):
    item_id = models.CharField(max_length=30, blank=True, null=True)
    dm = models.CharField(max_length=30, blank=True, null=True)
    sl = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cm_item_paper'


class CmPaperDict(models.Model):
    dm = models.CharField(max_length=10, blank=True, null=True)
    mc = models.CharField(max_length=200, blank=True, null=True)
    yxf = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cm_paper_dict'


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


class CrmCustCommRec(models.Model):
    dh = models.CharField(max_length=14, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=10, blank=True, null=True)
    ky = models.CharField(max_length=20, blank=True, null=True)
    xxms = models.CharField(max_length=400, blank=True, null=True)
    ywy = models.CharField(max_length=6, blank=True, null=True)
    ywyxm = models.CharField(max_length=10, blank=True, null=True)
    fssj = models.DateField(blank=True, null=True)
    tsf = models.CharField(max_length=1, blank=True, null=True)
    tqsj = models.IntegerField(blank=True, null=True)
    wcqk = models.CharField(max_length=10, blank=True, null=True)
    next_step = models.CharField(max_length=1, blank=True, null=True)
    xgdw = models.CharField(max_length=30, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_cust_comm_rec'


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


class CrmCustMoveDetail(models.Model):
    bill_code = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=10, blank=True, null=True)
    newywydm = models.CharField(max_length=6, blank=True, null=True)
    lb = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_cust_move_detail'


class CrmCustMoveIndex(models.Model):
    bill_code = models.CharField(max_length=12, blank=True, null=True)
    ywydm = models.CharField(max_length=6, blank=True, null=True)
    lrry = models.CharField(max_length=6, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    shry = models.CharField(max_length=6, blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_cust_move_index'


class CrmCustMoveRule(models.Model):
    bill_code = models.CharField(max_length=12, blank=True, null=True)
    begin_id = models.IntegerField(blank=True, null=True)
    end_id = models.IntegerField(blank=True, null=True)
    ywydm = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_cust_move_rule'


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


class CrmHfRecord(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    fh_item = models.CharField(max_length=6, blank=True, null=True)
    fwnr = models.CharField(max_length=200, blank=True, null=True)
    khfy = models.CharField(max_length=400, blank=True, null=True)
    cljg = models.CharField(max_length=100, blank=True, null=True)
    clry = models.CharField(max_length=6, blank=True, null=True)
    clsj = models.DateField(blank=True, null=True)
    memo = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    shry = models.CharField(max_length=6, blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_hf_record'


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


class CrmKhlydmb(models.Model):
    dm = models.CharField(max_length=6, blank=True, null=True)
    mc = models.CharField(max_length=30, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    tcfs = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_khlydmb'


class CrmMailSendCfg(models.Model):
    dh = models.CharField(max_length=10, blank=True, null=True)
    m_host = models.CharField(max_length=50, blank=True, null=True)
    m_port = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    pwd = models.CharField(max_length=20, blank=True, null=True)
    bj = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_mail_send_cfg'


class CrmMailSendDetail(models.Model):
    dh = models.CharField(max_length=12, blank=True, null=True)
    addr = models.CharField(max_length=50, blank=True, null=True)
    subj = models.CharField(max_length=50, blank=True, null=True)
    send_time = models.DateField(blank=True, null=True)
    body = models.CharField(max_length=2000, blank=True, null=True)
    bj = models.CharField(max_length=100, blank=True, null=True)
    attachment = models.CharField(max_length=100, blank=True, null=True)
    xm = models.CharField(max_length=10, blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    lx = models.CharField(max_length=2, blank=True, null=True)
    operator = models.CharField(max_length=6, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_mail_send_detail'


class CrmMailSendList(models.Model):
    dh = models.CharField(max_length=12, blank=True, null=True)
    send_time = models.DateField(blank=True, null=True)
    contxt = models.CharField(max_length=100, blank=True, null=True)
    js = models.IntegerField(blank=True, null=True)
    bj = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_mail_send_list'


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


class CrmTsjbxx(models.Model):
    dh = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=30, blank=True, null=True)
    cid = models.CharField(max_length=30, blank=True, null=True)
    zt = models.CharField(max_length=40, blank=True, null=True)
    tsrq = models.DateField(blank=True, null=True)
    tsdx = models.CharField(max_length=40, blank=True, null=True)
    tsnr = models.CharField(max_length=400, blank=True, null=True)
    lry = models.CharField(max_length=6, blank=True, null=True)
    lryxm = models.CharField(max_length=10, blank=True, null=True)
    clr = models.CharField(max_length=50, blank=True, null=True)
    clrxm = models.CharField(max_length=10, blank=True, null=True)
    cljg = models.CharField(max_length=400, blank=True, null=True)
    djzt = models.CharField(max_length=1, blank=True, null=True)
    clsj = models.DateField(blank=True, null=True)
    tsrlxfs = models.CharField(max_length=40, blank=True, null=True)
    shr = models.CharField(max_length=10, blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    tsbm = models.CharField(max_length=6, blank=True, null=True)
    tslb = models.CharField(max_length=50, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_tsjbxx'


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


class CustChangePassLog(models.Model):
    cid = models.CharField(max_length=30, blank=True, null=True)
    change_time = models.DateField(blank=True, null=True)
    old_pass = models.CharField(max_length=30, blank=True, null=True)
    new_pass = models.CharField(max_length=30, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_change_pass_log'


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


class CustZutoPjList(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    cid = models.CharField(max_length=30, blank=True, null=True)
    xm = models.CharField(max_length=30, blank=True, null=True)
    xb = models.CharField(max_length=30, blank=True, null=True)
    dwdm = models.CharField(max_length=30, blank=True, null=True)
    dwmc = models.CharField(max_length=200, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    lxdh = models.CharField(max_length=100, blank=True, null=True)
    yddh = models.CharField(max_length=100, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    pj_item = models.CharField(max_length=200, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)
    bz4 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_zuto_pj_list'


class CwDeleteItem(models.Model):
    billcode = models.CharField(max_length=100, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)
    item_id = models.CharField(max_length=30, blank=True, null=True)
    item_name = models.CharField(max_length=200, blank=True, null=True)
    item_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    delete_xj_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    delete_djq_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    delete_lpk_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    delete_dwgz_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    czy = models.CharField(max_length=30, blank=True, null=True)
    czy_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cw_delete_item'


class CwDwjxGzSetup(models.Model):
    dwdm = models.CharField(max_length=60, blank=True, null=True)
    kssj = models.DateField(blank=True, null=True)
    jzsj = models.DateField(blank=True, null=True)
    groupid = models.CharField(max_length=30, blank=True, null=True)
    jxx_dwgz = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cw_dwjx_gz_setup'


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


class DsfDz(models.Model):
    dsf = models.CharField(max_length=20, blank=True, null=True)
    xmid = models.CharField(max_length=30, blank=True, null=True)
    xmmc = models.CharField(max_length=50, blank=True, null=True)
    xmlx = models.CharField(max_length=5, blank=True, null=True)
    xmdw = models.CharField(max_length=20, blank=True, null=True)
    itemid = models.CharField(max_length=20, blank=True, null=True)
    itemmc = models.CharField(max_length=100, blank=True, null=True)
    groupid = models.CharField(max_length=20, blank=True, null=True)
    groupmc = models.CharField(max_length=200, blank=True, null=True)
    xmsx = models.CharField(max_length=300, blank=True, null=True)
    bz = models.CharField(max_length=200, blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsf_dz'


class EmicRecord(models.Model):
    callid = models.CharField(max_length=50, blank=True, null=True)
    createtime = models.DateField(blank=True, null=True)
    cid = models.CharField(max_length=20, blank=True, null=True)
    tonumber = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emic_record'


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


class GroupExchange2018(models.Model):
    billcode = models.CharField(max_length=100, blank=True, null=True)
    dwdm = models.CharField(max_length=100, blank=True, null=True)
    groupid = models.CharField(max_length=30, blank=True, null=True)
    groupname = models.CharField(max_length=300, blank=True, null=True)
    group_code = models.CharField(max_length=30, blank=True, null=True)
    czy = models.CharField(max_length=100, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    shry = models.CharField(max_length=100, blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    zfry = models.CharField(max_length=100, blank=True, null=True)
    zfsj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    id = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_exchange_2018'


class GroupSelectIndex(models.Model):
    id = models.CharField(max_length=200, blank=True, null=True)
    billcode = models.CharField(max_length=20, blank=True, null=True)
    groupid = models.CharField(max_length=20, blank=True, null=True)
    groupname = models.CharField(max_length=200, blank=True, null=True)
    num = models.BigIntegerField(blank=True, null=True)
    lrry = models.CharField(max_length=20, blank=True, null=True)
    lrry_name = models.CharField(max_length=100, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    shry = models.CharField(max_length=20, blank=True, null=True)
    shry_name = models.CharField(max_length=20, blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    zfry = models.CharField(max_length=20, blank=True, null=True)
    zfry_name = models.CharField(max_length=100, blank=True, null=True)
    zfsj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_select_index'


class GroupSelectList(models.Model):
    billcode = models.CharField(max_length=200, blank=True, null=True)
    groupid = models.CharField(max_length=30, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)
    groupname = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_select_list'


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


class IckManageLog(models.Model):
    card_bill = models.CharField(max_length=12, blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=10, blank=True, null=True)
    lx = models.CharField(max_length=1, blank=True, null=True)
    lxmc = models.CharField(max_length=30, blank=True, null=True)
    old_card_code = models.CharField(max_length=12, blank=True, null=True)
    new_card_code = models.CharField(max_length=12, blank=True, null=True)
    czry = models.CharField(max_length=6, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    card_serial = models.CharField(max_length=30, blank=True, null=True)
    card_type = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ick_manage_log'


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


class ItemJyGx(models.Model):
    dm = models.CharField(max_length=4, blank=True, null=True)
    mc = models.CharField(max_length=100, blank=True, null=True)
    yxf = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_jy_gx'


class ItemOtherColor(models.Model):
    item_id = models.CharField(max_length=20, blank=True, null=True)
    ys = models.CharField(max_length=10, blank=True, null=True)
    bz1 = models.CharField(max_length=50, blank=True, null=True)
    bz2 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_other_color'


class JdSocketLog(models.Model):
    czsj = models.DateField(blank=True, null=True)
    czy = models.CharField(max_length=6, blank=True, null=True)
    lb = models.CharField(max_length=1, blank=True, null=True)
    bz = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jd_socket_log'


class JjAddItemDict2018(models.Model):
    lb = models.CharField(max_length=80, blank=True, null=True)
    groupid = models.CharField(max_length=80, blank=True, null=True)
    groupname = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    w1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    w2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    w3 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    w4 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    w5 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    w6 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    w7 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_add_item_dict2018'


class JjAddItemList2018(models.Model):
    billcode = models.CharField(max_length=200, blank=True, null=True)
    cid = models.CharField(max_length=50, blank=True, null=True)
    vid = models.CharField(max_length=20, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    xb = models.CharField(max_length=10, blank=True, null=True)
    dwdm = models.CharField(max_length=50, blank=True, null=True)
    groupid = models.CharField(max_length=50, blank=True, null=True)
    groupname = models.CharField(max_length=300, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    add_checkdept = models.CharField(max_length=100, blank=True, null=True)
    add_checkdept_name = models.CharField(max_length=200, blank=True, null=True)
    add_oper = models.CharField(max_length=50, blank=True, null=True)
    add_opername = models.CharField(max_length=100, blank=True, null=True)
    fee_oper = models.CharField(max_length=50, blank=True, null=True)
    fee_opername = models.CharField(max_length=100, blank=True, null=True)
    create_oper = models.CharField(max_length=50, blank=True, null=True)
    create_opername = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    add_date = models.DateField(blank=True, null=True)
    fee_date = models.DateField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    fee_type = models.CharField(max_length=10, blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=300, blank=True, null=True)
    bz3 = models.CharField(max_length=300, blank=True, null=True)
    bz4 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_add_item_list2018'


class JjAdkBarcode(models.Model):
    adk_barcode = models.CharField(max_length=30, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    bz1 = models.CharField(max_length=10, blank=True, null=True)
    bz2 = models.CharField(max_length=50, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_adk_barcode'


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


class JjBcZdMiddle(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    item_id = models.CharField(max_length=30, blank=True, null=True)
    item_ms = models.CharField(max_length=30, blank=True, null=True)
    item_ms_zb = models.CharField(max_length=30, blank=True, null=True)
    zd_nr = models.CharField(max_length=200, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_bc_zd_middle'


class JjCommJcResult(models.Model):
    item_id = models.CharField(max_length=6, blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'jj_comm_jc_result'


class JjCommJcResultBack(models.Model):
    item_id = models.CharField(max_length=6, blank=True, null=True)
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
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_comm_jc_result_back'


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


class JjCustCook(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=10, blank=True, null=True)
    xb = models.CharField(max_length=2, blank=True, null=True)
    cook_billcode = models.CharField(max_length=6, blank=True, null=True)
    cook_name = models.CharField(max_length=60, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sg = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tz = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    lxtz = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ytrl = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    shry = models.CharField(max_length=6, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    mf_num = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sc_num = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    rl_num = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    dzp_num = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    dl_num = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    yz_num = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sg_num = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    dbz_num = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    zf_num = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_cust_cook'


class JjCustCooklist(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    cook_name = models.CharField(max_length=50, blank=True, null=True)
    cook_num = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    isrice = models.CharField(max_length=1, blank=True, null=True)
    memo = models.CharField(max_length=30, blank=True, null=True)
    units = models.CharField(max_length=8, blank=True, null=True)
    total_power = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_cust_cooklist'


class JjCustJtBwItemResult(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    lb = models.CharField(max_length=20, blank=True, null=True)
    item_id = models.CharField(max_length=100, blank=True, null=True)
    item_name = models.CharField(max_length=200, blank=True, null=True)
    num = models.BigIntegerField(blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_cust_jt_bw_item_result'


class JjCustJtBwItemResultBack(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    lb = models.CharField(max_length=20, blank=True, null=True)
    item_id = models.CharField(max_length=100, blank=True, null=True)
    item_name = models.CharField(max_length=200, blank=True, null=True)
    num = models.BigIntegerField(blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_cust_jt_bw_item_result_back'


class JjCustJyMultiJy(models.Model):
    id = models.CharField(max_length=100, blank=True, null=True)
    jybt = models.CharField(max_length=500, blank=True, null=True)
    jxys = models.CharField(max_length=1000, blank=True, null=True)
    yyhg = models.CharField(max_length=1000, blank=True, null=True)
    yxjy = models.CharField(max_length=1000, blank=True, null=True)
    ycbw = models.CharField(max_length=100, blank=True, null=True)
    jbnr = models.CharField(max_length=100, blank=True, null=True)
    sfjb = models.CharField(max_length=100, blank=True, null=True)
    yxf = models.CharField(max_length=10, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    item_id_1 = models.CharField(max_length=100, blank=True, null=True)
    abnormal_1 = models.CharField(max_length=100, blank=True, null=True)
    item_id_2 = models.CharField(max_length=100, blank=True, null=True)
    abnormal_2 = models.CharField(max_length=100, blank=True, null=True)
    item_id_3 = models.CharField(max_length=100, blank=True, null=True)
    abnormal_3 = models.CharField(max_length=100, blank=True, null=True)
    item_id_4 = models.CharField(max_length=100, blank=True, null=True)
    abnormal_4 = models.CharField(max_length=100, blank=True, null=True)
    item_id_5 = models.CharField(max_length=100, blank=True, null=True)
    abnormal_5 = models.CharField(max_length=100, blank=True, null=True)
    item_id_6 = models.CharField(max_length=100, blank=True, null=True)
    abnormal_6 = models.CharField(max_length=100, blank=True, null=True)
    item_id_7 = models.CharField(max_length=100, blank=True, null=True)
    abnormal_7 = models.CharField(max_length=100, blank=True, null=True)
    item_id_8 = models.CharField(max_length=100, blank=True, null=True)
    abnormal_8 = models.CharField(max_length=100, blank=True, null=True)
    item_id_9 = models.CharField(max_length=100, blank=True, null=True)
    abnormal_9 = models.CharField(max_length=100, blank=True, null=True)
    item_id_10 = models.CharField(max_length=100, blank=True, null=True)
    abnormal_10 = models.CharField(max_length=100, blank=True, null=True)
    item_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_cust_jy_multi_jy'


class JjCustPhoto(models.Model):
    cid = models.CharField(max_length=12, blank=True, null=True)
    cid_photo = models.BinaryField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_cust_photo'


class JjCustYcDict2014(models.Model):
    id = models.CharField(max_length=100, blank=True, null=True)
    item_ms_zb = models.CharField(max_length=100, blank=True, null=True)
    item_id = models.CharField(max_length=100, blank=True, null=True)
    lb = models.CharField(max_length=100, blank=True, null=True)
    jybt = models.CharField(max_length=300, blank=True, null=True)
    jxjs = models.CharField(max_length=1000, blank=True, null=True)
    yyhg = models.CharField(max_length=1000, blank=True, null=True)
    yxjy = models.CharField(max_length=1000, blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    yxjg = models.CharField(max_length=100, blank=True, null=True)
    pg_pd = models.CharField(max_length=100, blank=True, null=True)
    value_l = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    value_h = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    yxf = models.CharField(max_length=10, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    sfmrjy = models.CharField(max_length=10, blank=True, null=True)
    yxgjz = models.CharField(max_length=500, blank=True, null=True)
    ycbw_sz = models.CharField(max_length=500, blank=True, null=True)
    yxnr = models.CharField(max_length=500, blank=True, null=True)
    bz2 = models.CharField(max_length=500, blank=True, null=True)
    item_id_a = models.CharField(max_length=100, blank=True, null=True)
    sfjb = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_cust_yc_dict2014'


class JjCustZdjyResult(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    item_id = models.CharField(max_length=30, blank=True, null=True)
    item_ms = models.CharField(max_length=30, blank=True, null=True)
    item_ms_zb = models.CharField(max_length=30, blank=True, null=True)
    zd_nr = models.CharField(max_length=200, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    mbnr = models.CharField(max_length=1000, blank=True, null=True)
    sfjb = models.CharField(max_length=100, blank=True, null=True)
    jbnb = models.CharField(max_length=200, blank=True, null=True)
    jybt = models.CharField(max_length=200, blank=True, null=True)
    yxjs = models.CharField(max_length=1000, blank=True, null=True)
    yyhg = models.CharField(max_length=1000, blank=True, null=True)
    yxjy = models.CharField(max_length=1000, blank=True, null=True)
    lb = models.CharField(max_length=10, blank=True, null=True)
    trans_status1 = models.CharField(max_length=10, blank=True, null=True)
    trans_status2 = models.CharField(max_length=10, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    bz4 = models.CharField(max_length=1000, blank=True, null=True)
    bz5 = models.CharField(max_length=1000, blank=True, null=True)
    bz6 = models.CharField(max_length=1000, blank=True, null=True)
    ycbw = models.CharField(max_length=200, blank=True, null=True)
    in_factory = models.CharField(max_length=200, blank=True, null=True)
    czys = models.CharField(max_length=100, blank=True, null=True)
    results = models.CharField(max_length=2000, blank=True, null=True)
    fw = models.CharField(max_length=500, blank=True, null=True)
    item_id_a = models.CharField(max_length=100, blank=True, null=True)
    tdbg_bt = models.CharField(max_length=200, blank=True, null=True)
    abnormal = models.CharField(max_length=10, blank=True, null=True)
    sz = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    jt_bm = models.CharField(max_length=100, blank=True, null=True)
    jb_bm_mc = models.CharField(max_length=200, blank=True, null=True)
    zy_bz = models.CharField(max_length=200, blank=True, null=True)
    table_sxh = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    item_sxh = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_cust_zdjy_result'


class JjCustZdjyResultBack(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    item_id = models.CharField(max_length=30, blank=True, null=True)
    item_ms = models.CharField(max_length=30, blank=True, null=True)
    item_ms_zb = models.CharField(max_length=30, blank=True, null=True)
    zd_nr = models.CharField(max_length=200, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    mbnr = models.CharField(max_length=1000, blank=True, null=True)
    sfjb = models.CharField(max_length=100, blank=True, null=True)
    jbnb = models.CharField(max_length=200, blank=True, null=True)
    jybt = models.CharField(max_length=200, blank=True, null=True)
    yxjs = models.CharField(max_length=1000, blank=True, null=True)
    yyhg = models.CharField(max_length=1000, blank=True, null=True)
    yxjy = models.CharField(max_length=1000, blank=True, null=True)
    lb = models.CharField(max_length=10, blank=True, null=True)
    trans_status1 = models.CharField(max_length=10, blank=True, null=True)
    trans_status2 = models.CharField(max_length=10, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    bz4 = models.CharField(max_length=1000, blank=True, null=True)
    bz5 = models.CharField(max_length=1000, blank=True, null=True)
    bz6 = models.CharField(max_length=1000, blank=True, null=True)
    ycbw = models.CharField(max_length=200, blank=True, null=True)
    in_factory = models.CharField(max_length=200, blank=True, null=True)
    czys = models.CharField(max_length=100, blank=True, null=True)
    results = models.CharField(max_length=2000, blank=True, null=True)
    fw = models.CharField(max_length=500, blank=True, null=True)
    item_id_a = models.CharField(max_length=100, blank=True, null=True)
    tdbg_bt = models.CharField(max_length=200, blank=True, null=True)
    abnormal = models.CharField(max_length=10, blank=True, null=True)
    sz = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    jt_bm = models.CharField(max_length=100, blank=True, null=True)
    jb_bm_mc = models.CharField(max_length=200, blank=True, null=True)
    zy_bz = models.CharField(max_length=200, blank=True, null=True)
    table_sxh = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    item_sxh = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_cust_zdjy_result_back'


class JjCustZdnrResult(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    item_id = models.CharField(max_length=30, blank=True, null=True)
    item_ms = models.CharField(max_length=30, blank=True, null=True)
    item_ms_zb = models.CharField(max_length=30, blank=True, null=True)
    zd_nr = models.CharField(max_length=200, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    mbnr = models.CharField(max_length=1000, blank=True, null=True)
    sfjb = models.CharField(max_length=100, blank=True, null=True)
    jbnb = models.CharField(max_length=200, blank=True, null=True)
    jybt = models.CharField(max_length=200, blank=True, null=True)
    yxjs = models.CharField(max_length=1000, blank=True, null=True)
    yyhg = models.CharField(max_length=1000, blank=True, null=True)
    yxjy = models.CharField(max_length=1000, blank=True, null=True)
    lb = models.CharField(max_length=10, blank=True, null=True)
    trans_status1 = models.CharField(max_length=10, blank=True, null=True)
    trans_status2 = models.CharField(max_length=10, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    bz4 = models.CharField(max_length=1000, blank=True, null=True)
    bz5 = models.CharField(max_length=1000, blank=True, null=True)
    bz6 = models.CharField(max_length=1000, blank=True, null=True)
    ycbw = models.CharField(max_length=200, blank=True, null=True)
    in_factory = models.CharField(max_length=200, blank=True, null=True)
    czys = models.CharField(max_length=100, blank=True, null=True)
    results = models.CharField(max_length=2000, blank=True, null=True)
    fw = models.CharField(max_length=500, blank=True, null=True)
    item_id_a = models.CharField(max_length=100, blank=True, null=True)
    tdbg_bt = models.CharField(max_length=200, blank=True, null=True)
    abnormal = models.CharField(max_length=10, blank=True, null=True)
    sz = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    jt_bm = models.CharField(max_length=100, blank=True, null=True)
    jb_bm_mc = models.CharField(max_length=200, blank=True, null=True)
    zy_bz = models.CharField(max_length=200, blank=True, null=True)
    table_sxh = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    item_sxh = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_cust_zdnr_result'


class JjCustZdnrResultBack(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    item_id = models.CharField(max_length=30, blank=True, null=True)
    item_ms = models.CharField(max_length=30, blank=True, null=True)
    item_ms_zb = models.CharField(max_length=30, blank=True, null=True)
    zd_nr = models.CharField(max_length=200, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    mbnr = models.CharField(max_length=1000, blank=True, null=True)
    sfjb = models.CharField(max_length=100, blank=True, null=True)
    jbnb = models.CharField(max_length=200, blank=True, null=True)
    jybt = models.CharField(max_length=200, blank=True, null=True)
    yxjs = models.CharField(max_length=1000, blank=True, null=True)
    yyhg = models.CharField(max_length=1000, blank=True, null=True)
    yxjy = models.CharField(max_length=1000, blank=True, null=True)
    lb = models.CharField(max_length=10, blank=True, null=True)
    trans_status1 = models.CharField(max_length=10, blank=True, null=True)
    trans_status2 = models.CharField(max_length=10, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    bz4 = models.CharField(max_length=1000, blank=True, null=True)
    bz5 = models.CharField(max_length=1000, blank=True, null=True)
    bz6 = models.CharField(max_length=1000, blank=True, null=True)
    ycbw = models.CharField(max_length=200, blank=True, null=True)
    in_factory = models.CharField(max_length=200, blank=True, null=True)
    czys = models.CharField(max_length=100, blank=True, null=True)
    results = models.CharField(max_length=2000, blank=True, null=True)
    fw = models.CharField(max_length=500, blank=True, null=True)
    item_id_a = models.CharField(max_length=100, blank=True, null=True)
    tdbg_bt = models.CharField(max_length=200, blank=True, null=True)
    abnormal = models.CharField(max_length=10, blank=True, null=True)
    sz = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    jt_bm = models.CharField(max_length=100, blank=True, null=True)
    jb_bm_mc = models.CharField(max_length=200, blank=True, null=True)
    zy_bz = models.CharField(max_length=200, blank=True, null=True)
    table_sxh = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    item_sxh = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_cust_zdnr_result_back'


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


class JjDxysInterface(models.Model):
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
        db_table = 'jj_dxys_interface'


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


class JjGwycList2019(models.Model):
    billcode = models.CharField(max_length=200, blank=True, null=True)
    cid = models.CharField(max_length=100, blank=True, null=True)
    vid = models.CharField(max_length=20, blank=True, null=True)
    xm = models.CharField(max_length=200, blank=True, null=True)
    xb = models.CharField(max_length=20, blank=True, null=True)
    dwdm = models.CharField(max_length=100, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    lr_factory = models.CharField(max_length=30, blank=True, null=True)
    lb = models.CharField(max_length=100, blank=True, null=True)
    dm = models.CharField(max_length=200, blank=True, null=True)
    mc = models.CharField(max_length=500, blank=True, null=True)
    mc_detail = models.CharField(max_length=800, blank=True, null=True)
    dept_code = models.CharField(max_length=100, blank=True, null=True)
    lr_opername = models.CharField(max_length=200, blank=True, null=True)
    lr_date = models.DateField(blank=True, null=True)
    yxf = models.CharField(max_length=10, blank=True, null=True)
    bz1 = models.CharField(max_length=500, blank=True, null=True)
    bz2 = models.CharField(max_length=500, blank=True, null=True)
    bz3 = models.CharField(max_length=500, blank=True, null=True)
    bz4 = models.CharField(max_length=500, blank=True, null=True)
    bz5 = models.CharField(max_length=500, blank=True, null=True)
    read_ornot = models.CharField(max_length=10, blank=True, null=True)
    read_opername = models.CharField(max_length=100, blank=True, null=True)
    sh_opername = models.CharField(max_length=100, blank=True, null=True)
    sh_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_gwyc_list2019'


class JjGwycSfList(models.Model):
    billcode = models.CharField(max_length=200, blank=True, null=True)
    vid = models.CharField(max_length=50, blank=True, null=True)
    czjl = models.CharField(max_length=1000, blank=True, null=True)
    sfjl = models.CharField(max_length=1000, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    sfsj = models.DateField(blank=True, null=True)
    zfsj = models.DateField(blank=True, null=True)
    cz_opername = models.CharField(max_length=200, blank=True, null=True)
    sf_opername = models.CharField(max_length=200, blank=True, null=True)
    zf_opername = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    bz4 = models.CharField(max_length=200, blank=True, null=True)
    bz5 = models.CharField(max_length=200, blank=True, null=True)
    bz6 = models.CharField(max_length=600, blank=True, null=True)
    bz7 = models.CharField(max_length=600, blank=True, null=True)
    bz8 = models.CharField(max_length=600, blank=True, null=True)
    bz9 = models.CharField(max_length=600, blank=True, null=True)
    bz10 = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_gwyc_sf_list'


class JjHealthAdvice(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=10, blank=True, null=True)
    xb = models.CharField(max_length=2, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    ys_question = models.CharField(max_length=100, blank=True, null=True)
    bcyy = models.CharField(max_length=40, blank=True, null=True)
    zjswly = models.CharField(max_length=1000, blank=True, null=True)
    bz = models.CharField(max_length=100, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_health_advice'


class JjHealthJkjys(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=10, blank=True, null=True)
    xb = models.CharField(max_length=2, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    rl_require = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    rl_ydrl = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    rl_fact = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    rl_wggjl = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    rl_scl = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    rl_xqrl = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    rl_yxl = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    rl_dl = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    rl_dlzp = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    rl_sgl = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    rl_nl = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    rl_yzl = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    yys_dbz = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    yys_zf = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    yys_gz = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    yys_tz = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    yys_dgc = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    yys_tshhw = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    yys_xws = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    yys_wssa = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    yys_wssb1 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    yys_wssb2 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    yys_wssc = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    yys_dtl = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    yys_yf = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    yys_jj = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    jkzs = models.CharField(max_length=2, blank=True, null=True)
    import_num = models.IntegerField(blank=True, null=True)
    import_ms1 = models.CharField(max_length=100, blank=True, null=True)
    import_ms2 = models.CharField(max_length=100, blank=True, null=True)
    import_ms3 = models.CharField(max_length=100, blank=True, null=True)
    import_ms4 = models.CharField(max_length=100, blank=True, null=True)
    import_ms5 = models.CharField(max_length=100, blank=True, null=True)
    import_ms6 = models.CharField(max_length=100, blank=True, null=True)
    jb_grjws = models.CharField(max_length=200, blank=True, null=True)
    jb_jzjws = models.CharField(max_length=200, blank=True, null=True)
    cy_ms1 = models.CharField(max_length=100, blank=True, null=True)
    cy_ms2 = models.CharField(max_length=100, blank=True, null=True)
    wsq_ms1 = models.CharField(max_length=100, blank=True, null=True)
    wsq_ms2 = models.CharField(max_length=100, blank=True, null=True)
    js_ms1 = models.CharField(max_length=100, blank=True, null=True)
    js_ms2 = models.CharField(max_length=100, blank=True, null=True)
    slbc_ms1 = models.CharField(max_length=100, blank=True, null=True)
    slbc_ms2 = models.CharField(max_length=100, blank=True, null=True)
    yys_yd = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ms = models.CharField(max_length=4000, blank=True, null=True)
    jb_grjws2 = models.CharField(max_length=100, blank=True, null=True)
    jb_jzjws2 = models.CharField(max_length=100, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_health_jkjys'


class JjHealthQuestion(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=20, blank=True, null=True)
    mtcsc = models.CharField(max_length=1, blank=True, null=True)
    mtcr = models.CharField(max_length=1, blank=True, null=True)
    xyf = models.CharField(max_length=1, blank=True, null=True)
    ysf = models.CharField(max_length=1, blank=True, null=True)
    hjf = models.CharField(max_length=1, blank=True, null=True)
    cxcf = models.CharField(max_length=1, blank=True, null=True)
    cxr_tsspf = models.CharField(max_length=1, blank=True, null=True)
    ctsf = models.CharField(max_length=1, blank=True, null=True)
    cxyf = models.CharField(max_length=1, blank=True, null=True)
    syhf = models.CharField(max_length=1, blank=True, null=True)
    bmf = models.CharField(max_length=1, blank=True, null=True)
    npnjf = models.CharField(max_length=1, blank=True, null=True)
    tyf = models.CharField(max_length=1, blank=True, null=True)
    jdsjrsf = models.CharField(max_length=1, blank=True, null=True)
    zjjmcbf = models.CharField(max_length=1, blank=True, null=True)
    tjbbcf = models.CharField(max_length=1, blank=True, null=True)
    ksxmf = models.CharField(max_length=1, blank=True, null=True)
    hzkdf = models.CharField(max_length=1, blank=True, null=True)
    yxbxf = models.CharField(max_length=1, blank=True, null=True)
    stxsf = models.CharField(max_length=1, blank=True, null=True)
    stfpf = models.CharField(max_length=1, blank=True, null=True)
    xgxsf = models.CharField(max_length=1, blank=True, null=True)
    mtydf = models.CharField(max_length=1, blank=True, null=True)
    zsywskf = models.CharField(max_length=1, blank=True, null=True)
    cykysf = models.CharField(max_length=1, blank=True, null=True)
    gxytnbf = models.CharField(max_length=1, blank=True, null=True)
    yzbsf = models.CharField(max_length=1, blank=True, null=True)
    ysbtf = models.CharField(max_length=1, blank=True, null=True)
    hjwhf = models.CharField(max_length=1, blank=True, null=True)
    dqjcf = models.CharField(max_length=1, blank=True, null=True)
    bgd_lb = models.CharField(max_length=1, blank=True, null=True)
    ms = models.CharField(max_length=2000, blank=True, null=True)
    zd = models.CharField(max_length=2000, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_health_question'


class JjHealthQuestionBasic(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=10, blank=True, null=True)
    xb = models.CharField(max_length=2, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    jc_hiv = models.CharField(max_length=1, blank=True, null=True)
    jc_rpr = models.CharField(max_length=1, blank=True, null=True)
    jc_zgxbjc = models.CharField(max_length=1, blank=True, null=True)
    jc_zy = models.CharField(max_length=2, blank=True, null=True)
    jc_xl = models.CharField(max_length=1, blank=True, null=True)
    hy_wh = models.CharField(max_length=1, blank=True, null=True)
    hy_yh = models.CharField(max_length=1, blank=True, null=True)
    hy_dj = models.CharField(max_length=1, blank=True, null=True)
    hy_tj = models.CharField(max_length=1, blank=True, null=True)
    hy_lh = models.CharField(max_length=1, blank=True, null=True)
    hy_se = models.CharField(max_length=1, blank=True, null=True)
    xx = models.CharField(max_length=1, blank=True, null=True)
    shsp = models.CharField(max_length=1, blank=True, null=True)
    yyjsj = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_health_question_basic'


class JjHealthQuestionCurrent(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=10, blank=True, null=True)
    xb = models.CharField(max_length=2, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    mq_xzfz = models.CharField(max_length=1, blank=True, null=True)
    mq_gjhzbx = models.CharField(max_length=1, blank=True, null=True)
    mq_xbcx = models.CharField(max_length=1, blank=True, null=True)
    mq_tzdx = models.CharField(max_length=1, blank=True, null=True)
    mq_hxkn = models.CharField(max_length=1, blank=True, null=True)
    mq_sybj = models.CharField(max_length=1, blank=True, null=True)
    mq_dewt = models.CharField(max_length=1, blank=True, null=True)
    mq_dbdx = models.CharField(max_length=1, blank=True, null=True)
    mq_dbfh = models.CharField(max_length=1, blank=True, null=True)
    mq_cfwt = models.CharField(max_length=1, blank=True, null=True)
    mq_pbgb = models.CharField(max_length=1, blank=True, null=True)
    mq_xnf = models.CharField(max_length=1, blank=True, null=True)
    mq_emf = models.CharField(max_length=1, blank=True, null=True)
    mq_yxf = models.CharField(max_length=1, blank=True, null=True)
    mq_tzjq = models.CharField(max_length=1, blank=True, null=True)
    mq_btks = models.CharField(max_length=1, blank=True, null=True)
    mq_zcf = models.CharField(max_length=1, blank=True, null=True)
    mq_zysbhf = models.CharField(max_length=1, blank=True, null=True)
    mq_byskf = models.CharField(max_length=1, blank=True, null=True)
    mq_jbykf = models.CharField(max_length=1, blank=True, null=True)
    mq_kqklf = models.CharField(max_length=1, blank=True, null=True)
    mq_tjf = models.CharField(max_length=1, blank=True, null=True)
    mq_tjnl = models.CharField(max_length=2, blank=True, null=True)
    mq_zjyj_n = models.CharField(max_length=1, blank=True, null=True)
    mq_zjyj_y = models.CharField(max_length=2, blank=True, null=True)
    mq_zjyj_r1 = models.CharField(max_length=2, blank=True, null=True)
    mq_bzccx = models.CharField(max_length=1, blank=True, null=True)
    mq_xxwcx = models.CharField(max_length=1, blank=True, null=True)
    mq_yjgd = models.CharField(max_length=1, blank=True, null=True)
    mq_tj = models.CharField(max_length=1, blank=True, null=True)
    mq_jqts = models.CharField(max_length=1, blank=True, null=True)
    mq_yjzqgzf = models.CharField(max_length=1, blank=True, null=True)
    mq_hfkbf = models.CharField(max_length=1, blank=True, null=True)
    mq_fkssf = models.CharField(max_length=1, blank=True, null=True)
    mq_rfttzk = models.CharField(max_length=1, blank=True, null=True)
    mq_rtfmwbx = models.CharField(max_length=1, blank=True, null=True)
    mq_hycs = models.CharField(max_length=1, blank=True, null=True)
    mq_sccs = models.CharField(max_length=1, blank=True, null=True)
    mq_dythy = models.CharField(max_length=1, blank=True, null=True)
    mq_nxbr = models.CharField(max_length=1, blank=True, null=True)
    mq_byf = models.CharField(max_length=1, blank=True, null=True)
    mq_byff = models.CharField(max_length=1, blank=True, null=True)
    mq_gwcy = models.CharField(max_length=1, blank=True, null=True)
    mq_gwdxbhf = models.CharField(max_length=1, blank=True, null=True)
    mq_gwynttf = models.CharField(max_length=1, blank=True, null=True)
    mq_qlxkdf = models.CharField(max_length=1, blank=True, null=True)
    mq_xbknf = models.CharField(max_length=1, blank=True, null=True)
    mq_yjxbf = models.CharField(max_length=1, blank=True, null=True)
    mq_yjxbcs = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    mq_zjyj_r2 = models.CharField(max_length=1, blank=True, null=True)
    mq_syf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_health_question_current'


class JjHealthQuestionCustom(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=10, blank=True, null=True)
    xb = models.CharField(max_length=2, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    cy_mt = models.CharField(max_length=1, blank=True, null=True)
    cy_esy = models.CharField(max_length=1, blank=True, null=True)
    cy_er = models.CharField(max_length=1, blank=True, null=True)
    cy_ytyb = models.CharField(max_length=1, blank=True, null=True)
    cy_yteb = models.CharField(max_length=1, blank=True, null=True)
    cy_jyyn = models.CharField(max_length=1, blank=True, null=True)
    cy_bcy = models.CharField(max_length=1, blank=True, null=True)
    hj_lxj = models.CharField(max_length=1, blank=True, null=True)
    hj_ddj = models.CharField(max_length=1, blank=True, null=True)
    hj_ptj = models.CharField(max_length=1, blank=True, null=True)
    hj_hj = models.CharField(max_length=1, blank=True, null=True)
    hj_pj = models.CharField(max_length=1, blank=True, null=True)
    hj_mth = models.CharField(max_length=1, blank=True, null=True)
    hj_mzsdwc = models.CharField(max_length=1, blank=True, null=True)
    hj_mzydec = models.CharField(max_length=1, blank=True, null=True)
    hj_erh = models.CharField(max_length=1, blank=True, null=True)
    hj_mcsyel = models.CharField(max_length=1, blank=True, null=True)
    hj_mcdyel = models.CharField(max_length=1, blank=True, null=True)
    gzqd = models.CharField(max_length=1, blank=True, null=True)
    nx_prq = models.CharField(max_length=1, blank=True, null=True)
    nx_hyq = models.CharField(max_length=1, blank=True, null=True)
    nx_fbrhyq = models.CharField(max_length=1, blank=True, null=True)
    wh_wlxwh = models.CharField(max_length=1, blank=True, null=True)
    wh_rtlxwh = models.CharField(max_length=1, blank=True, null=True)
    wh_fc = models.CharField(max_length=1, blank=True, null=True)
    wh_hxwz = models.CharField(max_length=1, blank=True, null=True)
    wh_wwh = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_health_question_custom'


class JjHealthQuestionHistory(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=10, blank=True, null=True)
    xb = models.CharField(max_length=2, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    fyyw_nsy = models.CharField(max_length=1, blank=True, null=True)
    fyyw_xzby = models.CharField(max_length=1, blank=True, null=True)
    fyyw_gxyy = models.CharField(max_length=1, blank=True, null=True)
    fyyw_tnby = models.CharField(max_length=1, blank=True, null=True)
    fyyw_jzxy = models.CharField(max_length=1, blank=True, null=True)
    fyyw_gxzy = models.CharField(max_length=1, blank=True, null=True)
    fyyw_xcy = models.CharField(max_length=1, blank=True, null=True)
    fyyw_zdj = models.CharField(max_length=1, blank=True, null=True)
    fyyw_lgcy = models.CharField(max_length=1, blank=True, null=True)
    fyyw_xjs = models.CharField(max_length=1, blank=True, null=True)
    fyyw_zty = models.CharField(max_length=1, blank=True, null=True)
    fyyw_cwy = models.CharField(max_length=1, blank=True, null=True)
    fyyw_zy = models.CharField(max_length=1, blank=True, null=True)
    fyyw_jsky = models.CharField(max_length=1, blank=True, null=True)
    fyyw_wssy = models.CharField(max_length=1, blank=True, null=True)
    ywgmf = models.CharField(max_length=1, blank=True, null=True)
    jb_gxy = models.CharField(max_length=1, blank=True, null=True)
    jb_gxz = models.CharField(max_length=1, blank=True, null=True)
    jb_tnb = models.CharField(max_length=1, blank=True, null=True)
    jb_jzxjb = models.CharField(max_length=1, blank=True, null=True)
    jb_xzb = models.CharField(max_length=1, blank=True, null=True)
    jb_gxb = models.CharField(max_length=1, blank=True, null=True)
    jb_dmyh = models.CharField(max_length=1, blank=True, null=True)
    jb_nxg = models.CharField(max_length=1, blank=True, null=True)
    jb_xc = models.CharField(max_length=1, blank=True, null=True)
    jb_jh = models.CharField(max_length=1, blank=True, null=True)
    jb_xhxky = models.CharField(max_length=1, blank=True, null=True)
    jb_gy = models.CharField(max_length=1, blank=True, null=True)
    jb_gyh = models.CharField(max_length=1, blank=True, null=True)
    jb_sb = models.CharField(max_length=1, blank=True, null=True)
    jb_mlxtjs = models.CharField(max_length=1, blank=True, null=True)
    jb_ns = models.CharField(max_length=1, blank=True, null=True)
    jb_px = models.CharField(max_length=1, blank=True, null=True)
    jb_gjy = models.CharField(max_length=1, blank=True, null=True)
    jb_bya = models.CharField(max_length=1, blank=True, null=True)
    jb_fa = models.CharField(max_length=1, blank=True, null=True)
    jb_ra = models.CharField(max_length=1, blank=True, null=True)
    jb_wa = models.CharField(max_length=1, blank=True, null=True)
    jb_ga = models.CharField(max_length=1, blank=True, null=True)
    jb_zca = models.CharField(max_length=1, blank=True, null=True)
    jb_jgja = models.CharField(max_length=1, blank=True, null=True)
    jb_qlxa = models.CharField(max_length=1, blank=True, null=True)
    jb_qtaz = models.CharField(max_length=1, blank=True, null=True)
    jb_qt = models.CharField(max_length=1, blank=True, null=True)
    jb_wysjb = models.CharField(max_length=1, blank=True, null=True)
    ss_n = models.CharField(max_length=1, blank=True, null=True)
    ss_y = models.CharField(max_length=1, blank=True, null=True)
    ss_jzx = models.CharField(max_length=1, blank=True, null=True)
    ss_ebh = models.CharField(max_length=1, blank=True, null=True)
    ss_f = models.CharField(max_length=1, blank=True, null=True)
    ss_xz = models.CharField(max_length=1, blank=True, null=True)
    ss_x = models.CharField(max_length=1, blank=True, null=True)
    ss_wb = models.CharField(max_length=1, blank=True, null=True)
    ss_dndg = models.CharField(max_length=1, blank=True, null=True)
    ss_sz = models.CharField(max_length=1, blank=True, null=True)
    ss_nwqc = models.CharField(max_length=1, blank=True, null=True)
    ss_qtxhqg = models.CharField(max_length=1, blank=True, null=True)
    ss_qlx = models.CharField(max_length=1, blank=True, null=True)
    ss_fk = models.CharField(max_length=1, blank=True, null=True)
    ss_gk = models.CharField(max_length=1, blank=True, null=True)
    ss_qt = models.CharField(max_length=1, blank=True, null=True)
    ss_wss = models.CharField(max_length=1, blank=True, null=True)
    qs_bya = models.CharField(max_length=1, blank=True, null=True)
    qs_fa = models.CharField(max_length=1, blank=True, null=True)
    qs_ra = models.CharField(max_length=1, blank=True, null=True)
    qs_wa = models.CharField(max_length=1, blank=True, null=True)
    qs_ga = models.CharField(max_length=1, blank=True, null=True)
    qs_zca = models.CharField(max_length=1, blank=True, null=True)
    qs_zgja = models.CharField(max_length=1, blank=True, null=True)
    qs_qlxa = models.CharField(max_length=1, blank=True, null=True)
    qs_qtaz = models.CharField(max_length=1, blank=True, null=True)
    qs_gxy = models.CharField(max_length=1, blank=True, null=True)
    qs_tnb = models.CharField(max_length=1, blank=True, null=True)
    qs_nxgjb = models.CharField(max_length=1, blank=True, null=True)
    qs_xzxgjb = models.CharField(max_length=1, blank=True, null=True)
    qs_jzxpx = models.CharField(max_length=1, blank=True, null=True)
    qs_qtjzxjb = models.CharField(max_length=1, blank=True, null=True)
    qs_w = models.CharField(max_length=1, blank=True, null=True)
    zxqs_az = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_health_question_history'


class JjHealthQuestionSportsEat(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=10, blank=True, null=True)
    xb = models.CharField(max_length=2, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    yd_qdyd = models.CharField(max_length=1, blank=True, null=True)
    yd_szyd = models.CharField(max_length=1, blank=True, null=True)
    yd_zdyd = models.CharField(max_length=1, blank=True, null=True)
    yd_jlyd = models.CharField(max_length=1, blank=True, null=True)
    ys_dsdl = models.CharField(max_length=1, blank=True, null=True)
    ys_ssz = models.CharField(max_length=1, blank=True, null=True)
    ys_hnnl = models.CharField(max_length=1, blank=True, null=True)
    ys_rzpl = models.CharField(max_length=1, blank=True, null=True)
    ys_dll = models.CharField(max_length=1, blank=True, null=True)
    ys_rll = models.CharField(max_length=1, blank=True, null=True)
    ys_scpl = models.CharField(max_length=1, blank=True, null=True)
    ys_nzl_gz = models.CharField(max_length=1, blank=True, null=True)
    ys_nzl_n = models.CharField(max_length=1, blank=True, null=True)
    ys_nzl_qt = models.CharField(max_length=1, blank=True, null=True)
    ys_dzpl = models.CharField(max_length=1, blank=True, null=True)
    ys_dsscl = models.CharField(max_length=1, blank=True, null=True)
    ys_ssscl = models.CharField(max_length=1, blank=True, null=True)
    ys_scyysll = models.CharField(max_length=1, blank=True, null=True)
    ys_sgll = models.CharField(max_length=1, blank=True, null=True)
    ys_mfmzpl = models.CharField(max_length=1, blank=True, null=True)
    ys_wgzll = models.CharField(max_length=1, blank=True, null=True)
    ys_ychjyzpl = models.CharField(max_length=1, blank=True, null=True)
    ys_gjll = models.CharField(max_length=1, blank=True, null=True)
    ys_mbl = models.CharField(max_length=1, blank=True, null=True)
    ys_yll = models.CharField(max_length=1, blank=True, null=True)
    ys_yzyjl = models.CharField(max_length=1, blank=True, null=True)
    ys_bp_w = models.CharField(max_length=1, blank=True, null=True)
    ys_bp_wssc = models.CharField(max_length=1, blank=True, null=True)
    ys_bp_wsse = models.CharField(max_length=1, blank=True, null=True)
    ys_bp_gj = models.CharField(max_length=1, blank=True, null=True)
    ys_bp_tj = models.CharField(max_length=1, blank=True, null=True)
    ys_bp_wlys = models.CharField(max_length=1, blank=True, null=True)
    ys_bp_dsj = models.CharField(max_length=1, blank=True, null=True)
    ys_bp_zwxws = models.CharField(max_length=1, blank=True, null=True)
    ys_bp_shyy = models.CharField(max_length=1, blank=True, null=True)
    ys_bp_ygy = models.CharField(max_length=1, blank=True, null=True)
    ys_bp_llz = models.CharField(max_length=1, blank=True, null=True)
    ys_bp_fj = models.CharField(max_length=1, blank=True, null=True)
    ys_bp_zl = models.CharField(max_length=1, blank=True, null=True)
    ys_bp_hf = models.CharField(max_length=1, blank=True, null=True)
    ys_bp_rsj = models.CharField(max_length=1, blank=True, null=True)
    ys_bp_qtzcy = models.CharField(max_length=1, blank=True, null=True)
    ys_jcll = models.CharField(max_length=1, blank=True, null=True)
    ys_fbml = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    mq_jy_hqzl = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_health_question_sports_eat'


class JjHf2018List(models.Model):
    billcode = models.CharField(max_length=200, blank=True, null=True)
    cid = models.CharField(max_length=30, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    hfnr = models.CharField(max_length=2000, blank=True, null=True)
    hfsj = models.DateField(blank=True, null=True)
    hfr = models.CharField(max_length=50, blank=True, null=True)
    hfr_name = models.CharField(max_length=100, blank=True, null=True)
    xc_hfsj = models.DateField(blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=300, blank=True, null=True)
    bz3 = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_hf2018_list'


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


class JjHydwdeMx(models.Model):
    dh = models.CharField(max_length=12, blank=True, null=True)
    dwdm = models.CharField(max_length=12, blank=True, null=True)
    dwmc = models.CharField(max_length=100, blank=True, null=True)
    de = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    deye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_hydwde_mx'


class JjHydwdeSy(models.Model):
    dh = models.CharField(max_length=12, blank=True, null=True)
    bz = models.CharField(max_length=100, blank=True, null=True)
    lrry = models.CharField(max_length=6, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    shry = models.CharField(max_length=6, blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_hydwde_sy'


class JjInternetTransList2018(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    cid = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    bz = models.CharField(max_length=200, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    czsj1 = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_internet_trans_list2018'


class JjItemQmDict(models.Model):
    item_id = models.CharField(max_length=20, blank=True, null=True)
    jc_oper = models.CharField(max_length=100, blank=True, null=True)
    sh_oper = models.CharField(max_length=100, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_item_qm_dict'


class JjJcmxb(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    groupid = models.CharField(max_length=10, blank=True, null=True)
    groupname = models.CharField(max_length=100, blank=True, null=True)
    item_id = models.CharField(max_length=6, blank=True, null=True)
    item_name = models.CharField(max_length=40, blank=True, null=True)
    item_ename = models.CharField(max_length=40, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    standard = models.CharField(max_length=20, blank=True, null=True)
    begtime = models.DateField(blank=True, null=True)
    endtime = models.DateField(blank=True, null=True)
    checkoper = models.CharField(max_length=6, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    checkdept = models.CharField(max_length=6, blank=True, null=True)
    audit_oper = models.CharField(max_length=20, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    item_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    group_en = models.CharField(max_length=50, blank=True, null=True)
    group_ft = models.CharField(max_length=50, blank=True, null=True)
    item_en = models.CharField(max_length=50, blank=True, null=True)
    item_ft = models.CharField(max_length=50, blank=True, null=True)
    add_number = models.IntegerField(blank=True, null=True)
    check_opername = models.CharField(max_length=20, blank=True, null=True)
    sort_time = models.DateField(blank=True, null=True)
    init_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_jcmxb'


class JjJcmxbBack(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    groupid = models.CharField(max_length=10, blank=True, null=True)
    groupname = models.CharField(max_length=100, blank=True, null=True)
    item_id = models.CharField(max_length=6, blank=True, null=True)
    item_name = models.CharField(max_length=40, blank=True, null=True)
    item_ename = models.CharField(max_length=40, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    standard = models.CharField(max_length=20, blank=True, null=True)
    begtime = models.DateField(blank=True, null=True)
    endtime = models.DateField(blank=True, null=True)
    checkoper = models.CharField(max_length=6, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    checkdept = models.CharField(max_length=6, blank=True, null=True)
    audit_oper = models.CharField(max_length=20, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    item_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    group_en = models.CharField(max_length=50, blank=True, null=True)
    group_ft = models.CharField(max_length=50, blank=True, null=True)
    item_en = models.CharField(max_length=50, blank=True, null=True)
    item_ft = models.CharField(max_length=50, blank=True, null=True)
    add_number = models.IntegerField(blank=True, null=True)
    check_opername = models.CharField(max_length=20, blank=True, null=True)
    sort_time = models.DateField(blank=True, null=True)
    init_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_jcmxb_back'


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


class JjJzFklist(models.Model):
    jzdhm = models.CharField(max_length=14, blank=True, null=True)
    xh = models.IntegerField(blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    fkfs = models.CharField(max_length=2, blank=True, null=True)
    fkfsje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    hl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    zsje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bz = models.CharField(max_length=30, blank=True, null=True)
    ye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    zscs = models.IntegerField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    ls_jzsj = models.DateField(blank=True, null=True)
    dqjzr = models.CharField(max_length=10, blank=True, null=True)
    other_fkfs = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_jz_fklist'


class JjJzFklist201011(models.Model):
    jzdhm = models.CharField(max_length=14, blank=True, null=True)
    xh = models.IntegerField(blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    fkfs = models.CharField(max_length=2, blank=True, null=True)
    fkfsje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    hl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    zsje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bz = models.CharField(max_length=30, blank=True, null=True)
    ye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    zscs = models.IntegerField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    ls_jzsj = models.DateField(blank=True, null=True)
    dqjzr = models.CharField(max_length=10, blank=True, null=True)
    other_fkfs = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_jz_fklist_201011'


class JjJzqkb(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    jzdhm = models.CharField(max_length=14, blank=True, null=True)
    jzfs = models.CharField(max_length=2, blank=True, null=True)
    bzbl = models.FloatField(blank=True, null=True)
    fphm = models.CharField(max_length=15, blank=True, null=True)
    jzzje = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fpje = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    jzrdm = models.CharField(max_length=6, blank=True, null=True)
    jzsj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    qxrdm = models.CharField(max_length=6, blank=True, null=True)
    qxsj = models.DateField(blank=True, null=True)
    xjzdhm = models.CharField(max_length=14, blank=True, null=True)
    bz = models.CharField(max_length=100, blank=True, null=True)
    sfcd = models.CharField(max_length=1, blank=True, null=True)
    xfphm = models.CharField(max_length=15, blank=True, null=True)
    cdrdm = models.CharField(max_length=6, blank=True, null=True)
    cdsj = models.DateField(blank=True, null=True)
    jzfmc = models.CharField(max_length=60, blank=True, null=True)
    jzlx = models.CharField(max_length=1, blank=True, null=True)
    kjy = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    fpqx = models.CharField(max_length=1, blank=True, null=True)
    gcfpry = models.CharField(max_length=6, blank=True, null=True)
    tczje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_jzqkb'


class JjJzqkb201011(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    jzdhm = models.CharField(max_length=14, blank=True, null=True)
    jzfs = models.CharField(max_length=2, blank=True, null=True)
    bzbl = models.FloatField(blank=True, null=True)
    fphm = models.CharField(max_length=15, blank=True, null=True)
    jzzje = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fpje = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    jzrdm = models.CharField(max_length=6, blank=True, null=True)
    jzsj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    qxrdm = models.CharField(max_length=6, blank=True, null=True)
    qxsj = models.DateField(blank=True, null=True)
    xjzdhm = models.CharField(max_length=14, blank=True, null=True)
    bz = models.CharField(max_length=100, blank=True, null=True)
    sfcd = models.CharField(max_length=1, blank=True, null=True)
    xfphm = models.CharField(max_length=15, blank=True, null=True)
    cdrdm = models.CharField(max_length=6, blank=True, null=True)
    cdsj = models.DateField(blank=True, null=True)
    jzfmc = models.CharField(max_length=60, blank=True, null=True)
    jzlx = models.CharField(max_length=1, blank=True, null=True)
    kjy = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    fpqx = models.CharField(max_length=1, blank=True, null=True)
    gcfpry = models.CharField(max_length=6, blank=True, null=True)
    tczje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_jzqkb_201011'


class JjMndjkQeustion(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    lb = models.CharField(max_length=50, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    djry = models.CharField(max_length=100, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    nr1 = models.CharField(max_length=50, blank=True, null=True)
    nr2 = models.CharField(max_length=50, blank=True, null=True)
    nr3 = models.CharField(max_length=50, blank=True, null=True)
    nr4 = models.CharField(max_length=50, blank=True, null=True)
    nr5 = models.CharField(max_length=50, blank=True, null=True)
    nr6 = models.CharField(max_length=50, blank=True, null=True)
    nr7 = models.CharField(max_length=50, blank=True, null=True)
    nr8 = models.CharField(max_length=50, blank=True, null=True)
    nr9 = models.CharField(max_length=50, blank=True, null=True)
    nr10 = models.CharField(max_length=50, blank=True, null=True)
    nr11 = models.CharField(max_length=50, blank=True, null=True)
    nr12 = models.CharField(max_length=50, blank=True, null=True)
    nr13 = models.CharField(max_length=50, blank=True, null=True)
    nr14 = models.CharField(max_length=50, blank=True, null=True)
    nr15 = models.CharField(max_length=50, blank=True, null=True)
    nr16 = models.CharField(max_length=50, blank=True, null=True)
    nr17 = models.CharField(max_length=50, blank=True, null=True)
    nr18 = models.CharField(max_length=50, blank=True, null=True)
    nr19 = models.CharField(max_length=50, blank=True, null=True)
    nr20 = models.CharField(max_length=50, blank=True, null=True)
    nr21 = models.CharField(max_length=50, blank=True, null=True)
    nr22 = models.CharField(max_length=50, blank=True, null=True)
    nr23 = models.CharField(max_length=50, blank=True, null=True)
    nr24 = models.CharField(max_length=50, blank=True, null=True)
    nr25 = models.CharField(max_length=50, blank=True, null=True)
    nr26 = models.CharField(max_length=50, blank=True, null=True)
    nr27 = models.CharField(max_length=50, blank=True, null=True)
    nr28 = models.CharField(max_length=50, blank=True, null=True)
    nr29 = models.CharField(max_length=50, blank=True, null=True)
    nr30 = models.CharField(max_length=50, blank=True, null=True)
    nr31 = models.CharField(max_length=50, blank=True, null=True)
    nr32 = models.CharField(max_length=50, blank=True, null=True)
    nr33 = models.CharField(max_length=50, blank=True, null=True)
    nr34 = models.CharField(max_length=50, blank=True, null=True)
    nr35 = models.CharField(max_length=50, blank=True, null=True)
    nr36 = models.CharField(max_length=50, blank=True, null=True)
    nr37 = models.CharField(max_length=50, blank=True, null=True)
    nr38 = models.CharField(max_length=50, blank=True, null=True)
    nr39 = models.CharField(max_length=50, blank=True, null=True)
    nr40 = models.CharField(max_length=50, blank=True, null=True)
    nr41 = models.CharField(max_length=50, blank=True, null=True)
    nr42 = models.CharField(max_length=50, blank=True, null=True)
    nr43 = models.CharField(max_length=50, blank=True, null=True)
    nr44 = models.CharField(max_length=50, blank=True, null=True)
    nr45 = models.CharField(max_length=50, blank=True, null=True)
    nr46 = models.CharField(max_length=50, blank=True, null=True)
    nr47 = models.CharField(max_length=50, blank=True, null=True)
    nr48 = models.CharField(max_length=50, blank=True, null=True)
    nr49 = models.CharField(max_length=50, blank=True, null=True)
    nr50 = models.CharField(max_length=50, blank=True, null=True)
    nr51 = models.CharField(max_length=50, blank=True, null=True)
    nr52 = models.CharField(max_length=50, blank=True, null=True)
    nr53 = models.CharField(max_length=50, blank=True, null=True)
    nr54 = models.CharField(max_length=50, blank=True, null=True)
    nr55 = models.CharField(max_length=50, blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    bz4 = models.CharField(max_length=200, blank=True, null=True)
    bz5 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_mndjk_qeustion'


class JjMndjkQeustionBack(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    lb = models.CharField(max_length=50, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    djry = models.CharField(max_length=100, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    nr1 = models.CharField(max_length=50, blank=True, null=True)
    nr2 = models.CharField(max_length=50, blank=True, null=True)
    nr3 = models.CharField(max_length=50, blank=True, null=True)
    nr4 = models.CharField(max_length=50, blank=True, null=True)
    nr5 = models.CharField(max_length=50, blank=True, null=True)
    nr6 = models.CharField(max_length=50, blank=True, null=True)
    nr7 = models.CharField(max_length=50, blank=True, null=True)
    nr8 = models.CharField(max_length=50, blank=True, null=True)
    nr9 = models.CharField(max_length=50, blank=True, null=True)
    nr10 = models.CharField(max_length=50, blank=True, null=True)
    nr11 = models.CharField(max_length=50, blank=True, null=True)
    nr12 = models.CharField(max_length=50, blank=True, null=True)
    nr13 = models.CharField(max_length=50, blank=True, null=True)
    nr14 = models.CharField(max_length=50, blank=True, null=True)
    nr15 = models.CharField(max_length=50, blank=True, null=True)
    nr16 = models.CharField(max_length=50, blank=True, null=True)
    nr17 = models.CharField(max_length=50, blank=True, null=True)
    nr18 = models.CharField(max_length=50, blank=True, null=True)
    nr19 = models.CharField(max_length=50, blank=True, null=True)
    nr20 = models.CharField(max_length=50, blank=True, null=True)
    nr21 = models.CharField(max_length=50, blank=True, null=True)
    nr22 = models.CharField(max_length=50, blank=True, null=True)
    nr23 = models.CharField(max_length=50, blank=True, null=True)
    nr24 = models.CharField(max_length=50, blank=True, null=True)
    nr25 = models.CharField(max_length=50, blank=True, null=True)
    nr26 = models.CharField(max_length=50, blank=True, null=True)
    nr27 = models.CharField(max_length=50, blank=True, null=True)
    nr28 = models.CharField(max_length=50, blank=True, null=True)
    nr29 = models.CharField(max_length=50, blank=True, null=True)
    nr30 = models.CharField(max_length=50, blank=True, null=True)
    nr31 = models.CharField(max_length=50, blank=True, null=True)
    nr32 = models.CharField(max_length=50, blank=True, null=True)
    nr33 = models.CharField(max_length=50, blank=True, null=True)
    nr34 = models.CharField(max_length=50, blank=True, null=True)
    nr35 = models.CharField(max_length=50, blank=True, null=True)
    nr36 = models.CharField(max_length=50, blank=True, null=True)
    nr37 = models.CharField(max_length=50, blank=True, null=True)
    nr38 = models.CharField(max_length=50, blank=True, null=True)
    nr39 = models.CharField(max_length=50, blank=True, null=True)
    nr40 = models.CharField(max_length=50, blank=True, null=True)
    nr41 = models.CharField(max_length=50, blank=True, null=True)
    nr42 = models.CharField(max_length=50, blank=True, null=True)
    nr43 = models.CharField(max_length=50, blank=True, null=True)
    nr44 = models.CharField(max_length=50, blank=True, null=True)
    nr45 = models.CharField(max_length=50, blank=True, null=True)
    nr46 = models.CharField(max_length=50, blank=True, null=True)
    nr47 = models.CharField(max_length=50, blank=True, null=True)
    nr48 = models.CharField(max_length=50, blank=True, null=True)
    nr49 = models.CharField(max_length=50, blank=True, null=True)
    nr50 = models.CharField(max_length=50, blank=True, null=True)
    nr51 = models.CharField(max_length=50, blank=True, null=True)
    nr52 = models.CharField(max_length=50, blank=True, null=True)
    nr53 = models.CharField(max_length=50, blank=True, null=True)
    nr54 = models.CharField(max_length=50, blank=True, null=True)
    nr55 = models.CharField(max_length=50, blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    bz4 = models.CharField(max_length=200, blank=True, null=True)
    bz5 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_mndjk_qeustion_back'


class JjMultiYyInterface(models.Model):
    id = models.CharField(max_length=200, blank=True, null=True)
    vid = models.CharField(max_length=20, blank=True, null=True)
    dwdm = models.CharField(max_length=20, blank=True, null=True)
    lb = models.CharField(max_length=10, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_multi_yy_interface'


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


class JjPrintXts(models.Model):
    dm = models.CharField(max_length=10, blank=True, null=True)
    mc = models.CharField(max_length=60, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    print_datawindow = models.CharField(max_length=40, blank=True, null=True)
    print_text = models.CharField(max_length=4000, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_print_xts'


class JjQtdjBzxx(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    bz = models.CharField(max_length=1000, blank=True, null=True)
    czry = models.CharField(max_length=100, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    bz2 = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_qtdj_bzxx'


class JjReportPrintLog(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    print_time = models.DateField(blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    xb = models.CharField(max_length=100, blank=True, null=True)
    dwdm = models.CharField(max_length=60, blank=True, null=True)
    print_oper = models.CharField(max_length=60, blank=True, null=True)
    print_opername = models.CharField(max_length=60, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    page_log = models.CharField(max_length=100, blank=True, null=True)
    page_count = models.BigIntegerField(blank=True, null=True)
    print_dept = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_report_print_log'


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


class JjResultPicture(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=20, blank=True, null=True)
    xb = models.CharField(max_length=20, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    item_id = models.CharField(max_length=6, blank=True, null=True)
    item_name = models.CharField(max_length=60, blank=True, null=True)
    pic_id = models.IntegerField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    bmp_path = models.CharField(max_length=100, blank=True, null=True)
    file_name1 = models.CharField(max_length=100, blank=True, null=True)
    file_name2 = models.CharField(max_length=100, blank=True, null=True)
    file_name3 = models.CharField(max_length=100, blank=True, null=True)
    file_name4 = models.CharField(max_length=100, blank=True, null=True)
    file_name5 = models.CharField(max_length=100, blank=True, null=True)
    file_name6 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_result_picture'


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


class JjResultXts(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    xm = models.CharField(max_length=30, blank=True, null=True)
    xb = models.CharField(max_length=1, blank=True, null=True)
    xts_dm = models.CharField(max_length=10, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    tj_factory = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_result_xts'


class JjResultXts2(models.Model):
    vid = models.CharField(max_length=30, blank=True, null=True)
    item_id = models.CharField(max_length=30, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    cid = models.CharField(max_length=30, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    xb = models.CharField(max_length=10, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    nr1 = models.CharField(max_length=2000, blank=True, null=True)
    nr2 = models.CharField(max_length=2000, blank=True, null=True)
    nr3 = models.CharField(max_length=2000, blank=True, null=True)
    nr4 = models.CharField(max_length=2000, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    nr5 = models.CharField(max_length=2000, blank=True, null=True)
    column_height = models.IntegerField(blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    nr6 = models.CharField(max_length=2000, blank=True, null=True)
    nr7 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_result_xts_2'


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


class JjSdfxbgList(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    lb = models.CharField(max_length=20, blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    cid = models.CharField(max_length=100, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    xb = models.CharField(max_length=100, blank=True, null=True)
    dwdm = models.CharField(max_length=100, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    czopername = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    scsj = models.DateField(blank=True, null=True)
    scopername = models.CharField(max_length=100, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_sdfxbg_list'


class JjSfmxb(models.Model):
    sfmxid = models.CharField(max_length=14, blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    groupid = models.CharField(max_length=10, blank=True, null=True)
    groupname = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    standard = models.CharField(max_length=20, blank=True, null=True)
    jzf = models.CharField(max_length=1, blank=True, null=True)
    jzdhm = models.CharField(max_length=14, blank=True, null=True)
    oldprice = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    jxf = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    user_id = models.CharField(max_length=6, blank=True, null=True)
    member_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    sf_ywydm = models.CharField(max_length=6, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_sfmxb'


class JjSfmxb201011(models.Model):
    sfmxid = models.CharField(max_length=14, blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    groupid = models.CharField(max_length=10, blank=True, null=True)
    groupname = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    standard = models.CharField(max_length=20, blank=True, null=True)
    jzf = models.CharField(max_length=1, blank=True, null=True)
    jzdhm = models.CharField(max_length=14, blank=True, null=True)
    oldprice = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    jxf = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    user_id = models.CharField(max_length=6, blank=True, null=True)
    member_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    sf_ywydm = models.CharField(max_length=6, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_sfmxb_201011'


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


class JjTraceYclog(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    cid = models.CharField(max_length=20, blank=True, null=True)
    dwdm = models.CharField(max_length=30, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    je = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bz1 = models.CharField(max_length=50, blank=True, null=True)
    bz2 = models.CharField(max_length=50, blank=True, null=True)
    bz3 = models.CharField(max_length=50, blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_trace_yclog'


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


class JjTtyySy(models.Model):
    id = models.CharField(max_length=12, blank=True, null=True)
    dwdm = models.CharField(max_length=12, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    ywydm = models.CharField(max_length=6, blank=True, null=True)
    status = models.CharField(max_length=6, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    djry = models.CharField(max_length=10, blank=True, null=True)
    print_time = models.DateField(blank=True, null=True)
    print_ry = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_ttyy_sy'


class JjVidCxGsList(models.Model):
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    vid = models.CharField(max_length=20, blank=True, null=True)
    ys = models.CharField(max_length=30, blank=True, null=True)
    gx = models.CharField(max_length=50, blank=True, null=True)
    sl = models.IntegerField(blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_vid_cx_gs_list'


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


class JjVidOtherTrans2(models.Model):
    lx = models.CharField(max_length=10, blank=True, null=True)
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
        db_table = 'jj_vid_other_trans2'


class JjWjdcb(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    wjdm = models.CharField(max_length=4, blank=True, null=True)
    wjmc = models.CharField(max_length=100, blank=True, null=True)
    wjjg = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_wjdcb'


class JjWsResults(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    item_id = models.CharField(max_length=30, blank=True, null=True)
    xm = models.CharField(max_length=60, blank=True, null=True)
    xb = models.CharField(max_length=60, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    create_oper = models.CharField(max_length=30, blank=True, null=True)
    send_date = models.DateField(blank=True, null=True)
    send_oper = models.CharField(max_length=20, blank=True, null=True)
    field_results = models.CharField(max_length=1000, blank=True, null=True)
    audit_date = models.DateField(blank=True, null=True)
    audit_oper = models.CharField(max_length=30, blank=True, null=True)
    audit_opername = models.CharField(max_length=30, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_ws_results'


class JjYcbwResults(models.Model):
    vid = models.CharField(max_length=10, blank=True, null=True)
    t = models.CharField(max_length=10, blank=True, null=True)
    yj = models.CharField(max_length=10, blank=True, null=True)
    ebh = models.CharField(max_length=10, blank=True, null=True)
    kq = models.CharField(max_length=10, blank=True, null=True)
    jdm = models.CharField(max_length=10, blank=True, null=True)
    xz = models.CharField(max_length=10, blank=True, null=True)
    jzyz = models.CharField(max_length=10, blank=True, null=True)
    xq = models.CharField(max_length=10, blank=True, null=True)
    ybjc = models.CharField(max_length=10, blank=True, null=True)
    nk = models.CharField(max_length=10, blank=True, null=True)
    wk = models.CharField(max_length=10, blank=True, null=True)
    qt = models.CharField(max_length=10, blank=True, null=True)
    jzx = models.CharField(max_length=10, blank=True, null=True)
    rf = models.CharField(max_length=10, blank=True, null=True)
    g = models.CharField(max_length=10, blank=True, null=True)
    d = models.CharField(max_length=10, blank=True, null=True)
    y = models.CharField(max_length=10, blank=True, null=True)
    p = models.CharField(max_length=10, blank=True, null=True)
    s = models.CharField(max_length=10, blank=True, null=True)
    wc = models.CharField(max_length=10, blank=True, null=True)
    fk = models.CharField(max_length=10, blank=True, null=True)
    zgfj = models.CharField(max_length=10, blank=True, null=True)
    ny = models.CharField(max_length=10, blank=True, null=True)
    zlxy = models.CharField(max_length=10, blank=True, null=True)
    qtxy = models.CharField(max_length=10, blank=True, null=True)
    qlx = models.CharField(max_length=10, blank=True, null=True)
    pgsng = models.CharField(max_length=10, blank=True, null=True)
    bz1 = models.CharField(max_length=10, blank=True, null=True)
    bz2 = models.CharField(max_length=10, blank=True, null=True)
    bz3 = models.CharField(max_length=10, blank=True, null=True)
    bz4 = models.CharField(max_length=10, blank=True, null=True)
    bz5 = models.CharField(max_length=10, blank=True, null=True)
    in_factory = models.CharField(max_length=10, blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    xb = models.CharField(max_length=10, blank=True, null=True)
    tzzs = models.CharField(max_length=10, blank=True, null=True)
    xy = models.CharField(max_length=10, blank=True, null=True)
    xt = models.CharField(max_length=10, blank=True, null=True)
    x_xz = models.CharField(max_length=10, blank=True, null=True)
    sg = models.CharField(max_length=10, blank=True, null=True)
    gg = models.CharField(max_length=10, blank=True, null=True)
    zl = models.CharField(max_length=10, blank=True, null=True)
    zcf = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_ycbw_results'


class JjYgldbPrint(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    print_opername = models.CharField(max_length=100, blank=True, null=True)
    print_time = models.DateField(blank=True, null=True)
    zjsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_ygldb_print'


class JjYqfqList(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    item_id = models.CharField(max_length=30, blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    cid = models.CharField(max_length=30, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    xb = models.CharField(max_length=10, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    dwdm = models.CharField(max_length=100, blank=True, null=True)
    sfzhm = models.CharField(max_length=100, blank=True, null=True)
    fgs = models.CharField(max_length=300, blank=True, null=True)
    bm1 = models.CharField(max_length=300, blank=True, null=True)
    bm2 = models.CharField(max_length=300, blank=True, null=True)
    ygh = models.CharField(max_length=300, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    clsj = models.DateField(blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_yqfq_list'


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


class JjYyqkb(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"VID")
    cid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"CID")
    dwdm = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"单位代码")
    yysj = models.DateField(blank=True, null=True, verbose_name=u"预约时间")
    yyzh = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"VID")
    yydjr = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"VID")
    yydjsj = models.DateField(blank=True, null=True)
    jjzh = models.CharField(max_length=5, blank=True, null=True)
    jjlsh = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"预约状态")
    qtdjr = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"VID")
    qtdjsj = models.DateField(blank=True, null=True)
    tjsj = models.DateField(blank=True, null=True)
    tjzzsj = models.DateField(blank=True, null=True)
    tzf = models.CharField(max_length=1, blank=True, null=True)
    dwjzf = models.CharField(max_length=1, blank=True, null=True)
    member_type = models.CharField(max_length=2, blank=True, null=True)
    yydhtzr = models.CharField(max_length=25, blank=True, null=True)
    yyth = models.CharField(max_length=12, blank=True, null=True)
    zyf = models.CharField(max_length=1, blank=True, null=True)
    jjch = models.CharField(max_length=12, blank=True, null=True)
    print_time = models.DateField(blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    ywydm = models.CharField(max_length=6, blank=True, null=True)
    yqhff = models.CharField(max_length=1, blank=True, null=True)
    erqhff = models.CharField(max_length=1, blank=True, null=True)
    sqhff = models.CharField(max_length=1, blank=True, null=True)
    tcbl = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    dwyyid = models.CharField(max_length=30, blank=True, null=True)
    cust_name = models.CharField(max_length=50, blank=True, null=True)
    cust_xb = models.CharField(max_length=2, blank=True, null=True)
    cust_csrq = models.DateField(blank=True, null=True)
    temp_bz = models.CharField(max_length=3000, blank=True, null=True, verbose_name=u"套餐名称变更")
    cust_zy = models.CharField(max_length=20, blank=True, null=True)
    cust_gzhy = models.CharField(max_length=20, blank=True, null=True)
    zzys = models.CharField(max_length=6, blank=True, null=True)
    zzhs = models.CharField(max_length=6, blank=True, null=True)
    in_floor = models.CharField(max_length=10, blank=True, null=True)
    gzhy_dm = models.CharField(max_length=20, blank=True, null=True)
    bz_fgs = models.CharField(max_length=200, blank=True, null=True)
    bz_bm1 = models.CharField(max_length=200, blank=True, null=True)
    bz_bm2 = models.CharField(max_length=200, blank=True, null=True)
    bz_ygh = models.CharField(max_length=200, blank=True, null=True)
    bz_sfzhm = models.CharField(max_length=200, blank=True, null=True)
    bz_a = models.CharField(max_length=200, blank=True, null=True)
    bz_b = models.CharField(max_length=200, blank=True, null=True)
    bz_c = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"老的VID")
    bz_xj = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bz_gz = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bz_lpk = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_yyqkb'


class JjYyqkb201011(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    dwdm = models.CharField(max_length=12, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    yyzh = models.CharField(max_length=2, blank=True, null=True)
    yydjr = models.CharField(max_length=6, blank=True, null=True)
    yydjsj = models.DateField(blank=True, null=True)
    jjzh = models.CharField(max_length=2, blank=True, null=True)
    jjlsh = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    qtdjr = models.CharField(max_length=6, blank=True, null=True)
    qtdjsj = models.DateField(blank=True, null=True)
    tjsj = models.DateField(blank=True, null=True)
    tjzzsj = models.DateField(blank=True, null=True)
    tzf = models.CharField(max_length=1, blank=True, null=True)
    dwjzf = models.CharField(max_length=1, blank=True, null=True)
    member_type = models.CharField(max_length=2, blank=True, null=True)
    yydhtzr = models.CharField(max_length=25, blank=True, null=True)
    yyth = models.CharField(max_length=12, blank=True, null=True)
    zyf = models.CharField(max_length=1, blank=True, null=True)
    jjch = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"报告单方式")
    print_time = models.DateField(blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    ywydm = models.CharField(max_length=6, blank=True, null=True)
    yqhff = models.CharField(max_length=1, blank=True, null=True)
    erqhff = models.CharField(max_length=1, blank=True, null=True)
    sqhff = models.CharField(max_length=1, blank=True, null=True)
    tcbl = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    dwyyid = models.CharField(max_length=30, blank=True, null=True)
    cust_name = models.CharField(max_length=50, blank=True, null=True)
    cust_xb = models.CharField(max_length=2, blank=True, null=True)
    cust_csrq = models.DateField(blank=True, null=True)
    temp_bz = models.CharField(max_length=3000, blank=True, null=True)
    cust_zy = models.CharField(max_length=20, blank=True, null=True)
    cust_gzhy = models.CharField(max_length=20, blank=True, null=True)
    zzys = models.CharField(max_length=6, blank=True, null=True)
    zzhs = models.CharField(max_length=6, blank=True, null=True)
    in_floor = models.CharField(max_length=10, blank=True, null=True)
    gzhy_dm = models.CharField(max_length=20, blank=True, null=True)
    bz_fgs = models.CharField(max_length=200, blank=True, null=True)
    bz_bm1 = models.CharField(max_length=200, blank=True, null=True)
    bz_bm2 = models.CharField(max_length=200, blank=True, null=True)
    bz_ygh = models.CharField(max_length=200, blank=True, null=True)
    bz_sfzhm = models.CharField(max_length=200, blank=True, null=True)
    bz_a = models.CharField(max_length=200, blank=True, null=True)
    bz_b = models.CharField(max_length=200, blank=True, null=True)
    bz_c = models.CharField(max_length=200, blank=True, null=True)
    bz_xj = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bz_gz = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bz_lpk = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_yyqkb_201011'


class JjYyqkbBack(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    dwdm = models.CharField(max_length=12, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    yyzh = models.CharField(max_length=2, blank=True, null=True)
    yydjr = models.CharField(max_length=6, blank=True, null=True)
    yydjsj = models.DateField(blank=True, null=True)
    jjzh = models.CharField(max_length=2, blank=True, null=True)
    jjlsh = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    qtdjr = models.CharField(max_length=6, blank=True, null=True)
    qtdjsj = models.DateField(blank=True, null=True)
    tjsj = models.DateField(blank=True, null=True)
    tjzzsj = models.DateField(blank=True, null=True)
    tzf = models.CharField(max_length=1, blank=True, null=True)
    dwjzf = models.CharField(max_length=1, blank=True, null=True)
    member_type = models.CharField(max_length=2, blank=True, null=True)
    yydhtzr = models.CharField(max_length=25, blank=True, null=True)
    yyth = models.CharField(max_length=12, blank=True, null=True)
    zyf = models.CharField(max_length=1, blank=True, null=True)
    jjch = models.CharField(max_length=12, blank=True, null=True)
    print_time = models.DateField(blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    ywydm = models.CharField(max_length=6, blank=True, null=True)
    yqhff = models.CharField(max_length=1, blank=True, null=True)
    erqhff = models.CharField(max_length=1, blank=True, null=True)
    sqhff = models.CharField(max_length=1, blank=True, null=True)
    tcbl = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    dwyyid = models.CharField(max_length=30, blank=True, null=True)
    cust_name = models.CharField(max_length=50, blank=True, null=True)
    cust_xb = models.CharField(max_length=2, blank=True, null=True)
    cust_csrq = models.DateField(blank=True, null=True)
    temp_bz = models.CharField(max_length=3000, blank=True, null=True)
    cust_zy = models.CharField(max_length=20, blank=True, null=True)
    cust_gzhy = models.CharField(max_length=20, blank=True, null=True)
    zzys = models.CharField(max_length=6, blank=True, null=True)
    zzhs = models.CharField(max_length=6, blank=True, null=True)
    in_floor = models.CharField(max_length=10, blank=True, null=True)
    gzhy_dm = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_yyqkb_back'


class JjYyqkbTdbgList(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    xb = models.CharField(max_length=10, blank=True, null=True)
    hyzk = models.CharField(max_length=100, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    sfzhm = models.CharField(max_length=50, blank=True, null=True)
    fgs = models.CharField(max_length=300, blank=True, null=True)
    bm1 = models.CharField(max_length=300, blank=True, null=True)
    bm2 = models.CharField(max_length=300, blank=True, null=True)
    ygh = models.CharField(max_length=300, blank=True, null=True)
    dwdm = models.CharField(max_length=50, blank=True, null=True)
    dwyyid = models.CharField(max_length=100, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)
    bz4 = models.CharField(max_length=100, blank=True, null=True)
    bz5 = models.CharField(max_length=100, blank=True, null=True)
    bz6 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_yyqkb_tdbg_list'


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


class JjZbbcData2019(models.Model):
    billcode = models.CharField(max_length=100, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)
    localvid = models.CharField(max_length=30, blank=True, null=True)
    xm = models.CharField(max_length=200, blank=True, null=True)
    sfzhm = models.CharField(max_length=100, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    point_name = models.CharField(max_length=300, blank=True, null=True)
    item_name = models.CharField(max_length=300, blank=True, null=True)
    field_comment = models.CharField(max_length=300, blank=True, null=True)
    field_results = models.CharField(max_length=3500, blank=True, null=True)
    sss = models.CharField(max_length=10, blank=True, null=True)
    qcs = models.CharField(max_length=10, blank=True, null=True)
    lb = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_zbbc_data2019'


class JjZczdMszd(models.Model):
    dm = models.CharField(max_length=4, blank=True, null=True)
    mc = models.CharField(max_length=30, blank=True, null=True)
    sjdm = models.CharField(max_length=4, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_zczd_mszd'


class JjZqqcDj(models.Model):
    billcode = models.CharField(max_length=150, blank=True, null=True)
    cid = models.CharField(max_length=50, blank=True, null=True)
    vid = models.CharField(max_length=50, blank=True, null=True)
    sfzhm = models.CharField(max_length=100, blank=True, null=True)
    xm = models.CharField(max_length=200, blank=True, null=True)
    nr = models.CharField(max_length=220, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    lrry = models.CharField(max_length=100, blank=True, null=True)
    lrks = models.CharField(max_length=200, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    bz4 = models.CharField(max_length=200, blank=True, null=True)
    bz5 = models.CharField(max_length=200, blank=True, null=True)
    trans_status1 = models.CharField(max_length=10, blank=True, null=True)
    trans_status2 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj_zqqc_dj'


class LisAdviceRepeatDetail(models.Model):
    bill_code = models.CharField(max_length=8, blank=True, null=True)
    testitem_id = models.CharField(max_length=6, blank=True, null=True)
    item_value1 = models.CharField(max_length=20, blank=True, null=True)
    item_value2 = models.CharField(max_length=20, blank=True, null=True)
    item_value3 = models.CharField(max_length=20, blank=True, null=True)
    advice_type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_advice_repeat_detail'


class LisAdviceRepeatIndex(models.Model):
    bill_code = models.CharField(max_length=8, blank=True, null=True)
    advice_title = models.CharField(max_length=200, blank=True, null=True)
    sfjb = models.CharField(max_length=1, blank=True, null=True)
    advice_context = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    zd_title = models.CharField(max_length=200, blank=True, null=True)
    lx = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_advice_repeat_index'


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


class LisAuditOther(models.Model):
    testitem_id = models.CharField(max_length=30, blank=True, null=True)
    value_h = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    value_yx = models.CharField(max_length=10, blank=True, null=True)
    value_l = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_audit_other'


class LisBaseItemBl(models.Model):
    testitem_id = models.CharField(max_length=30, blank=True, null=True)
    bl = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_base_item_bl'


class LisBigLbList(models.Model):
    lb = models.CharField(max_length=60, blank=True, null=True)
    big_sxh = models.IntegerField(blank=True, null=True)
    testitem_id = models.CharField(max_length=30, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_big_lb_list'


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


class LisCooperationAnomalous(models.Model):
    recodenumber = models.FloatField(blank=True, null=True)
    anomaloustype = models.CharField(max_length=1, blank=True, null=True)
    anomalousdate = models.DateField(blank=True, null=True)
    anomalouscode = models.CharField(max_length=20, blank=True, null=True)
    anomalouslog = models.CharField(max_length=100, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    inputperson = models.CharField(max_length=10, blank=True, null=True)
    inputpersonname = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    disposetime = models.DateField(blank=True, null=True)
    disposeperson = models.CharField(max_length=10, blank=True, null=True)
    disposepersonname = models.CharField(max_length=50, blank=True, null=True)
    in_factory = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_cooperation_anomalous'


class LisCooperationCriticalvalue(models.Model):
    recordnumber = models.FloatField(blank=True, null=True)
    cooperationcriticalvaluetype = models.CharField(max_length=1, blank=True, null=True)
    criticalvaluetype = models.CharField(max_length=1, blank=True, null=True)
    mechanismcode = models.CharField(max_length=10, blank=True, null=True)
    mechanismname = models.CharField(max_length=100, blank=True, null=True)
    cid = models.CharField(max_length=8, blank=True, null=True)
    vid = models.CharField(max_length=10, blank=True, null=True)
    sampleid = models.CharField(max_length=14, blank=True, null=True)
    sampleordertime = models.DateField(blank=True, null=True)
    testgroupcode = models.CharField(max_length=10, blank=True, null=True)
    testgroupname = models.CharField(max_length=100, blank=True, null=True)
    testcode = models.CharField(max_length=10, blank=True, null=True)
    testname = models.CharField(max_length=100, blank=True, null=True)
    testresult = models.CharField(max_length=400, blank=True, null=True)
    testunit = models.CharField(max_length=50, blank=True, null=True)
    testhint = models.CharField(max_length=1, blank=True, null=True)
    testrrs = models.CharField(max_length=1000, blank=True, null=True)
    receivetime = models.DateField(blank=True, null=True)
    receiveperson = models.CharField(max_length=10, blank=True, null=True)
    receivepersonname = models.CharField(max_length=50, blank=True, null=True)
    testtime = models.DateField(blank=True, null=True)
    testperson = models.CharField(max_length=10, blank=True, null=True)
    testpersonname = models.CharField(max_length=50, blank=True, null=True)
    checktime = models.DateField(blank=True, null=True)
    checkperson = models.CharField(max_length=10, blank=True, null=True)
    checkpersonname = models.CharField(max_length=50, blank=True, null=True)
    completetime = models.DateField(blank=True, null=True)
    completeperson = models.CharField(max_length=10, blank=True, null=True)
    completepersonname = models.CharField(max_length=50, blank=True, null=True)
    testhinttype = models.CharField(max_length=1, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    inputperson = models.CharField(max_length=10, blank=True, null=True)
    inputpersonname = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    valuereadtime = models.DateField(blank=True, null=True)
    valuereadperson = models.CharField(max_length=10, blank=True, null=True)
    valuereadpersonname = models.CharField(max_length=50, blank=True, null=True)
    valuechecktime = models.DateField(blank=True, null=True)
    valuecheckperson = models.CharField(max_length=10, blank=True, null=True)
    valuecheckpersonname = models.CharField(max_length=50, blank=True, null=True)
    invalidatedate = models.DateField(blank=True, null=True)
    invalidateperson = models.CharField(max_length=10, blank=True, null=True)
    invalidatepersonname = models.CharField(max_length=50, blank=True, null=True)
    in_factory = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_cooperation_criticalvalue'


class LisCooperationEmployee(models.Model):
    mechanismcode = models.CharField(max_length=10, blank=True, null=True)
    mechanismname = models.CharField(max_length=100, blank=True, null=True)
    employeecode = models.CharField(max_length=6, blank=True, null=True)
    employeename = models.CharField(max_length=50, blank=True, null=True)
    contrastemployeecode = models.CharField(max_length=20, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    inputperson = models.CharField(max_length=6, blank=True, null=True)
    inputpersonname = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    invalidatedate = models.DateField(blank=True, null=True)
    invalidateperson = models.CharField(max_length=6, blank=True, null=True)
    invalidatepersonname = models.CharField(max_length=50, blank=True, null=True)
    in_factory = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_cooperation_employee'


class LisCooperationTestcontrast(models.Model):
    mechanismcode = models.CharField(max_length=10, blank=True, null=True)
    mechanismname = models.CharField(max_length=100, blank=True, null=True)
    deviceid = models.CharField(max_length=4, blank=True, null=True)
    devicename = models.CharField(max_length=40, blank=True, null=True)
    testgroupcode = models.CharField(max_length=10, blank=True, null=True)
    testgroupname = models.CharField(max_length=100, blank=True, null=True)
    testcode = models.CharField(max_length=10, blank=True, null=True)
    testname = models.CharField(max_length=100, blank=True, null=True)
    contrasttestcode = models.CharField(max_length=100, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    inputperson = models.CharField(max_length=6, blank=True, null=True)
    inputpersonname = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    invalidatedate = models.DateField(blank=True, null=True)
    invalidateperson = models.CharField(max_length=6, blank=True, null=True)
    invalidatepersonname = models.CharField(max_length=50, blank=True, null=True)
    in_factory = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_cooperation_testcontrast'


class LisGroupApparatus(models.Model):
    sample_type_id = models.CharField(max_length=4, blank=True, null=True)
    apparatusid = models.CharField(max_length=4, blank=True, null=True)
    groupid = models.CharField(max_length=6, blank=True, null=True)
    sfdlwc = models.CharField(max_length=1, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_group_apparatus'


class LisGroupItem(models.Model):
    groupid = models.CharField(max_length=6, blank=True, null=True)
    testitem_id = models.CharField(max_length=6, blank=True, null=True)
    dyzbm = models.CharField(max_length=10, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_group_item'


class LisHi701(models.Model):
    xh = models.IntegerField(blank=True, null=True)
    mc = models.CharField(max_length=30, blank=True, null=True)
    dw = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_hi701'


class LisJsgsDict(models.Model):
    appid = models.CharField(max_length=100, blank=True, null=True)
    testitem_id = models.CharField(max_length=100, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    jsgs = models.CharField(max_length=1000, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    xsd = models.IntegerField(blank=True, null=True)
    bz = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_jsgs_dict'


class LisJtTestItem(models.Model):
    lb = models.CharField(max_length=50, blank=True, null=True)
    jt_item_id = models.CharField(max_length=100, blank=True, null=True)
    jt_item_name = models.CharField(max_length=200, blank=True, null=True)
    local_item_id = models.CharField(max_length=100, blank=True, null=True)
    local_item_id_2 = models.CharField(max_length=100, blank=True, null=True)
    in_factory = models.CharField(max_length=100, blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_jt_test_item'


class LisQcBatchnumber(models.Model):
    qcbatchnumber = models.CharField(max_length=50, blank=True, null=True)
    qcproductname = models.CharField(max_length=100, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    manufacturedate = models.DateField(blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    inputperson = models.CharField(max_length=10, blank=True, null=True)
    inputpersonname = models.CharField(max_length=50, blank=True, null=True)
    enabledate = models.DateField(blank=True, null=True)
    enableperson = models.CharField(max_length=10, blank=True, null=True)
    enablepersonname = models.CharField(max_length=50, blank=True, null=True)
    expirydate = models.DateField(blank=True, null=True)
    states = models.CharField(max_length=1, blank=True, null=True)
    invalidatedate = models.DateField(blank=True, null=True)
    invalidateperson = models.CharField(max_length=10, blank=True, null=True)
    invalidatepersonname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_qc_batchnumber'


class LisQcDefaulttester(models.Model):
    deviceid = models.CharField(max_length=10, blank=True, null=True)
    devicename = models.CharField(max_length=50, blank=True, null=True)
    defaulttesterid = models.CharField(max_length=10, blank=True, null=True)
    defaulttestername = models.CharField(max_length=50, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    inputperson = models.CharField(max_length=10, blank=True, null=True)
    inputpersonname = models.CharField(max_length=50, blank=True, null=True)
    states = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_qc_defaulttester'


class LisQcDevicecontrast(models.Model):
    deviceid = models.CharField(max_length=10, blank=True, null=True)
    qcbatchnumber = models.CharField(max_length=50, blank=True, null=True)
    devicename = models.CharField(max_length=100, blank=True, null=True)
    positiontype = models.CharField(max_length=1, blank=True, null=True)
    qcpositionno = models.CharField(max_length=4, blank=True, null=True)
    qcpositiondetailedno = models.CharField(max_length=4, blank=True, null=True)
    contrastdeviceid = models.CharField(max_length=10, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    inputperson = models.CharField(max_length=10, blank=True, null=True)
    inputpersonname = models.CharField(max_length=50, blank=True, null=True)
    enabledate = models.DateField(blank=True, null=True)
    enableperson = models.CharField(max_length=10, blank=True, null=True)
    enablepersonname = models.CharField(max_length=50, blank=True, null=True)
    states = models.CharField(max_length=1, blank=True, null=True)
    invalidatedate = models.DateField(blank=True, null=True)
    invalidateperson = models.CharField(max_length=10, blank=True, null=True)
    invalidatepersonname = models.CharField(max_length=50, blank=True, null=True)
    qcresulttype = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_qc_devicecontrast'


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


class LisQcMonthreport(models.Model):
    monthreportid = models.FloatField(blank=True, null=True)
    monthreportname = models.CharField(max_length=50, blank=True, null=True)
    reportdate = models.DateField(blank=True, null=True)
    begindate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    deviceid = models.CharField(max_length=4, blank=True, null=True)
    devicename = models.CharField(max_length=40, blank=True, null=True)
    programmeid = models.CharField(max_length=10, blank=True, null=True)
    programmename = models.CharField(max_length=50, blank=True, null=True)
    qcbatchnumber = models.CharField(max_length=50, blank=True, null=True)
    qcproductname = models.CharField(max_length=100, blank=True, null=True)
    qctestid = models.CharField(max_length=10, blank=True, null=True)
    qctestname = models.CharField(max_length=50, blank=True, null=True)
    qctestenglishname = models.CharField(max_length=50, blank=True, null=True)
    monthsummaryinfo = models.CharField(max_length=4000, blank=True, null=True)
    outcontrolprocess = models.CharField(max_length=4000, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    inputperson = models.CharField(max_length=10, blank=True, null=True)
    inputpersonname = models.CharField(max_length=50, blank=True, null=True)
    confirmationdate = models.DateField(blank=True, null=True)
    confirmationperson = models.CharField(max_length=10, blank=True, null=True)
    confirmationpersonname = models.CharField(max_length=50, blank=True, null=True)
    states = models.CharField(max_length=1, blank=True, null=True)
    invalidatedate = models.DateField(blank=True, null=True)
    invalidateperson = models.CharField(max_length=10, blank=True, null=True)
    invalidatepersonname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_qc_monthreport'


class LisQcOutcontrolprocess(models.Model):
    outcontrolid = models.CharField(max_length=10, blank=True, null=True)
    qcbatchnumber = models.CharField(max_length=50, blank=True, null=True)
    qcbatchname = models.CharField(max_length=200, blank=True, null=True)
    qctestid = models.CharField(max_length=10, blank=True, null=True)
    qctestname = models.CharField(max_length=50, blank=True, null=True)
    deviceid = models.CharField(max_length=10, blank=True, null=True)
    devicename = models.CharField(max_length=50, blank=True, null=True)
    programmeid = models.CharField(max_length=10, blank=True, null=True)
    programmename = models.CharField(max_length=50, blank=True, null=True)
    outcontroldate = models.DateField(blank=True, null=True)
    qctestresultvalue = models.CharField(max_length=10, blank=True, null=True)
    qctestsdvalue = models.CharField(max_length=10, blank=True, null=True)
    resultcondition = models.CharField(max_length=50, blank=True, null=True)
    judgementcondition = models.CharField(max_length=200, blank=True, null=True)
    reagentbatchnumber = models.CharField(max_length=50, blank=True, null=True)
    calibratorbatchernumber = models.CharField(max_length=50, blank=True, null=True)
    causeanalysis = models.CharField(max_length=2000, blank=True, null=True)
    processingprocess = models.CharField(max_length=2000, blank=True, null=True)
    processingresults = models.CharField(max_length=500, blank=True, null=True)
    states = models.CharField(max_length=1, blank=True, null=True)
    qcresultbatch = models.CharField(max_length=10, blank=True, null=True)
    processdate = models.DateField(blank=True, null=True)
    processperson = models.CharField(max_length=10, blank=True, null=True)
    processpersonname = models.CharField(max_length=50, blank=True, null=True)
    resultsource = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_qc_outcontrolprocess'


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


class LisQcProgramme(models.Model):
    programmeid = models.CharField(max_length=10, blank=True, null=True)
    programmename = models.CharField(max_length=50, blank=True, null=True)
    deviceid = models.CharField(max_length=10, blank=True, null=True)
    devicename = models.CharField(max_length=50, blank=True, null=True)
    programmeprofile = models.CharField(max_length=2, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    inputperson = models.CharField(max_length=10, blank=True, null=True)
    inputpersonname = models.CharField(max_length=50, blank=True, null=True)
    enabledate = models.DateField(blank=True, null=True)
    enableperson = models.CharField(max_length=10, blank=True, null=True)
    enablepersonname = models.CharField(max_length=50, blank=True, null=True)
    states = models.CharField(max_length=1, blank=True, null=True)
    invalidatedate = models.DateField(blank=True, null=True)
    invalidateperson = models.CharField(max_length=10, blank=True, null=True)
    invalidatepersonname = models.CharField(max_length=50, blank=True, null=True)
    drawtype = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_qc_programme'


class LisQcProgrammeseting(models.Model):
    programmeid = models.CharField(max_length=10, blank=True, null=True)
    programmesetingtype = models.CharField(max_length=1, blank=True, null=True)
    programmecontrast = models.CharField(max_length=50, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    inputperson = models.CharField(max_length=10, blank=True, null=True)
    inputpersonname = models.CharField(max_length=50, blank=True, null=True)
    enabledate = models.DateField(blank=True, null=True)
    enableperson = models.CharField(max_length=10, blank=True, null=True)
    enablepersonname = models.CharField(max_length=50, blank=True, null=True)
    states = models.CharField(max_length=1, blank=True, null=True)
    invalidatedate = models.DateField(blank=True, null=True)
    invalidateperson = models.CharField(max_length=10, blank=True, null=True)
    invalidatepersonname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_qc_programmeseting'


class LisQcResult(models.Model):
    controldate = models.DateField(blank=True, null=True)
    control_id = models.IntegerField(blank=True, null=True)
    sampleid = models.CharField(max_length=12, blank=True, null=True)
    labsequenceno = models.IntegerField(blank=True, null=True)
    testid = models.CharField(max_length=6, blank=True, null=True)
    qc_results = models.CharField(max_length=30, blank=True, null=True)
    testtime = models.DateField(blank=True, null=True)
    qc_operator = models.CharField(max_length=6, blank=True, null=True)
    flag_log = models.NullBooleanField()
    rec_log = models.CharField(max_length=100, blank=True, null=True)
    flag_redo = models.NullBooleanField()
    rec_redo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_qc_result'


class LisQcResultvalue(models.Model):
    qcresultvalueid = models.CharField(max_length=10, blank=True, null=True)
    qcbatchnumber = models.CharField(max_length=50, blank=True, null=True)
    qcbatchname = models.CharField(max_length=100, blank=True, null=True)
    deviceid = models.CharField(max_length=10, blank=True, null=True)
    devicename = models.CharField(max_length=50, blank=True, null=True)
    programmeid = models.CharField(max_length=10, blank=True, null=True)
    programmename = models.CharField(max_length=50, blank=True, null=True)
    qctestid = models.CharField(max_length=10, blank=True, null=True)
    qctestname = models.CharField(max_length=50, blank=True, null=True)
    qctestenglishname = models.CharField(max_length=50, blank=True, null=True)
    qctestresultvalue = models.CharField(max_length=10, blank=True, null=True)
    qctestsdvalue = models.CharField(max_length=10, blank=True, null=True)
    qctesttargetvalue = models.CharField(max_length=10, blank=True, null=True)
    qcresultstate = models.CharField(max_length=1, blank=True, null=True)
    states = models.CharField(max_length=1, blank=True, null=True)
    qctestdate = models.DateField(blank=True, null=True)
    qcresultbatch = models.CharField(max_length=10, blank=True, null=True)
    qctestperson = models.CharField(max_length=10, blank=True, null=True)
    qctestpersonname = models.CharField(max_length=50, blank=True, null=True)
    resultsource = models.CharField(max_length=1, blank=True, null=True)
    qcteststandarddeviation = models.CharField(max_length=10, blank=True, null=True)
    qctestcoefficientvariation = models.CharField(max_length=10, blank=True, null=True)
    iscalculate = models.CharField(max_length=1, blank=True, null=True)
    isdraw = models.CharField(max_length=1, blank=True, null=True)
    qclowqualitative = models.CharField(max_length=10, blank=True, null=True)
    qchighqualitative = models.CharField(max_length=10, blank=True, null=True)
    qctestvaluetype = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_qc_resultvalue'


class LisQcSummarytemplate(models.Model):
    templateid = models.CharField(max_length=10, blank=True, null=True)
    deviceid = models.CharField(max_length=10, blank=True, null=True)
    devicename = models.CharField(max_length=50, blank=True, null=True)
    templatecontent = models.CharField(max_length=4000, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    inputperson = models.CharField(max_length=10, blank=True, null=True)
    inputpersonname = models.CharField(max_length=50, blank=True, null=True)
    states = models.CharField(max_length=1, blank=True, null=True)
    invalidatedate = models.DateField(blank=True, null=True)
    invalidateperson = models.CharField(max_length=10, blank=True, null=True)
    invalidatepersonname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_qc_summarytemplate'


class LisQcTargetvalue(models.Model):
    qcbatchnumber = models.CharField(max_length=50, blank=True, null=True)
    deviceid = models.CharField(max_length=10, blank=True, null=True)
    devicename = models.CharField(max_length=50, blank=True, null=True)
    qctestid = models.CharField(max_length=10, blank=True, null=True)
    qctestname = models.CharField(max_length=50, blank=True, null=True)
    qctestenglishname = models.CharField(max_length=50, blank=True, null=True)
    qctestsampletype = models.CharField(max_length=2, blank=True, null=True)
    qctestvaluetype = models.CharField(max_length=1, blank=True, null=True)
    targetvalue = models.CharField(max_length=10, blank=True, null=True)
    standarddeviation = models.CharField(max_length=10, blank=True, null=True)
    coefficientvariation = models.CharField(max_length=10, blank=True, null=True)
    qclowqualitative = models.CharField(max_length=10, blank=True, null=True)
    qchighqualitative = models.CharField(max_length=10, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    inputperson = models.CharField(max_length=10, blank=True, null=True)
    inputpersonname = models.CharField(max_length=50, blank=True, null=True)
    states = models.CharField(max_length=1, blank=True, null=True)
    invalidatedate = models.DateField(blank=True, null=True)
    invalidateperson = models.CharField(max_length=10, blank=True, null=True)
    invalidatepersonname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_qc_targetvalue'


class LisQcTestcontrast(models.Model):
    qctestid = models.CharField(max_length=20, blank=True, null=True)
    qcbatchnumber = models.CharField(max_length=50, blank=True, null=True)
    qctestname = models.CharField(max_length=50, blank=True, null=True)
    qctestenglishname = models.CharField(max_length=100, blank=True, null=True)
    qctestsampletype = models.CharField(max_length=2, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    inputperson = models.CharField(max_length=10, blank=True, null=True)
    inputpersonname = models.CharField(max_length=50, blank=True, null=True)
    states = models.CharField(max_length=1, blank=True, null=True)
    invalidatedate = models.DateField(blank=True, null=True)
    invalidateperson = models.CharField(max_length=10, blank=True, null=True)
    invalidatepersonname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_qc_testcontrast'


class LisQcTestvaluecontrast(models.Model):
    qcbatchnumber = models.CharField(max_length=50, blank=True, null=True)
    deviceid = models.CharField(max_length=10, blank=True, null=True)
    devicename = models.CharField(max_length=50, blank=True, null=True)
    qctestid = models.CharField(max_length=10, blank=True, null=True)
    qctestname = models.CharField(max_length=50, blank=True, null=True)
    qctestenglishname = models.CharField(max_length=50, blank=True, null=True)
    devicevalue = models.CharField(max_length=10, blank=True, null=True)
    qcvalue = models.CharField(max_length=10, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    inputperson = models.CharField(max_length=10, blank=True, null=True)
    inputpersonname = models.CharField(max_length=50, blank=True, null=True)
    states = models.CharField(max_length=1, blank=True, null=True)
    invalidatedate = models.DateField(blank=True, null=True)
    invalidateperson = models.CharField(max_length=10, blank=True, null=True)
    invalidatepersonname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_qc_testvaluecontrast'


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


class LisSampleMiddle(models.Model):
    apparatusid = models.CharField(max_length=4, blank=True, null=True)
    no = models.IntegerField(blank=True, null=True)
    readed = models.CharField(max_length=1, blank=True, null=True)
    com_text = models.TextField(blank=True, null=True)  # This field type is a guess.
    accepttime = models.DateField(blank=True, null=True)
    xh = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_sample_middle'


class LisSampleOrder(models.Model):
    cid = models.CharField(max_length=12, blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    sampleid = models.CharField(max_length=18, blank=True, null=True)
    send_to_group = models.CharField(max_length=6, blank=True, null=True)
    groupid = models.CharField(max_length=6, blank=True, null=True)
    groupname = models.CharField(max_length=100, blank=True, null=True)
    quatity_of_sample = models.IntegerField(blank=True, null=True)
    sample_send_time = models.DateField(blank=True, null=True)
    who_sampling = models.CharField(max_length=6, blank=True, null=True)
    sample_send_dept = models.CharField(max_length=4, blank=True, null=True)
    sample_receive_time = models.DateField(blank=True, null=True)
    who_receive = models.CharField(max_length=6, blank=True, null=True)
    rec_qualified = models.CharField(max_length=100, blank=True, null=True)
    apparatusid = models.CharField(max_length=4, blank=True, null=True)
    labsequenceno = models.IntegerField(blank=True, null=True)
    extappratus = models.CharField(max_length=4, blank=True, null=True)
    expsequence = models.IntegerField(blank=True, null=True)
    completetime = models.DateField(blank=True, null=True)
    completeoperator = models.CharField(max_length=6, blank=True, null=True)
    checktime = models.DateField(blank=True, null=True)
    checkoperator = models.CharField(max_length=6, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    xm = models.CharField(max_length=10, blank=True, null=True)
    coll_operator = models.CharField(max_length=6, blank=True, null=True)
    coll_time = models.DateField(blank=True, null=True)
    sample_type_id = models.CharField(max_length=4, blank=True, null=True)
    sfgroupid = models.CharField(max_length=10, blank=True, null=True)
    jyid = models.CharField(max_length=6, blank=True, null=True)
    djxhsj = models.DateField(blank=True, null=True)
    djxhry = models.CharField(max_length=6, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    sample_name = models.CharField(max_length=20, blank=True, null=True)
    sample_xb = models.CharField(max_length=2, blank=True, null=True)
    sample_csrq = models.DateField(blank=True, null=True)
    sample_yysj = models.DateField(blank=True, null=True)
    item_en = models.CharField(max_length=50, blank=True, null=True)
    item_ft = models.CharField(max_length=50, blank=True, null=True)
    add_number = models.IntegerField(blank=True, null=True)
    complete_opername = models.CharField(max_length=20, blank=True, null=True)
    red_green = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_sample_order'


class LisSampleOrderBack(models.Model):
    cid = models.CharField(max_length=12, blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    sampleid = models.CharField(max_length=18, blank=True, null=True)
    send_to_group = models.CharField(max_length=6, blank=True, null=True)
    groupid = models.CharField(max_length=6, blank=True, null=True)
    groupname = models.CharField(max_length=100, blank=True, null=True)
    quatity_of_sample = models.IntegerField(blank=True, null=True)
    sample_send_time = models.DateField(blank=True, null=True)
    who_sampling = models.CharField(max_length=6, blank=True, null=True)
    sample_send_dept = models.CharField(max_length=4, blank=True, null=True)
    sample_receive_time = models.DateField(blank=True, null=True)
    who_receive = models.CharField(max_length=6, blank=True, null=True)
    rec_qualified = models.CharField(max_length=100, blank=True, null=True)
    apparatusid = models.CharField(max_length=4, blank=True, null=True)
    labsequenceno = models.IntegerField(blank=True, null=True)
    extappratus = models.CharField(max_length=4, blank=True, null=True)
    expsequence = models.IntegerField(blank=True, null=True)
    completetime = models.DateField(blank=True, null=True)
    completeoperator = models.CharField(max_length=6, blank=True, null=True)
    checktime = models.DateField(blank=True, null=True)
    checkoperator = models.CharField(max_length=6, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    xm = models.CharField(max_length=10, blank=True, null=True)
    coll_operator = models.CharField(max_length=6, blank=True, null=True)
    coll_time = models.DateField(blank=True, null=True)
    sample_type_id = models.CharField(max_length=4, blank=True, null=True)
    sfgroupid = models.CharField(max_length=10, blank=True, null=True)
    jyid = models.CharField(max_length=6, blank=True, null=True)
    djxhsj = models.DateField(blank=True, null=True)
    djxhry = models.CharField(max_length=6, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    sample_name = models.CharField(max_length=20, blank=True, null=True)
    sample_xb = models.CharField(max_length=2, blank=True, null=True)
    sample_csrq = models.DateField(blank=True, null=True)
    sample_yysj = models.DateField(blank=True, null=True)
    item_en = models.CharField(max_length=50, blank=True, null=True)
    item_ft = models.CharField(max_length=50, blank=True, null=True)
    add_number = models.IntegerField(blank=True, null=True)
    complete_opername = models.CharField(max_length=20, blank=True, null=True)
    red_green = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_sample_order_back'


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


class LisTestItem(models.Model):
    testitem_id = models.CharField(max_length=6, blank=True, null=True)
    testitem_name_e = models.CharField(max_length=40, blank=True, null=True)
    testitem_name_c = models.CharField(max_length=150, blank=True, null=True)
    testitem_short = models.CharField(max_length=8, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    testmethod_id = models.CharField(max_length=4, blank=True, null=True)
    qc_method_id = models.CharField(max_length=4, blank=True, null=True)
    sjdm = models.CharField(max_length=10, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=8, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    flag_qc = models.CharField(max_length=1, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    testitem_ft = models.CharField(max_length=50, blank=True, null=True)
    init_value = models.CharField(max_length=16, blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    aid_code = models.CharField(max_length=20, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_test_item'


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


class LisTestResult(models.Model):
    cid = models.CharField(max_length=12, blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    sampleid = models.CharField(max_length=18, blank=True, null=True)
    apparatusid = models.CharField(max_length=4, blank=True, null=True)
    labsequenceno = models.IntegerField(blank=True, null=True)
    testitem_id = models.CharField(max_length=6, blank=True, null=True)
    testitem_name_e = models.CharField(max_length=40, blank=True, null=True)
    testitem_name_c = models.CharField(max_length=150, blank=True, null=True)
    testitem_short = models.CharField(max_length=8, blank=True, null=True)
    results = models.CharField(max_length=400, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    flag_log_filter = models.NullBooleanField()
    rec_log_filter = models.CharField(max_length=255, blank=True, null=True)
    flag_qc_filter = models.NullBooleanField()
    rec_qc_filter = models.CharField(max_length=100, blank=True, null=True)
    flag_redo = models.NullBooleanField()
    rec_redo = models.CharField(max_length=100, blank=True, null=True)
    flag_do_more = models.NullBooleanField()
    rec_do_more = models.CharField(max_length=100, blank=True, null=True)
    normal_l = models.CharField(max_length=40, blank=True, null=True)
    normal_h = models.CharField(max_length=40, blank=True, null=True)
    dlms = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    abnormal = models.CharField(max_length=1, blank=True, null=True)
    xh = models.IntegerField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    testitem_ft = models.CharField(max_length=50, blank=True, null=True)
    bz = models.CharField(max_length=100, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_test_result'


class LisTestResultBack(models.Model):
    cid = models.CharField(max_length=12, blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    sampleid = models.CharField(max_length=18, blank=True, null=True)
    apparatusid = models.CharField(max_length=4, blank=True, null=True)
    labsequenceno = models.IntegerField(blank=True, null=True)
    testitem_id = models.CharField(max_length=6, blank=True, null=True)
    testitem_name_e = models.CharField(max_length=40, blank=True, null=True)
    testitem_name_c = models.CharField(max_length=150, blank=True, null=True)
    testitem_short = models.CharField(max_length=8, blank=True, null=True)
    results = models.CharField(max_length=400, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    flag_log_filter = models.NullBooleanField()
    rec_log_filter = models.CharField(max_length=255, blank=True, null=True)
    flag_qc_filter = models.NullBooleanField()
    rec_qc_filter = models.CharField(max_length=100, blank=True, null=True)
    flag_redo = models.NullBooleanField()
    rec_redo = models.CharField(max_length=100, blank=True, null=True)
    flag_do_more = models.NullBooleanField()
    rec_do_more = models.CharField(max_length=100, blank=True, null=True)
    normal_l = models.CharField(max_length=40, blank=True, null=True)
    normal_h = models.CharField(max_length=40, blank=True, null=True)
    dlms = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)
    abnormal = models.CharField(max_length=1, blank=True, null=True)
    xh = models.IntegerField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    testitem_ft = models.CharField(max_length=50, blank=True, null=True)
    bz = models.CharField(max_length=100, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_test_result_back'


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


class Microsoftdtproperties(models.Model):
    id = models.FloatField(blank=True, null=True)
    objectid = models.FloatField(blank=True, null=True)
    property = models.CharField(max_length=64, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    lvalue = models.TextField(blank=True, null=True)  # This field type is a guess.
    version = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'microsoftdtproperties'


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


class MnItemLbList(models.Model):
    item_id = models.CharField(max_length=20, blank=True, null=True)
    item_lb = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mn_item_lb_list'


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


class MzJkcjsJgdzb(models.Model):
    lsh = models.CharField(max_length=19, blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    name_ch = models.CharField(max_length=200, blank=True, null=True)
    sfbt = models.CharField(max_length=10, blank=True, null=True)
    jglx = models.CharField(max_length=10, blank=True, null=True)
    jgdw = models.CharField(max_length=50, blank=True, null=True)
    groupid = models.CharField(max_length=20, blank=True, null=True)
    itemid = models.CharField(max_length=20, blank=True, null=True)
    beizhu = models.CharField(max_length=500, blank=True, null=True)
    bz1 = models.CharField(max_length=20, blank=True, null=True)
    bz2 = models.CharField(max_length=20, blank=True, null=True)
    bz3 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mz_jkcjs_jgdzb'


class MzJkwjKswt(models.Model):
    keshi = models.CharField(max_length=20, blank=True, null=True)
    questionid = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mz_jkwj_kswt'


class MzJkwjLayout(models.Model):
    questionid = models.CharField(max_length=19, blank=True, null=True)
    optionid = models.CharField(max_length=30, blank=True, null=True)
    questionno = models.CharField(max_length=200, blank=True, null=True)
    questiontype = models.CharField(max_length=1, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    x = models.BigIntegerField(blank=True, null=True)
    y = models.BigIntegerField(blank=True, null=True)
    w = models.BigIntegerField(blank=True, null=True)
    h = models.BigIntegerField(blank=True, null=True)
    adaptsexid = models.CharField(max_length=1, blank=True, null=True)
    style = models.CharField(max_length=200, blank=True, null=True)
    parentid = models.CharField(max_length=30, blank=True, null=True)
    formid = models.CharField(max_length=19, blank=True, null=True)
    questioncode = models.CharField(max_length=50, blank=True, null=True)
    optioncode = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mz_jkwj_layout'


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


class MzWjdjQueue(models.Model):
    vid = models.CharField(max_length=12, blank=True, null=True)
    leixing = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)
    createrid = models.CharField(max_length=19, blank=True, null=True)
    createdeptid = models.CharField(max_length=19, blank=True, null=True)
    createdate = models.DateField(blank=True, null=True)
    operaterid = models.CharField(max_length=19, blank=True, null=True)
    operatedeptid = models.CharField(max_length=19, blank=True, null=True)
    operatedate = models.DateField(blank=True, null=True)
    bz1 = models.CharField(max_length=20, blank=True, null=True)
    bz2 = models.CharField(max_length=50, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mz_wjdj_queue'


class OfsItems(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    parent_id = models.BigIntegerField(blank=True, null=True)
    item_type = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=256, blank=True, null=True)
    date_modified = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=256, blank=True, null=True)
    read_only = models.CharField(max_length=1, blank=True, null=True)
    compressed = models.CharField(max_length=1, blank=True, null=True)
    data = models.BinaryField(blank=True, null=True)
    locked_by = models.CharField(max_length=256, blank=True, null=True)
    date_locked = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofs_items'


class OtherCardLog(models.Model):
    card_code = models.CharField(max_length=30, blank=True, null=True)
    old_lsh = models.CharField(max_length=100, blank=True, null=True)
    lx = models.CharField(max_length=100, blank=True, null=True)
    czy_name = models.CharField(max_length=50, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    new_lsh = models.CharField(max_length=100, blank=True, null=True)
    new_card_code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_card_log'


class OtherFeeBindDetail(models.Model):
    dm = models.CharField(max_length=30, blank=True, null=True)
    item_dm = models.CharField(max_length=30, blank=True, null=True)
    lc = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    lccs = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    zsl = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_fee_bind_detail'


class OtherFeeBindIndex(models.Model):
    dm = models.CharField(max_length=30, blank=True, null=True)
    mc = models.CharField(max_length=100, blank=True, null=True)
    lx = models.CharField(max_length=1, blank=True, null=True)
    lc = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    lc_cs = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    zsl = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    sjdm = models.CharField(max_length=30, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_fee_bind_index'


class OtherFeeCard(models.Model):
    card_code = models.CharField(max_length=30, blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    card_id = models.CharField(max_length=100, blank=True, null=True)
    lx = models.CharField(max_length=10, blank=True, null=True)
    mzje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    bz = models.CharField(max_length=200, blank=True, null=True)
    zkl = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    sjje = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    dm = models.CharField(max_length=40, blank=True, null=True)
    mc = models.CharField(max_length=100, blank=True, null=True)
    card_title = models.CharField(max_length=200, blank=True, null=True)
    valid_date = models.DateField(blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    card_password = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_fee_card'


class OtherFeeCardList(models.Model):
    card_code = models.CharField(max_length=30, blank=True, null=True)
    card_id = models.CharField(max_length=100, blank=True, null=True)
    card_type = models.CharField(max_length=30, blank=True, null=True)
    dwdm = models.CharField(max_length=30, blank=True, null=True)
    dwmc = models.CharField(max_length=200, blank=True, null=True)
    ywydm = models.CharField(max_length=30, blank=True, null=True)
    sjje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    mzje = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    zkl = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    fkfs = models.CharField(max_length=10, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    xm = models.CharField(max_length=30, blank=True, null=True)
    xb = models.CharField(max_length=30, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    sfzhm = models.CharField(max_length=30, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    lx = models.CharField(max_length=10, blank=True, null=True)
    in_factory = models.CharField(max_length=10, blank=True, null=True)
    czlx = models.CharField(max_length=10, blank=True, null=True)
    kye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bz = models.CharField(max_length=200, blank=True, null=True)
    cust_child_id = models.CharField(max_length=30, blank=True, null=True)
    cust_id = models.CharField(max_length=30, blank=True, null=True)
    card_lsh = models.CharField(max_length=60, blank=True, null=True)
    id = models.CharField(max_length=100, blank=True, null=True)
    item_dm = models.CharField(max_length=30, blank=True, null=True)
    item_mc = models.CharField(max_length=100, blank=True, null=True)
    cs = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    card_title = models.CharField(max_length=100, blank=True, null=True)
    groupid = models.CharField(max_length=30, blank=True, null=True)
    djr_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_fee_card_list'


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


class OtherFeeCustFkfs(models.Model):
    jzdhm = models.CharField(max_length=20, blank=True, null=True)
    cust_child_id = models.CharField(max_length=20, blank=True, null=True)
    cust_id = models.CharField(max_length=20, blank=True, null=True)
    fkfs = models.CharField(max_length=20, blank=True, null=True)
    zsje = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qt_je1 = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qt_je2 = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    id = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)
    jzsj = models.DateField(blank=True, null=True)
    jzrdm = models.CharField(max_length=20, blank=True, null=True)
    card_code = models.CharField(max_length=20, blank=True, null=True)
    card_lsh = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_fee_cust_fkfs'


class OtherFeeCustSfmx(models.Model):
    sfmxid = models.CharField(max_length=20, blank=True, null=True)
    cust_child_id = models.CharField(max_length=20, blank=True, null=True)
    dm = models.CharField(max_length=50, blank=True, null=True)
    mc = models.CharField(max_length=300, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    gg = models.CharField(max_length=40, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    last_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    jzdhm = models.CharField(max_length=20, blank=True, null=True)
    check_num = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    check_total_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    check_last_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)
    jzsj = models.DateField(blank=True, null=True)
    bw = models.CharField(max_length=500, blank=True, null=True)
    bz4 = models.CharField(max_length=500, blank=True, null=True)
    bz5 = models.CharField(max_length=500, blank=True, null=True)
    bz6 = models.CharField(max_length=500, blank=True, null=True)
    js = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    zsl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    czy = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_fee_cust_sfmx'


class OtherTlsStatus(models.Model):
    user_id = models.CharField(max_length=30, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    in_rs = models.IntegerField(blank=True, null=True)
    not_rs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_tls_status'


class OtherYyqkItemList(models.Model):
    id = models.CharField(max_length=60, blank=True, null=True)
    dm = models.CharField(max_length=30, blank=True, null=True)
    mc = models.CharField(max_length=200, blank=True, null=True)
    bw = models.CharField(max_length=500, blank=True, null=True)
    bz4 = models.CharField(max_length=500, blank=True, null=True)
    bz5 = models.CharField(max_length=500, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    lls = models.CharField(max_length=30, blank=True, null=True)
    lls_name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    fpr = models.CharField(max_length=30, blank=True, null=True)
    fpsj = models.DateField(blank=True, null=True)
    print_time = models.DateField(blank=True, null=True)
    wcsj = models.DateField(blank=True, null=True)
    cust_id = models.CharField(max_length=30, blank=True, null=True)
    cs = models.IntegerField(blank=True, null=True)
    do_czy = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_yyqk_item_list'


class OtherZyFyList(models.Model):
    cust_id = models.CharField(max_length=30, blank=True, null=True)
    cust_child_id = models.CharField(max_length=30, blank=True, null=True)
    cid = models.CharField(max_length=30, blank=True, null=True)
    dm = models.CharField(max_length=30, blank=True, null=True)
    mc = models.CharField(max_length=200, blank=True, null=True)
    ph = models.CharField(max_length=200, blank=True, null=True)
    gg = models.CharField(max_length=100, blank=True, null=True)
    sl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    dj = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    dw = models.CharField(max_length=50, blank=True, null=True)
    zy_fs = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    kcye = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    fysj = models.DateField(blank=True, null=True)
    fyr = models.CharField(max_length=30, blank=True, null=True)
    fyr_name = models.CharField(max_length=50, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    fyff = models.CharField(max_length=200, blank=True, null=True)
    jyff = models.CharField(max_length=200, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)
    bz4 = models.CharField(max_length=200, blank=True, null=True)
    bz5 = models.CharField(max_length=200, blank=True, null=True)
    lx = models.CharField(max_length=1, blank=True, null=True)
    zsl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sfmxid = models.CharField(max_length=30, blank=True, null=True)
    fydh = models.CharField(max_length=50, blank=True, null=True)
    ksdm = models.CharField(max_length=30, blank=True, null=True)
    device_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_zy_fy_list'


class OtherZyYyqkb(models.Model):
    cust_id = models.CharField(max_length=30, blank=True, null=True)
    xm = models.CharField(max_length=30, blank=True, null=True)
    xb = models.CharField(max_length=30, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    sfzhm = models.CharField(max_length=30, blank=True, null=True)
    member_code = models.CharField(max_length=30, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    zzys = models.CharField(max_length=30, blank=True, null=True)
    czy = models.CharField(max_length=30, blank=True, null=True)
    czy_name = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=60, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    lx = models.CharField(max_length=1, blank=True, null=True)
    bz = models.CharField(max_length=300, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_zy_yyqkb'


class OtherZyllList(models.Model):
    cust_id = models.CharField(max_length=30, blank=True, null=True)
    lx = models.CharField(max_length=30, blank=True, null=True)
    czlx = models.CharField(max_length=30, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    xb = models.CharField(max_length=50, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    member_code = models.CharField(max_length=30, blank=True, null=True)
    dm = models.CharField(max_length=30, blank=True, null=True)
    mc = models.CharField(max_length=200, blank=True, null=True)
    sl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    czy_name = models.CharField(max_length=30, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)
    sysl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    card_id = models.CharField(max_length=100, blank=True, null=True)
    bw = models.CharField(max_length=500, blank=True, null=True)
    bz4 = models.CharField(max_length=500, blank=True, null=True)
    bz5 = models.CharField(max_length=500, blank=True, null=True)
    bz6 = models.CharField(max_length=500, blank=True, null=True)
    id = models.CharField(max_length=60, blank=True, null=True)
    next_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_zyll_list'


class OtherZyllStock(models.Model):
    cust_id = models.CharField(max_length=30, blank=True, null=True)
    member_code = models.CharField(max_length=30, blank=True, null=True)
    lx = models.CharField(max_length=30, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    xb = models.CharField(max_length=50, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    dm = models.CharField(max_length=30, blank=True, null=True)
    sl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    slclsj = models.DateField(blank=True, null=True)
    scclsl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    dj = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    card_id = models.CharField(max_length=100, blank=True, null=True)
    bw = models.CharField(max_length=500, blank=True, null=True)
    bz4 = models.CharField(max_length=500, blank=True, null=True)
    bz5 = models.CharField(max_length=500, blank=True, null=True)
    bz6 = models.CharField(max_length=500, blank=True, null=True)
    next_date = models.DateField(blank=True, null=True)
    next_tls = models.CharField(max_length=30, blank=True, null=True)
    prior_date = models.DateField(blank=True, null=True)
    ys_tls = models.CharField(max_length=30, blank=True, null=True)
    ys_tlsname = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_zyll_stock'


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


class Pbcatedt(models.Model):
    pbe_name = models.CharField(max_length=30, blank=True, null=True)
    pbe_edit = models.CharField(max_length=254, blank=True, null=True)
    pbe_type = models.BigIntegerField(blank=True, null=True)
    pbe_cntr = models.BigIntegerField(blank=True, null=True)
    pbe_seqn = models.BigIntegerField(blank=True, null=True)
    pbe_flag = models.BigIntegerField(blank=True, null=True)
    pbe_work = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcatedt'


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


class Pbcatvld(models.Model):
    pbv_name = models.CharField(max_length=30, blank=True, null=True)
    pbv_vald = models.CharField(max_length=254, blank=True, null=True)
    pbv_type = models.BigIntegerField(blank=True, null=True)
    pbv_cntr = models.BigIntegerField(blank=True, null=True)
    pbv_msg = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcatvld'


class PlanTable(models.Model):
    statement_id = models.CharField(max_length=30, blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=80, blank=True, null=True)
    operation = models.CharField(max_length=30, blank=True, null=True)
    options = models.CharField(max_length=255, blank=True, null=True)
    object_node = models.CharField(max_length=128, blank=True, null=True)
    object_owner = models.CharField(max_length=30, blank=True, null=True)
    object_name = models.CharField(max_length=30, blank=True, null=True)
    object_instance = models.BigIntegerField(blank=True, null=True)
    object_type = models.CharField(max_length=30, blank=True, null=True)
    optimizer = models.CharField(max_length=255, blank=True, null=True)
    search_columns = models.FloatField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    parent_id = models.BigIntegerField(blank=True, null=True)
    position = models.BigIntegerField(blank=True, null=True)
    cost = models.BigIntegerField(blank=True, null=True)
    cardinality = models.BigIntegerField(blank=True, null=True)
    bytes = models.BigIntegerField(blank=True, null=True)
    other_tag = models.CharField(max_length=255, blank=True, null=True)
    partition_start = models.CharField(max_length=255, blank=True, null=True)
    partition_stop = models.CharField(max_length=255, blank=True, null=True)
    partition_id = models.BigIntegerField(blank=True, null=True)
    other = models.TextField(blank=True, null=True)  # This field type is a guess.
    distribution = models.CharField(max_length=30, blank=True, null=True)
    cpu_cost = models.BigIntegerField(blank=True, null=True)
    io_cost = models.BigIntegerField(blank=True, null=True)
    temp_space = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan_table'


class PwcTemp(models.Model):
    ygh = models.CharField(max_length=30, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pwc_temp'


class PzkCzLog(models.Model):
    billcode = models.CharField(max_length=80, blank=True, null=True)
    dwdm = models.CharField(max_length=30, blank=True, null=True)
    dwmc = models.CharField(max_length=200, blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    card_code = models.CharField(max_length=30, blank=True, null=True)
    lx = models.CharField(max_length=30, blank=True, null=True)
    czy = models.CharField(max_length=30, blank=True, null=True)
    czy_opername = models.CharField(max_length=30, blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    other_billcode = models.CharField(max_length=30, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    xb = models.CharField(max_length=10, blank=True, null=True)
    csrq = models.CharField(max_length=20, blank=True, null=True)
    groupid = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pzk_cz_log'


class PzkDjDetail(models.Model):
    billcode = models.CharField(max_length=30, blank=True, null=True)
    id = models.CharField(max_length=30, blank=True, null=True)
    begin_code = models.CharField(max_length=60, blank=True, null=True)
    end_code = models.CharField(max_length=60, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    groupid = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pzk_dj_detail'


class PzkDjIndex(models.Model):
    billcode = models.CharField(max_length=30, blank=True, null=True)
    dwdm = models.CharField(max_length=30, blank=True, null=True)
    dwmc = models.CharField(max_length=200, blank=True, null=True)
    lr_oper = models.CharField(max_length=20, blank=True, null=True)
    lr_opername = models.CharField(max_length=30, blank=True, null=True)
    sh_oper = models.CharField(max_length=30, blank=True, null=True)
    sh_opername = models.CharField(max_length=30, blank=True, null=True)
    cwsh_oper = models.CharField(max_length=30, blank=True, null=True)
    cwsh_opername = models.CharField(max_length=30, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    cwshsj = models.DateField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    bz = models.CharField(max_length=200, blank=True, null=True)
    lx = models.CharField(max_length=1, blank=True, null=True)
    zfr_oper = models.CharField(max_length=30, blank=True, null=True)
    zfr_opername = models.CharField(max_length=30, blank=True, null=True)
    zfsj = models.DateField(blank=True, null=True)
    fkfs = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pzk_dj_index'


class PzkStockList(models.Model):
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    card_code = models.CharField(max_length=30, blank=True, null=True)
    billcode = models.CharField(max_length=30, blank=True, null=True)
    dwdm = models.CharField(max_length=30, blank=True, null=True)
    dwmc = models.CharField(max_length=200, blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    other_in_factory = models.CharField(max_length=20, blank=True, null=True)
    groupid = models.CharField(max_length=30, blank=True, null=True)
    fkfs = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pzk_stock_list'


class QcMethod(models.Model):
    qc_method_id = models.IntegerField(blank=True, null=True)
    qc_method_name = models.CharField(max_length=20, blank=True, null=True)
    qc_method_code = models.CharField(max_length=10, blank=True, null=True)
    qc_procedure = models.TextField(blank=True, null=True)  # This field type is a guess.
    qc_application = models.TextField(blank=True, null=True)
    qc_method_character = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qc_method'


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


class ReportManyPrintSqLog(models.Model):
    id = models.CharField(max_length=200, blank=True, null=True)
    csr = models.CharField(max_length=200, blank=True, null=True)
    clsj = models.DateField(blank=True, null=True)
    wcr = models.CharField(max_length=200, blank=True, null=True)
    wcsj = models.DateField(blank=True, null=True)
    bz = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_many_print_sq_log'


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


class ReportTjXts(models.Model):
    dwyyid = models.CharField(max_length=30, blank=True, null=True)
    xts_dm = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_tj_xts'


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


class Reportimage(models.Model):
    tjh000 = models.CharField(max_length=20, blank=True, null=True)
    ctrq00 = models.CharField(max_length=20, blank=True, null=True)
    tpbt00 = models.CharField(max_length=20, blank=True, null=True)
    bdy000 = models.CharField(max_length=20, blank=True, null=True)
    jcbg00 = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reportimage'


class Reportresult(models.Model):
    tjh000 = models.CharField(max_length=20, blank=True, null=True)
    ydzws0 = models.CharField(max_length=20, blank=True, null=True)
    ydsfwc = models.CharField(max_length=20, blank=True, null=True)
    zszws0 = models.CharField(max_length=20, blank=True, null=True)
    zssfwc = models.CharField(max_length=20, blank=True, null=True)
    jccs00 = models.CharField(max_length=20, blank=True, null=True)
    cgcs00 = models.CharField(max_length=20, blank=True, null=True)
    cgl000 = models.CharField(max_length=20, blank=True, null=True)
    scrq00 = models.CharField(max_length=20, blank=True, null=True)
    scsj00 = models.CharField(max_length=20, blank=True, null=True)
    qt001 = models.CharField(max_length=20, blank=True, null=True)
    qt002 = models.CharField(max_length=20, blank=True, null=True)
    qt003 = models.CharField(max_length=20, blank=True, null=True)
    bz0000 = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reportresult'


class RmCardGroupDj(models.Model):
    card_code = models.CharField(max_length=100, blank=True, null=True)
    czy = models.CharField(max_length=100, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    bz1 = models.CharField(max_length=50, blank=True, null=True)
    bz2 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rm_card_group_dj'


class RmCardcodeZx(models.Model):
    billcode = models.CharField(max_length=150, blank=True, null=True)
    card_code = models.CharField(max_length=100, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    czry = models.CharField(max_length=100, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rm_cardcode_zx'


class RmItemList2018(models.Model):
    item_id_rm = models.CharField(max_length=60, blank=True, null=True)
    item_name = models.CharField(max_length=200, blank=True, null=True)
    item_id_mn = models.CharField(max_length=60, blank=True, null=True)
    bz1 = models.CharField(max_length=60, blank=True, null=True)
    bz2 = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rm_item_list2018'


class SaleBctjqkList(models.Model):
    cid = models.CharField(max_length=20, blank=True, null=True)
    vid = models.CharField(max_length=20, blank=True, null=True)
    xm = models.CharField(max_length=30, blank=True, null=True)
    xb = models.CharField(max_length=10, blank=True, null=True)
    dwdm = models.CharField(max_length=20, blank=True, null=True)
    dwmc = models.CharField(max_length=100, blank=True, null=True)
    tdyq_dm = models.CharField(max_length=100, blank=True, null=True)
    tdyq_mc = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    read_oper = models.CharField(max_length=10, blank=True, null=True)
    auditoper = models.CharField(max_length=10, blank=True, null=True)
    read_time = models.DateField(blank=True, null=True)
    audit_time = models.DateField(blank=True, null=True)
    create_oper = models.CharField(max_length=10, blank=True, null=True)
    create_time = models.DateField(blank=True, null=True)
    in_factory = models.CharField(max_length=60, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    tj_in_factory = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_bctjqk_list'


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


class SaleEhoList(models.Model):
    dwdm = models.CharField(max_length=30, blank=True, null=True)
    ygh = models.CharField(max_length=30, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    xb = models.CharField(max_length=10, blank=True, null=True)
    hyzk = models.CharField(max_length=10, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    sfzhm = models.CharField(max_length=30, blank=True, null=True)
    fgs = models.CharField(max_length=100, blank=True, null=True)
    bm1 = models.CharField(max_length=100, blank=True, null=True)
    bm2 = models.CharField(max_length=100, blank=True, null=True)
    lxdh = models.CharField(max_length=60, blank=True, null=True)
    yyrq = models.DateField(blank=True, null=True)
    groupid = models.CharField(max_length=30, blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    add_item = models.CharField(max_length=1000, blank=True, null=True)
    bz = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    lxdz = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_eho_list'


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


class SaleGroupSsh2019(models.Model):
    billcode = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=30, blank=True, null=True)
    dwdm = models.CharField(max_length=50, blank=True, null=True)
    dwmc = models.CharField(max_length=350, blank=True, null=True)
    groupid = models.CharField(max_length=60, blank=True, null=True)
    groupname = models.CharField(max_length=100, blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    oldprice = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    sqr_oper = models.CharField(max_length=50, blank=True, null=True)
    sqr_opername = models.CharField(max_length=100, blank=True, null=True)
    sqsj = models.DateField(blank=True, null=True)
    shr_oper = models.CharField(max_length=50, blank=True, null=True)
    shr_opername = models.CharField(max_length=100, blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    lb = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_group_ssh2019'


class SaleQgddFw(models.Model):
    id = models.CharField(max_length=200, blank=True, null=True)
    billcode = models.CharField(max_length=200, blank=True, null=True)
    in_factory = models.CharField(max_length=100, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_qgdd_fw'


class SaleQgddGroup(models.Model):
    id = models.CharField(max_length=200, blank=True, null=True)
    billcode = models.CharField(max_length=100, blank=True, null=True)
    dwdm = models.CharField(max_length=100, blank=True, null=True)
    lb = models.CharField(max_length=10, blank=True, null=True)
    in_factory = models.CharField(max_length=100, blank=True, null=True)
    groupid = models.CharField(max_length=100, blank=True, null=True)
    r_groupid = models.CharField(max_length=100, blank=True, null=True)
    member_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    trans_status = models.CharField(max_length=10, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    audit_opername = models.CharField(max_length=100, blank=True, null=True)
    item_id = models.CharField(max_length=30, blank=True, null=True)
    r_item_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_qgdd_group'


class SaleShYy(models.Model):
    cust_name = models.CharField(max_length=30, blank=True, null=True)
    company = models.CharField(max_length=60, blank=True, null=True)
    yysj = models.DateField(blank=True, null=True)
    cust_sex = models.CharField(max_length=2, blank=True, null=True)
    bz = models.CharField(max_length=200, blank=True, null=True)
    djr = models.CharField(max_length=50, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    dwdm = models.CharField(max_length=30, blank=True, null=True)
    id = models.CharField(max_length=50, blank=True, null=True)
    groupid = models.CharField(max_length=50, blank=True, null=True)
    csrq = models.DateField(blank=True, null=True)
    fkfs = models.CharField(max_length=1, blank=True, null=True)
    jsf = models.CharField(max_length=1, blank=True, null=True)
    ygh = models.CharField(max_length=30, blank=True, null=True)
    fgs = models.CharField(max_length=100, blank=True, null=True)
    bz1 = models.CharField(max_length=50, blank=True, null=True)
    bz2 = models.CharField(max_length=50, blank=True, null=True)
    bz3 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_sh_yy'


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


class SaleTjdwFkfsChange(models.Model):
    billcode = models.CharField(max_length=30, blank=True, null=True)
    dwdm = models.CharField(max_length=30, blank=True, null=True)
    dwmc = models.CharField(max_length=100, blank=True, null=True)
    kssj = models.DateField(blank=True, null=True)
    fkfs = models.CharField(max_length=10, blank=True, null=True)
    lrry = models.CharField(max_length=20, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    zfry = models.CharField(max_length=10, blank=True, null=True)
    zfsj = models.DateField(blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    bz1 = models.CharField(max_length=30, blank=True, null=True)
    bz2 = models.CharField(max_length=30, blank=True, null=True)
    bz3 = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_tjdw_fkfs_change'


class SaleTjdwList(models.Model):
    billcode = models.CharField(max_length=12, blank=True, null=True)
    dwdm = models.CharField(max_length=12, blank=True, null=True)
    dwmc = models.CharField(max_length=60, blank=True, null=True)
    ywydm = models.CharField(max_length=6, blank=True, null=True)
    lxr = models.CharField(max_length=30, blank=True, null=True)
    lxdh = models.CharField(max_length=50, blank=True, null=True)
    lxdz = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    djsj = models.DateField(blank=True, null=True)
    jgxx = models.CharField(max_length=3000, blank=True, null=True)
    sfjzsj = models.DateField(blank=True, null=True)
    xsyq = models.CharField(max_length=3000, blank=True, null=True)
    ywy_zg = models.CharField(max_length=60, blank=True, null=True)
    ywy_zg_shsj = models.DateField(blank=True, null=True)
    zrhs = models.CharField(max_length=6, blank=True, null=True)
    zrys = models.CharField(max_length=6, blank=True, null=True)
    ywb_zg_shsj = models.DateField(blank=True, null=True)
    zxfw = models.CharField(max_length=1, blank=True, null=True)
    yj = models.CharField(max_length=1, blank=True, null=True)
    lcctf = models.CharField(max_length=1, blank=True, null=True)
    tdhf = models.CharField(max_length=1, blank=True, null=True)
    xsbyj = models.CharField(max_length=3000, blank=True, null=True)
    xsbdjr = models.CharField(max_length=6, blank=True, null=True)
    xsbdjsj = models.DateField(blank=True, null=True)
    lcksyj = models.CharField(max_length=200, blank=True, null=True)
    lcdjr = models.CharField(max_length=6, blank=True, null=True)
    lcdjsj = models.DateField(blank=True, null=True)
    wctjsj = models.DateField(blank=True, null=True)
    wctjrs = models.IntegerField(blank=True, null=True)
    wcbgrs = models.IntegerField(blank=True, null=True)
    zxwcsj = models.DateField(blank=True, null=True)
    jzwcsj = models.DateField(blank=True, null=True)
    zj_zrr = models.CharField(max_length=6, blank=True, null=True)
    zj_qzsj = models.DateField(blank=True, null=True)
    zj_bz = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    status1 = models.CharField(max_length=1, blank=True, null=True)
    status2 = models.CharField(max_length=1, blank=True, null=True)
    status3 = models.CharField(max_length=1, blank=True, null=True)
    status4 = models.CharField(max_length=1, blank=True, null=True)
    status5 = models.CharField(max_length=1, blank=True, null=True)
    ywb_zg = models.CharField(max_length=6, blank=True, null=True)
    zlpg_shry = models.CharField(max_length=6, blank=True, null=True)
    zlpg_shsj = models.DateField(blank=True, null=True)
    zjbz_zrr = models.CharField(max_length=6, blank=True, null=True)
    zjbz_qzsj = models.DateField(blank=True, null=True)
    htsj = models.DateField(blank=True, null=True)
    qbgdfs = models.CharField(max_length=10, blank=True, null=True)
    fkfs = models.CharField(max_length=1, blank=True, null=True)
    read_ornot = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_tjdw_list'


class SaleTjdwTbtx(models.Model):
    dwdm = models.CharField(max_length=30, blank=True, null=True)
    billcode = models.CharField(max_length=60, blank=True, null=True)
    userobject = models.CharField(max_length=100, blank=True, null=True)
    id = models.CharField(max_length=100, blank=True, null=True)
    kssj = models.DateField(blank=True, null=True)
    jzsj = models.DateField(blank=True, null=True)
    nr = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_tjdw_tbtx'


class SaleTjdwTdyq(models.Model):
    billcode = models.CharField(max_length=12, blank=True, null=True)
    tdyq_dm = models.CharField(max_length=20, blank=True, null=True)
    yqkssj = models.DateField(blank=True, null=True)
    yqjzsj = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    shr = models.CharField(max_length=6, blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    bz = models.CharField(max_length=200, blank=True, null=True)
    cqyxf = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    dwdm = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_tjdw_tdyq'


class SaleYypqInput(models.Model):
    bill_code = models.CharField(max_length=12, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    yyrq = models.DateField(blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    pqzh = models.CharField(max_length=20, blank=True, null=True)
    dwdm = models.CharField(max_length=12, blank=True, null=True)
    dwmc = models.CharField(max_length=60, blank=True, null=True)
    pqrs = models.BigIntegerField(blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    isselect = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_yypq_input'


class SmallPictureList(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    s_item_id = models.CharField(max_length=20, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    czy = models.CharField(max_length=100, blank=True, null=True)
    czyname = models.CharField(max_length=100, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'small_picture_list'


class SmpVborBackupConfiguration(models.Model):
    configname = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    userc = models.CharField(max_length=32, blank=True, null=True)
    rcusername = models.CharField(max_length=128, blank=True, null=True)
    rcpassword = models.TextField(blank=True, null=True)  # This field type is a guess.
    rcservicename = models.CharField(max_length=128, blank=True, null=True)
    overrideprefcred = models.CharField(max_length=32, blank=True, null=True)
    prefusername = models.CharField(max_length=128, blank=True, null=True)
    prefpassword = models.TextField(blank=True, null=True)  # This field type is a guess.
    overridermandef = models.CharField(max_length=128, blank=True, null=True)
    usefilesbackupset = models.CharField(max_length=32, blank=True, null=True)
    filesbackupset = models.FloatField(blank=True, null=True)
    usesizebackupset = models.CharField(max_length=32, blank=True, null=True)
    usesizebackupsetal = models.CharField(max_length=32, blank=True, null=True)
    sizebackupset = models.FloatField(blank=True, null=True)
    sizeal = models.FloatField(blank=True, null=True)
    copinitora = models.CharField(max_length=32, blank=True, null=True)
    copyfromdef = models.CharField(max_length=32, blank=True, null=True)
    copyfromlocation = models.CharField(max_length=128, blank=True, null=True)
    copydestination = models.CharField(max_length=128, blank=True, null=True)
    oemuser = models.CharField(max_length=128, blank=True, null=True)
    permission = models.CharField(max_length=128, blank=True, null=True)
    usefilesbackupsetal = models.CharField(max_length=32, blank=True, null=True)
    filesbackupsetal = models.FloatField(blank=True, null=True)
    isappliancedatabase = models.CharField(max_length=32, blank=True, null=True)
    nsrserver = models.CharField(max_length=128, blank=True, null=True)
    proxyusage = models.CharField(max_length=8, blank=True, null=True)
    usenewrc = models.CharField(max_length=4, blank=True, null=True)
    newrctriplet = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vbor_backup_configuration'


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


class SmpVdeEvent(models.Model):
    id = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    owner = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    target_type = models.CharField(max_length=64, blank=True, null=True)
    schedule = models.CharField(max_length=512, blank=True, null=True)
    app_name = models.CharField(max_length=64, blank=True, null=True)
    is_library = models.CharField(max_length=1, blank=True, null=True)
    fixit_job_id = models.FloatField(blank=True, null=True)
    fixit_job_name = models.CharField(max_length=64, blank=True, null=True)
    fixit_job_owner = models.CharField(max_length=32, blank=True, null=True)
    is_unsolicited = models.CharField(max_length=1, blank=True, null=True)
    incomplete = models.FloatField(blank=True, null=True)
    snmp_trap_attribute = models.CharField(max_length=1, blank=True, null=True)
    last_modified = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vde_event'


class SmpVdeEventArchive(models.Model):
    owner = models.CharField(max_length=32, blank=True, null=True)
    event_id = models.FloatField(blank=True, null=True)
    event_test_id = models.FloatField(blank=True, null=True)
    event_occurrence_id = models.BigIntegerField(blank=True, null=True)
    target_name = models.CharField(max_length=128, blank=True, null=True)
    target_type = models.CharField(max_length=128, blank=True, null=True)
    node = models.CharField(max_length=128, blank=True, null=True)
    occur_date = models.DateField(blank=True, null=True)
    local_date = models.DateField(blank=True, null=True)
    timezone = models.FloatField(blank=True, null=True)
    severity = models.IntegerField(blank=True, null=True)
    registration_status = models.IntegerField(blank=True, null=True)
    target_agent_state = models.IntegerField(blank=True, null=True)
    record_type = models.IntegerField(blank=True, null=True)
    test_name = models.CharField(max_length=128, blank=True, null=True)
    company = models.CharField(max_length=128, blank=True, null=True)
    organization = models.CharField(max_length=128, blank=True, null=True)
    product = models.CharField(max_length=128, blank=True, null=True)
    filename = models.CharField(max_length=128, blank=True, null=True)
    msg_output = models.CharField(max_length=4000, blank=True, null=True)
    annotation = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vde_event_archive'


class SmpVdeEventArchivePurge(models.Model):
    trigger_purge_interval = models.IntegerField(blank=True, null=True)
    keep_days = models.IntegerField(blank=True, null=True)
    keep_rows = models.IntegerField(blank=True, null=True)
    archive_row_count = models.FloatField(blank=True, null=True)
    time_measure = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vde_event_archive_purge'


class SmpVdeEventDetails(models.Model):
    event_id = models.FloatField(blank=True, null=True)
    test_id = models.FloatField(blank=True, null=True)
    company = models.CharField(max_length=128, blank=True, null=True)
    organization = models.CharField(max_length=128, blank=True, null=True)
    product = models.CharField(max_length=128, blank=True, null=True)
    filename = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vde_event_details'


class SmpVdeEventLockTab(models.Model):
    c1 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vde_event_lock_tab'


class SmpVdeEventLog(models.Model):
    event_occurrence_id = models.BigIntegerField(blank=True, null=True)
    entry = models.CharField(max_length=4000, blank=True, null=True)
    author = models.CharField(max_length=256, blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    timezone = models.FloatField(blank=True, null=True)
    severity = models.FloatField(blank=True, null=True)
    event_test_id = models.FloatField(blank=True, null=True)
    event_test_severity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vde_event_log'


class SmpVdeEventOccurDetails(models.Model):
    event_occurrence_id = models.BigIntegerField(blank=True, null=True)
    company = models.CharField(max_length=128, blank=True, null=True)
    organization = models.CharField(max_length=128, blank=True, null=True)
    product = models.CharField(max_length=128, blank=True, null=True)
    filename = models.CharField(max_length=128, blank=True, null=True)
    test_name = models.CharField(max_length=128, blank=True, null=True)
    severity = models.FloatField(blank=True, null=True)
    occur_date = models.DateField(blank=True, null=True)
    timezone = models.FloatField(blank=True, null=True)
    event_test_id = models.FloatField(blank=True, null=True)
    message = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vde_event_occur_details'


class SmpVdeEventOccurrence(models.Model):
    event_occurrence_id = models.BigIntegerField(blank=True, null=True)
    event_id = models.FloatField(blank=True, null=True)
    target_name = models.CharField(max_length=128, blank=True, null=True)
    target_type = models.CharField(max_length=128, blank=True, null=True)
    node_name = models.CharField(max_length=128, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    occur_date = models.DateField(blank=True, null=True)
    timezone = models.FloatField(blank=True, null=True)
    severity = models.BigIntegerField(blank=True, null=True)
    assignee = models.CharField(max_length=256, blank=True, null=True)
    markedfordelete = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'smp_vde_event_occurrence'


class SmpVdeEventTargetAck(models.Model):
    event_id = models.FloatField(blank=True, null=True)
    target_name = models.CharField(max_length=128, blank=True, null=True)
    target_type = models.CharField(max_length=128, blank=True, null=True)
    node_name = models.CharField(max_length=128, blank=True, null=True)
    userid = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vde_event_target_ack'


class SmpVdeEventTargetDetails(models.Model):
    event_id = models.FloatField(blank=True, null=True)
    event_test_id = models.FloatField(blank=True, null=True)
    target_name = models.CharField(max_length=128, blank=True, null=True)
    target_type = models.CharField(max_length=128, blank=True, null=True)
    node_name = models.CharField(max_length=128, blank=True, null=True)
    company = models.CharField(max_length=128, blank=True, null=True)
    organization = models.CharField(max_length=128, blank=True, null=True)
    product = models.CharField(max_length=128, blank=True, null=True)
    filename = models.CharField(max_length=128, blank=True, null=True)
    test_name = models.CharField(max_length=128, blank=True, null=True)
    severity = models.FloatField(blank=True, null=True)
    occur_date = models.DateField(blank=True, null=True)
    timezone = models.FloatField(blank=True, null=True)
    operation = models.FloatField(blank=True, null=True)
    message = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vde_event_target_details'


class SmpVdeEventTargetInfo(models.Model):
    event_id = models.FloatField(blank=True, null=True)
    target_name = models.CharField(max_length=128, blank=True, null=True)
    target_type = models.CharField(max_length=128, blank=True, null=True)
    node_name = models.CharField(max_length=128, blank=True, null=True)
    agent_status = models.FloatField(blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    timezone = models.FloatField(blank=True, null=True)
    error_code = models.FloatField(blank=True, null=True)
    error_message = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vde_event_target_info'


class SmpVdeEventTargetState(models.Model):
    event_id = models.FloatField(blank=True, null=True)
    target_name = models.CharField(max_length=128, blank=True, null=True)
    target_type = models.CharField(max_length=128, blank=True, null=True)
    node_name = models.CharField(max_length=128, blank=True, null=True)
    agent_severity = models.FloatField(blank=True, null=True)
    node_state = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vde_event_target_state'


class SmpVdeEventUpdownQueue(models.Model):
    sequence_num = models.BigIntegerField(blank=True, null=True)
    event_id = models.BigIntegerField(blank=True, null=True)
    target_name = models.CharField(max_length=128, blank=True, null=True)
    target_type = models.CharField(max_length=128, blank=True, null=True)
    updown = models.CharField(max_length=1, blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    timezone = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vde_event_updown_queue'


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


class SmpVdeNodeUpdownQueue(models.Model):
    sequence_num = models.BigIntegerField(blank=True, null=True)
    node = models.CharField(max_length=128, blank=True, null=True)
    updown = models.CharField(max_length=1, blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    timezone = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vde_node_updown_queue'


class SmpVdeThresholdAssoc(models.Model):
    id = models.FloatField(blank=True, null=True)
    principal_id = models.FloatField(blank=True, null=True)
    state = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vde_threshold_assoc'


class SmpVdeTryRemoveEventQueue(models.Model):
    sequence_num = models.BigIntegerField(blank=True, null=True)
    event_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vde_try_remove_event_queue'


class SmpVdfMaslist(models.Model):
    mas_name = models.CharField(max_length=128, blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdf_maslist'


class SmpVdgEventDeleteList(models.Model):
    masid = models.BigIntegerField(blank=True, null=True)
    agentid = models.BigIntegerField(blank=True, null=True)
    targetname = models.CharField(max_length=256, blank=True, null=True)
    targettype = models.CharField(max_length=128, blank=True, null=True)
    eventname = models.CharField(max_length=256, blank=True, null=True)
    nodename = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdg_event_delete_list'


class SmpVdgEventNotifList(models.Model):
    masid = models.BigIntegerField(blank=True, null=True)
    eventname = models.CharField(max_length=256, blank=True, null=True)
    targetname = models.CharField(max_length=256, blank=True, null=True)
    targettype = models.CharField(max_length=128, blank=True, null=True)
    nodename = models.CharField(max_length=128, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    maxstatus = models.BigIntegerField(blank=True, null=True)
    hold = models.BigIntegerField(blank=True, null=True)
    agentid = models.BigIntegerField(blank=True, null=True)
    event_index = models.BigIntegerField(blank=True, null=True)
    eventargs = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdg_event_notif_list'


class SmpVdgEventidMap(models.Model):
    nodename = models.CharField(max_length=128, blank=True, null=True)
    targetname = models.CharField(max_length=256, blank=True, null=True)
    targettype = models.CharField(max_length=128, blank=True, null=True)
    masid = models.BigIntegerField(blank=True, null=True)
    agentid = models.BigIntegerField(blank=True, null=True)
    eventname = models.CharField(max_length=256, blank=True, null=True)
    agenteventname = models.CharField(max_length=256, blank=True, null=True)
    eventargs = models.CharField(max_length=2000, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    oldstatus = models.BigIntegerField(blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    frequency = models.BigIntegerField(blank=True, null=True)
    reg_complete = models.BigIntegerField(blank=True, null=True)
    event_index = models.BigIntegerField(blank=True, null=True)
    unsolfilter = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdg_eventid_map'


class SmpVdgGatewayMap(models.Model):
    nodename = models.CharField(max_length=128, blank=True, null=True)
    hostname = models.CharField(max_length=256, blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    up_down = models.CharField(max_length=4, blank=True, null=True)
    up_index = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdg_gateway_map'


class SmpVdgJobidMap(models.Model):
    nodename = models.CharField(max_length=128, blank=True, null=True)
    targetname = models.CharField(max_length=256, blank=True, null=True)
    targettype = models.CharField(max_length=128, blank=True, null=True)
    masid = models.BigIntegerField(blank=True, null=True)
    agentid = models.BigIntegerField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    schedule_ts = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdg_jobid_map'


class SmpVdgNodeList(models.Model):
    nodename = models.CharField(max_length=128, blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    gatewayname = models.CharField(max_length=40, blank=True, null=True)
    status = models.CharField(max_length=4, blank=True, null=True)
    processing = models.CharField(max_length=40, blank=True, null=True)
    node_index = models.FloatField(blank=True, null=True)
    agentname = models.CharField(max_length=128, blank=True, null=True)
    agenttz = models.BigIntegerField(blank=True, null=True)
    agentstate = models.CharField(max_length=4, blank=True, null=True)
    agentversion = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdg_node_list'


class SmpVdgNodeLockTable(models.Model):
    nodename = models.CharField(max_length=128, blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    gatewayname = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdg_node_lock_table'


class SmpVdiAobjectNotification(models.Model):
    username = models.CharField(max_length=128, blank=True, null=True)
    object_id = models.FloatField(blank=True, null=True)
    notify = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdi_aobject_notification'


class SmpVdiObjectTable(models.Model):
    object_id = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=128, blank=True, null=True)
    owner = models.CharField(max_length=128, blank=True, null=True)
    object_name = models.CharField(max_length=128, blank=True, null=True)
    version = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdi_object_table'


class SmpVdiPos(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    taskid = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=256, blank=True, null=True)
    data = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'smp_vdi_pos'


class SmpVdiTargetProperties(models.Model):
    object_id = models.FloatField(blank=True, null=True)
    object_type = models.CharField(max_length=256, blank=True, null=True)
    property_name = models.CharField(max_length=256, blank=True, null=True)
    property_value = models.CharField(max_length=2000, blank=True, null=True)
    property_type = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'smp_vdi_target_properties'


class SmpVdjJob(models.Model):
    job_id = models.FloatField(blank=True, null=True)
    job_name = models.CharField(max_length=64, blank=True, null=True)
    owner = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    app_name = models.CharField(max_length=64, blank=True, null=True)
    target_type = models.CharField(max_length=64, blank=True, null=True)
    schedule = models.CharField(max_length=512, blank=True, null=True)
    submit_time = models.DateField(blank=True, null=True)
    is_fixit = models.CharField(max_length=1, blank=True, null=True)
    is_lib = models.CharField(max_length=1, blank=True, null=True)
    last_mod_by = models.CharField(max_length=32, blank=True, null=True)
    last_mod_time = models.DateField(blank=True, null=True)
    time_zone = models.FloatField(blank=True, null=True)
    number_tasks = models.FloatField(blank=True, null=True)
    incomplete = models.FloatField(blank=True, null=True)
    overriding_node_creds = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'smp_vdj_job'


class SmpVdjJobLock(models.Model):
    c1 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdj_job_lock'


class SmpVdjJobLog(models.Model):
    job_id = models.FloatField(blank=True, null=True)
    target_name = models.CharField(max_length=128, blank=True, null=True)
    exec_num = models.FloatField(blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    time_zone = models.FloatField(blank=True, null=True)
    output_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdj_job_log'


class SmpVdjJobLogComment(models.Model):
    job_id = models.FloatField(blank=True, null=True)
    target_name = models.CharField(max_length=128, blank=True, null=True)
    exec_num = models.FloatField(blank=True, null=True)
    author = models.CharField(max_length=64, blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    comment_text = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdj_job_log_comment'


class SmpVdjJobLogIntermed(models.Model):
    job_id = models.FloatField(blank=True, null=True)
    target_name = models.CharField(max_length=128, blank=True, null=True)
    exec_num = models.FloatField(blank=True, null=True)
    intermed_index = models.FloatField(blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    output = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdj_job_log_intermed'


class SmpVdjJobOutput(models.Model):
    blob_id = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'smp_vdj_job_output'


class SmpVdjJobPerTarget(models.Model):
    job_id = models.FloatField(blank=True, null=True)
    target_name = models.CharField(max_length=128, blank=True, null=True)
    job_name = models.CharField(max_length=64, blank=True, null=True)
    target_type = models.CharField(max_length=64, blank=True, null=True)
    node_name = models.CharField(max_length=128, blank=True, null=True)
    deliver_time = models.DateField(blank=True, null=True)
    exec_num = models.FloatField(blank=True, null=True)
    start_time = models.DateField(blank=True, null=True)
    finish_time = models.DateField(blank=True, null=True)
    next_exec_time = models.DateField(blank=True, null=True)
    occur_time = models.DateField(blank=True, null=True)
    time_zone = models.FloatField(blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    parameters = models.CharField(max_length=1024, blank=True, null=True)
    login_username = models.CharField(max_length=32, blank=True, null=True)
    login_password = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdj_job_per_target'


class SmpVdjJobTarget(models.Model):
    job_id = models.FloatField(blank=True, null=True)
    target_name = models.CharField(max_length=128, blank=True, null=True)
    target_type = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdj_job_target'


class SmpVdmAddress(models.Model):
    sequence_num = models.FloatField(blank=True, null=True)
    username = models.CharField(max_length=256, blank=True, null=True)
    app_name = models.CharField(max_length=256, blank=True, null=True)
    enhanced_notification = models.BigIntegerField(blank=True, null=True)
    proxy = models.CharField(max_length=256, blank=True, null=True)
    slotretrievaltime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdm_address'


class SmpVdmGlobalInfo(models.Model):
    service_type = models.CharField(max_length=128, blank=True, null=True)
    service_name = models.CharField(max_length=128, blank=True, null=True)
    property_name = models.CharField(max_length=128, blank=True, null=True)
    property_value = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdm_global_info'


class SmpVdmLastNotifSeqPertype(models.Model):
    notification_type = models.FloatField(blank=True, null=True)
    last_notif_sequence = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdm_last_notif_seq_pertype'


class SmpVdmNotification(models.Model):
    sequence_num = models.BigIntegerField(blank=True, null=True)
    notification_id = models.BigIntegerField(blank=True, null=True)
    notification_type = models.BigIntegerField(blank=True, null=True)
    subtype = models.BigIntegerField(blank=True, null=True)
    node_name = models.CharField(max_length=256, blank=True, null=True)
    service_name = models.CharField(max_length=256, blank=True, null=True)
    service_type = models.CharField(max_length=256, blank=True, null=True)
    time_stamp = models.BigIntegerField(blank=True, null=True)
    time_zone = models.BigIntegerField(blank=True, null=True)
    verbose = models.BigIntegerField(blank=True, null=True)
    domain = models.CharField(max_length=256, blank=True, null=True)
    num_clients = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdm_notification'


class SmpVdmNotificationDetails(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    type = models.BigIntegerField(blank=True, null=True)
    target = models.CharField(max_length=256, blank=True, null=True)
    execnum = models.BigIntegerField(blank=True, null=True)
    owner = models.CharField(max_length=256, blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    time_zone = models.BigIntegerField(blank=True, null=True)
    method = models.CharField(max_length=256, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    message = models.CharField(max_length=2000, blank=True, null=True)
    operation_status = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdm_notification_details'


class SmpVdmNotificationNvpairs(models.Model):
    sequence_num = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    value_length = models.FloatField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'smp_vdm_notification_nvpairs'


class SmpVdmNotificationServices(models.Model):
    service_type = models.CharField(max_length=255, blank=True, null=True)
    nodename = models.CharField(max_length=255, blank=True, null=True)
    ior = models.CharField(max_length=2000, blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdm_notification_services'


class SmpVdmPagingCarrierInfo(models.Model):
    paging_server_name = models.CharField(max_length=255, blank=True, null=True)
    paging_carrier_id = models.FloatField(blank=True, null=True)
    paging_carrier_name = models.CharField(max_length=128, blank=True, null=True)
    paging_carrier_type = models.FloatField(blank=True, null=True)
    paging_carrier_timeout = models.IntegerField(blank=True, null=True)
    paging_carrier_conn_delay = models.IntegerField(blank=True, null=True)
    paging_carrier_protocol = models.CharField(max_length=128, blank=True, null=True)
    phone_country_code = models.IntegerField(blank=True, null=True)
    phone_area_code = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=128, blank=True, null=True)
    phone_number_suffix = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdm_paging_carrier_info'


class SmpVdmSessionNotiftypePair(models.Model):
    session_id = models.FloatField(blank=True, null=True)
    notification_type = models.FloatField(blank=True, null=True)
    last_notif_sequence = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdm_session_notiftype_pair'


class SmpVdnBlackoutschedule(models.Model):
    targetid = models.FloatField(blank=True, null=True)
    schedulename = models.CharField(max_length=64, blank=True, null=True)
    schedulestate = models.FloatField(blank=True, null=True)
    schedule = models.CharField(max_length=512, blank=True, null=True)
    start_time = models.CharField(max_length=128, blank=True, null=True)
    end_time = models.CharField(max_length=128, blank=True, null=True)
    duration_length = models.FloatField(blank=True, null=True)
    units = models.FloatField(blank=True, null=True)
    duration_mode = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdn_blackoutschedule'


class SmpVdnGroupGroup(models.Model):
    groupid = models.FloatField(blank=True, null=True)
    membergroupid = models.FloatField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdn_group_group'


class SmpVdnGroupList(models.Model):
    id = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    owner = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    backgroundfileurl = models.CharField(max_length=512, blank=True, null=True)
    iconsize = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdn_group_list'


class SmpVdnGroupTarget(models.Model):
    groupid = models.FloatField(blank=True, null=True)
    targetid = models.FloatField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdn_group_target'


class SmpVdnNodeList(models.Model):
    id = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    agent = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdn_node_list'


class SmpVdnNotify(models.Model):
    appname = models.CharField(max_length=128, blank=True, null=True)
    username = models.CharField(max_length=128, blank=True, null=True)
    type = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdn_notify'


class SmpVdnState(models.Model):
    target_name = models.CharField(max_length=128, blank=True, null=True)
    target_type = models.CharField(max_length=128, blank=True, null=True)
    node = models.CharField(max_length=128, blank=True, null=True)
    num_events = models.FloatField(blank=True, null=True)
    state = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdn_state'


class SmpVdnTargetList(models.Model):
    id = models.FloatField(blank=True, null=True)
    typeid = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    nodeid = models.FloatField(blank=True, null=True)
    tnsaddr = models.CharField(max_length=4000, blank=True, null=True)
    userdata = models.CharField(max_length=4000, blank=True, null=True)
    withagent = models.FloatField(blank=True, null=True)
    totalblackout = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdn_target_list'


class SmpVdnTargetProperties(models.Model):
    targetid = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    value = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdn_target_properties'


class SmpVdnTargetTypeDefn(models.Model):
    id = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    category = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdn_target_type_defn'


class SmpVdpNodeInfo(models.Model):
    node = models.CharField(max_length=256, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    down_time = models.DateField(blank=True, null=True)
    down_timezone = models.FloatField(blank=True, null=True)
    last_checked = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdp_node_info'


class SmpVdpNodeInfoVdd(models.Model):
    node = models.CharField(max_length=256, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdp_node_info_vdd'


class SmpVdpNodeOmsMap(models.Model):
    node = models.CharField(max_length=256, blank=True, null=True)
    oms = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdp_node_oms_map'


class SmpVdpNodes(models.Model):
    node = models.CharField(max_length=256, blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    region_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdp_nodes'


class SmpVdpOmsNumNodes(models.Model):
    oms = models.CharField(max_length=128, blank=True, null=True)
    num_nodes = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdp_oms_num_nodes'


class SmpVdpOmsRegionMap(models.Model):
    oms = models.CharField(max_length=128, blank=True, null=True)
    region_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdp_oms_region_map'


class SmpVdpPgsrvRegionMap(models.Model):
    paging_server = models.CharField(max_length=255, blank=True, null=True)
    region_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdp_pgsrv_region_map'


class SmpVdpRegions(models.Model):
    region_id = models.BigIntegerField(blank=True, null=True)
    region_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdp_regions'


class SmpVdrRegistry(models.Model):
    id = models.FloatField(blank=True, null=True)
    key = models.CharField(max_length=512, blank=True, null=True)
    parent = models.FloatField(blank=True, null=True)
    value = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdr_registry'


class SmpVdsReposVersion(models.Model):
    app_name = models.CharField(max_length=512, blank=True, null=True)
    version = models.FloatField(blank=True, null=True)
    upd_in_progress = models.FloatField(blank=True, null=True)
    standalone = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vds_repos_version'


class SmpVdsSessionsTable(models.Model):
    session_id = models.FloatField(blank=True, null=True)
    principal_name = models.CharField(max_length=128, blank=True, null=True)
    principal_type = models.CharField(max_length=128, blank=True, null=True)
    principal_ior = models.CharField(max_length=2000, blank=True, null=True)
    login_time = models.DateField(blank=True, null=True)
    oms = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vds_sessions_table'


class SmpVduCallbackTable(models.Model):
    mas_manager = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdu_callback_table'


class SmpVduObjectsTable(models.Model):
    object_id = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=128, blank=True, null=True)
    owner = models.CharField(max_length=128, blank=True, null=True)
    object_name = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdu_objects_table'


class SmpVduPrincipalsTable(models.Model):
    principal_id = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=128, blank=True, null=True)
    principal_name = models.CharField(max_length=128, blank=True, null=True)
    password = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'smp_vdu_principals_table'


class SmpVduPrivilegeTable(models.Model):
    principal_oid = models.FloatField(blank=True, null=True)
    privilege_string = models.CharField(max_length=128, blank=True, null=True)
    object_oid = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdu_privilege_table'


class SmpVdvDefaultNotifyPrefs(models.Model):
    user_id = models.FloatField(blank=True, null=True)
    other_user_id = models.FloatField(blank=True, null=True)
    notify = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdv_default_notify_prefs'


class SmpVdvDefaultPermissions(models.Model):
    user_id = models.FloatField(blank=True, null=True)
    other_user_id = models.FloatField(blank=True, null=True)
    permission = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdv_default_permissions'


class SmpVdvGeneral(models.Model):
    user_id = models.FloatField(blank=True, null=True)
    advanced_features = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    time_zone = models.CharField(max_length=32, blank=True, null=True)
    time_zone_pref = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdv_general'


class SmpVdvMapiEmail(models.Model):
    user_id = models.FloatField(blank=True, null=True)
    account_name = models.CharField(max_length=128, blank=True, null=True)
    display_name = models.CharField(max_length=128, blank=True, null=True)
    email_address = models.CharField(max_length=128, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    reply_address = models.CharField(max_length=128, blank=True, null=True)
    mapi_server = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdv_mapi_email'


class SmpVdvNotificationSchedule(models.Model):
    user_id = models.FloatField(blank=True, null=True)
    schedule = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'smp_vdv_notification_schedule'


class SmpVdvPage(models.Model):
    user_id = models.FloatField(blank=True, null=True)
    is_page_to_email = models.NullBooleanField()
    carrier = models.CharField(max_length=128, blank=True, null=True)
    pin = models.CharField(max_length=128, blank=True, null=True)
    page_email_id = models.CharField(max_length=4000, blank=True, null=True)
    page_prefix = models.CharField(max_length=128, blank=True, null=True)
    page_data_length = models.FloatField(blank=True, null=True)
    page_filter = models.FloatField(blank=True, null=True)
    body_header_format = models.CharField(max_length=256, blank=True, null=True)
    body_detail_format = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdv_page'


class SmpVdvPaging(models.Model):
    user_id = models.FloatField(blank=True, null=True)
    service_name = models.CharField(max_length=128, blank=True, null=True)
    pin = models.CharField(max_length=128, blank=True, null=True)
    enabled = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdv_paging'


class SmpVdvPreferredCredentials(models.Model):
    user_id = models.FloatField(blank=True, null=True)
    service_type = models.CharField(max_length=128, blank=True, null=True)
    service_name = models.CharField(max_length=128, blank=True, null=True)
    credentials = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'smp_vdv_preferred_credentials'


class SmpVdvServiceParms(models.Model):
    service_type = models.CharField(max_length=128, blank=True, null=True)
    service_name = models.CharField(max_length=128, blank=True, null=True)
    property_name = models.CharField(max_length=128, blank=True, null=True)
    property_value = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdv_service_parms'


class SmpVdvSmtpEmail(models.Model):
    user_id = models.FloatField(blank=True, null=True)
    email_address = models.CharField(max_length=4000, blank=True, null=True)
    subject_prefix = models.CharField(max_length=128, blank=True, null=True)
    subject_format = models.CharField(max_length=256, blank=True, null=True)
    body_header_format = models.CharField(max_length=256, blank=True, null=True)
    body_detail_format = models.CharField(max_length=256, blank=True, null=True)
    email_length = models.FloatField(blank=True, null=True)
    email_filter = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdv_smtp_email'


class SmpVdvUser(models.Model):
    user_id = models.FloatField(blank=True, null=True)
    user_name = models.CharField(max_length=256, blank=True, null=True)
    display_name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdv_user'


class SmpVdvUserLocale(models.Model):
    user_id = models.FloatField(blank=True, null=True)
    language = models.CharField(max_length=2, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    variant = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdv_user_locale'


class SmpVdvUserPref(models.Model):
    user_id = models.FloatField(blank=True, null=True)
    app = models.CharField(max_length=256, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    value = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vdv_user_pref'


class SmpVtdDgLocation(models.Model):
    target_id = models.FloatField(blank=True, null=True)
    dg_node = models.CharField(max_length=128, blank=True, null=True)
    principal_id = models.FloatField(blank=True, null=True)
    collection_modified = models.DateField(blank=True, null=True)
    collection_active = models.FloatField(blank=True, null=True)
    direct_connect = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vtd_dg_location'


class SmpVtdHistoricalLocation(models.Model):
    target_id = models.FloatField(blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    password = models.TextField(blank=True, null=True)  # This field type is a guess.
    service = models.CharField(max_length=128, blank=True, null=True)
    principal_id = models.FloatField(blank=True, null=True)
    last_modified = models.DateField(blank=True, null=True)
    is_repository = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp_vtd_historical_location'


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


class StBill(models.Model):
    dh = models.CharField(max_length=12, blank=True, null=True)
    ksdm = models.CharField(max_length=6, blank=True, null=True)
    ywlx = models.CharField(max_length=2, blank=True, null=True)
    dyksdm = models.CharField(max_length=10, blank=True, null=True)
    lrry = models.CharField(max_length=6, blank=True, null=True)
    lrsj = models.DateField(blank=True, null=True)
    shry = models.CharField(max_length=6, blank=True, null=True)
    shsj = models.DateField(blank=True, null=True)
    wcbz = models.CharField(max_length=1, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    slr_oper = models.CharField(max_length=10, blank=True, null=True)
    slr_opername = models.CharField(max_length=20, blank=True, null=True)
    dyksmc = models.CharField(max_length=200, blank=True, null=True)
    lrry_name = models.CharField(max_length=20, blank=True, null=True)
    shry_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_bill'


class StBills(models.Model):
    dh = models.CharField(max_length=12, blank=True, null=True)
    ksdm = models.CharField(max_length=6, blank=True, null=True)
    ywlx = models.CharField(max_length=2, blank=True, null=True)
    dm = models.CharField(max_length=10, blank=True, null=True)
    mc = models.CharField(max_length=80, blank=True, null=True)
    gg = models.CharField(max_length=20, blank=True, null=True)
    scph = models.CharField(max_length=20, blank=True, null=True)
    clsl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sjsl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    kysl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    pfj = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    lsj = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    dw = models.CharField(max_length=10, blank=True, null=True)
    kcsl = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bsbfyy = models.CharField(max_length=3, blank=True, null=True)
    newlsj = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    sccj = models.CharField(max_length=30, blank=True, null=True)
    sxq = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_bills'


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


class StMaterial(models.Model):
    aid_code = models.CharField(max_length=15, blank=True, null=True)
    dm = models.CharField(max_length=10, blank=True, null=True)
    mc = models.CharField(max_length=80, blank=True, null=True)
    gg = models.CharField(max_length=40, blank=True, null=True)
    dj = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    dw = models.CharField(max_length=10, blank=True, null=True)
    sjdm = models.CharField(max_length=15, blank=True, null=True)
    jb = models.IntegerField(blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    bzpym = models.CharField(max_length=10, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    add_jx = models.CharField(max_length=60, blank=True, null=True)
    add_jl = models.CharField(max_length=60, blank=True, null=True)
    add_fydw = models.CharField(max_length=60, blank=True, null=True)
    st_bz1 = models.CharField(max_length=60, blank=True, null=True)
    st_bz2 = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_material'


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


class StStock(models.Model):
    ksdm = models.CharField(max_length=6, blank=True, null=True)
    dm = models.CharField(max_length=10, blank=True, null=True)
    scph = models.CharField(max_length=20, blank=True, null=True)
    zsl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    dj = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_stock'


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


class SurveryFormanswer(models.Model):
    formanswerid = models.CharField(max_length=19, blank=True, null=True)
    formid = models.CharField(max_length=19, blank=True, null=True)
    formcode = models.CharField(max_length=50, blank=True, null=True)
    formname = models.CharField(max_length=50, blank=True, null=True)
    formbh = models.CharField(max_length=10, blank=True, null=True)
    sglarchiveid = models.CharField(max_length=19, blank=True, null=True)
    sglcheckinfoid = models.CharField(max_length=19, blank=True, null=True)
    sglcheckinfocode = models.CharField(max_length=19, blank=True, null=True)
    sglname = models.CharField(max_length=20, blank=True, null=True)
    sexid = models.CharField(max_length=1, blank=True, null=True)
    sexname = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    answerdate = models.DateField(blank=True, null=True)
    formstatus = models.CharField(max_length=1, blank=True, null=True)
    guardianname = models.CharField(max_length=50, blank=True, null=True)
    guardianrelation = models.CharField(max_length=50, blank=True, null=True)
    createrid = models.CharField(max_length=19, blank=True, null=True)
    createdeptid = models.CharField(max_length=19, blank=True, null=True)
    createdate = models.DateField(blank=True, null=True)
    operaterid = models.CharField(max_length=19, blank=True, null=True)
    operatedeptid = models.CharField(max_length=19, blank=True, null=True)
    operatedate = models.DateField(blank=True, null=True)
    isdeleted = models.CharField(max_length=1, blank=True, null=True)
    upflag = models.CharField(max_length=1, blank=True, null=True)
    myrowid = models.CharField(max_length=50, blank=True, null=True)
    mobilephone = models.CharField(max_length=50, blank=True, null=True)
    mnstatus = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survery_formanswer'


class SurveryOptionanswer(models.Model):
    optionanswerid = models.CharField(max_length=19, blank=True, null=True)
    formanswerid = models.CharField(max_length=19, blank=True, null=True)
    questionanswerid = models.CharField(max_length=19, blank=True, null=True)
    formid = models.CharField(max_length=19, blank=True, null=True)
    questionid = models.CharField(max_length=19, blank=True, null=True)
    optionid = models.CharField(max_length=19, blank=True, null=True)
    optioncode = models.CharField(max_length=50, blank=True, null=True)
    optionname = models.CharField(max_length=500, blank=True, null=True)
    optiontype = models.CharField(max_length=1, blank=True, null=True)
    answertext = models.CharField(max_length=500, blank=True, null=True)
    createrid = models.CharField(max_length=19, blank=True, null=True)
    createdeptid = models.CharField(max_length=19, blank=True, null=True)
    createdate = models.DateField(blank=True, null=True)
    operaterid = models.CharField(max_length=19, blank=True, null=True)
    operatedeptid = models.CharField(max_length=19, blank=True, null=True)
    operatedate = models.DateField(blank=True, null=True)
    isdeleted = models.CharField(max_length=1, blank=True, null=True)
    upflag = models.CharField(max_length=1, blank=True, null=True)
    myrowid = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survery_optionanswer'


class SurveryQuestform(models.Model):
    formid = models.CharField(max_length=19, blank=True, null=True)
    formcode = models.CharField(max_length=50, blank=True, null=True)
    formname = models.CharField(max_length=50, blank=True, null=True)
    adaptsexid = models.CharField(max_length=1, blank=True, null=True)
    adaptsexname = models.CharField(max_length=50, blank=True, null=True)
    adaptmarryid = models.CharField(max_length=1, blank=True, null=True)
    adaptmarryname = models.CharField(max_length=50, blank=True, null=True)
    adaptagemin = models.IntegerField(blank=True, null=True)
    adaptagemax = models.IntegerField(blank=True, null=True)
    createrid = models.CharField(max_length=19, blank=True, null=True)
    createdeptid = models.CharField(max_length=19, blank=True, null=True)
    createdate = models.DateField(blank=True, null=True)
    operaterid = models.CharField(max_length=19, blank=True, null=True)
    operatedeptid = models.CharField(max_length=19, blank=True, null=True)
    operatedate = models.DateField(blank=True, null=True)
    isdeleted = models.CharField(max_length=1, blank=True, null=True)
    upflag = models.CharField(max_length=1, blank=True, null=True)
    myrowid = models.CharField(max_length=50, blank=True, null=True)
    formsubcode = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survery_questform'


class SurveryQuestion(models.Model):
    questionid = models.CharField(max_length=19, blank=True, null=True)
    formid = models.CharField(max_length=19, blank=True, null=True)
    questionno = models.CharField(max_length=200, blank=True, null=True)
    adaptsexid = models.CharField(max_length=1, blank=True, null=True)
    adaptmarryid = models.CharField(max_length=1, blank=True, null=True)
    adaptagemin = models.IntegerField(blank=True, null=True)
    adaptagemax = models.IntegerField(blank=True, null=True)
    questioncode = models.CharField(max_length=50, blank=True, null=True)
    questiontitle = models.CharField(max_length=500, blank=True, null=True)
    questiondesc = models.CharField(max_length=500, blank=True, null=True)
    questiontype = models.CharField(max_length=1, blank=True, null=True)
    createrid = models.CharField(max_length=19, blank=True, null=True)
    createdeptid = models.CharField(max_length=19, blank=True, null=True)
    createdate = models.DateField(blank=True, null=True)
    operaterid = models.CharField(max_length=19, blank=True, null=True)
    operatedeptid = models.CharField(max_length=19, blank=True, null=True)
    operatedate = models.DateField(blank=True, null=True)
    isdeleted = models.CharField(max_length=1, blank=True, null=True)
    upflag = models.CharField(max_length=1, blank=True, null=True)
    myrowid = models.CharField(max_length=50, blank=True, null=True)
    questionpath = models.CharField(max_length=500, blank=True, null=True)
    questionlevel = models.IntegerField(blank=True, null=True)
    parentquestionid = models.CharField(max_length=19, blank=True, null=True)
    showorder = models.CharField(max_length=50, blank=True, null=True)
    checkunitid = models.CharField(max_length=19, blank=True, null=True)
    checkunitcode = models.CharField(max_length=50, blank=True, null=True)
    checkunitname = models.CharField(max_length=50, blank=True, null=True)
    questionsubtitle = models.CharField(max_length=200, blank=True, null=True)
    analyzetitle = models.CharField(max_length=50, blank=True, null=True)
    malaysia_questionno = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survery_question'


class SurveryQuestion2Option(models.Model):
    question2optionid = models.CharField(max_length=19, blank=True, null=True)
    questionid = models.CharField(max_length=19, blank=True, null=True)
    optionid = models.CharField(max_length=19, blank=True, null=True)
    optionno = models.CharField(max_length=6, blank=True, null=True)
    createrid = models.CharField(max_length=19, blank=True, null=True)
    createdeptid = models.CharField(max_length=19, blank=True, null=True)
    createdate = models.DateField(blank=True, null=True)
    operaterid = models.CharField(max_length=19, blank=True, null=True)
    operatedeptid = models.CharField(max_length=19, blank=True, null=True)
    operatedate = models.DateField(blank=True, null=True)
    isdeleted = models.CharField(max_length=1, blank=True, null=True)
    upflag = models.CharField(max_length=1, blank=True, null=True)
    myrowid = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survery_question2option'


class SurveryQuestionanswer(models.Model):
    questionanswerid = models.CharField(max_length=19, blank=True, null=True)
    formanswerid = models.CharField(max_length=19, blank=True, null=True)
    formid = models.CharField(max_length=19, blank=True, null=True)
    questionid = models.CharField(max_length=19, blank=True, null=True)
    createrid = models.CharField(max_length=19, blank=True, null=True)
    createdeptid = models.CharField(max_length=19, blank=True, null=True)
    createdate = models.DateField(blank=True, null=True)
    operaterid = models.CharField(max_length=19, blank=True, null=True)
    operatedeptid = models.CharField(max_length=19, blank=True, null=True)
    operatedate = models.DateField(blank=True, null=True)
    isdeleted = models.CharField(max_length=1, blank=True, null=True)
    upflag = models.CharField(max_length=1, blank=True, null=True)
    myrowid = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survery_questionanswer'


class SurveryQuestoption(models.Model):
    optionid = models.CharField(max_length=19, blank=True, null=True)
    parentoptionid = models.CharField(max_length=19, blank=True, null=True)
    optioncode = models.CharField(max_length=500, blank=True, null=True)
    optiontitle = models.CharField(max_length=500, blank=True, null=True)
    optiondesc = models.CharField(max_length=500, blank=True, null=True)
    iscategory = models.CharField(max_length=1, blank=True, null=True)
    optiontype = models.CharField(max_length=1, blank=True, null=True)
    createrid = models.CharField(max_length=19, blank=True, null=True)
    createdeptid = models.CharField(max_length=19, blank=True, null=True)
    createdate = models.DateField(blank=True, null=True)
    operaterid = models.CharField(max_length=19, blank=True, null=True)
    operatedeptid = models.CharField(max_length=19, blank=True, null=True)
    operatedate = models.DateField(blank=True, null=True)
    isdeleted = models.CharField(max_length=1, blank=True, null=True)
    upflag = models.CharField(max_length=1, blank=True, null=True)
    myrowid = models.CharField(max_length=50, blank=True, null=True)
    optionpath = models.CharField(max_length=500, blank=True, null=True)
    optionlevel = models.IntegerField(blank=True, null=True)
    showorder = models.CharField(max_length=50, blank=True, null=True)
    diseaseid = models.CharField(max_length=19, blank=True, null=True)
    diseasename = models.CharField(max_length=500, blank=True, null=True)
    diseasecode = models.CharField(max_length=50, blank=True, null=True)
    optionno = models.CharField(max_length=50, blank=True, null=True)
    positivetip = models.CharField(max_length=500, blank=True, null=True)
    malaysia_index = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survery_questoption'


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


class SysDataComplete(models.Model):
    code_value = models.CharField(max_length=30, blank=True, null=True)
    lb = models.CharField(max_length=2, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_data_complete'


class SysDataComplete2(models.Model):
    code_value = models.CharField(max_length=30, blank=True, null=True)
    lb = models.CharField(max_length=2, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    in_factory = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_data_complete_2'


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


class SysDeleteSyntax(models.Model):
    op_date = models.DateField(blank=True, null=True)
    up_down = models.CharField(max_length=1, blank=True, null=True)
    delete_syntax = models.CharField(max_length=220, blank=True, null=True)
    do_with = models.CharField(max_length=1, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_delete_syntax'


class SysDeleteYyqkLog(models.Model):
    billcode = models.CharField(max_length=300, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)
    cid = models.CharField(max_length=30, blank=True, null=True)
    czsj = models.DateField(blank=True, null=True)
    czry = models.CharField(max_length=100, blank=True, null=True)
    ms = models.CharField(max_length=100, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_delete_yyqk_log'


class SysDeveloper(models.Model):
    companyname = models.CharField(max_length=40, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    postcode = models.CharField(max_length=6, blank=True, null=True)
    telephone = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=25, blank=True, null=True)
    www = models.CharField(max_length=30, blank=True, null=True)
    version = models.CharField(max_length=20, blank=True, null=True)
    copyright = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    product = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_developer'


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


class SysQueue2017(models.Model):
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
        db_table = 'sys_queue_2017'


class SysQueuePt(models.Model):
    xh = models.IntegerField(blank=True, null=True)
    item_id = models.CharField(max_length=20, blank=True, null=True)
    pt_item_id1 = models.CharField(max_length=20, blank=True, null=True)
    pt_item_id2 = models.CharField(max_length=20, blank=True, null=True)
    pt_item_id3 = models.CharField(max_length=20, blank=True, null=True)
    pt_item_id4 = models.CharField(max_length=20, blank=True, null=True)
    pt_item_id5 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_queue_pt'


class SysRegionNotTrans(models.Model):
    ct = models.CharField(max_length=1, blank=True, null=True)
    hc = models.CharField(max_length=1, blank=True, null=True)
    xdt = models.CharField(max_length=1, blank=True, null=True)
    qt1 = models.CharField(max_length=1, blank=True, null=True)
    qt2 = models.CharField(max_length=1, blank=True, null=True)
    qt3 = models.CharField(max_length=1, blank=True, null=True)
    qt4 = models.CharField(max_length=1, blank=True, null=True)
    qt5 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_region_not_trans'


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


class SysRzRoom(models.Model):
    userid = models.CharField(max_length=20, blank=True, null=True)
    other_userid = models.CharField(max_length=20, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_rz_room'


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


class SysTransColumn(models.Model):
    table_name = models.CharField(max_length=40, blank=True, null=True)
    column_name = models.CharField(max_length=40, blank=True, null=True)
    column_memo = models.CharField(max_length=40, blank=True, null=True)
    sxh = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_trans_column'


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


class SysTransLog(models.Model):
    record_id = models.BigIntegerField(blank=True, null=True)
    trans_date = models.DateField(blank=True, null=True)
    file_name = models.CharField(max_length=60, blank=True, null=True)
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    table_name = models.CharField(max_length=30, blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    trans_type = models.CharField(max_length=1, blank=True, null=True)
    in_thread = models.CharField(max_length=1, blank=True, null=True)
    file_length = models.BigIntegerField(blank=True, null=True)
    record_num = models.IntegerField(blank=True, null=True)
    up_trans_result = models.CharField(max_length=1, blank=True, null=True)
    down_trans_result = models.CharField(max_length=1, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_trans_log'


class SysTransMiddle(models.Model):
    id = models.CharField(max_length=300, blank=True, null=True)
    table_name = models.CharField(max_length=200, blank=True, null=True)
    bz_number = models.CharField(max_length=200, blank=True, null=True)
    code_value = models.CharField(max_length=200, blank=True, null=True)
    bz1 = models.CharField(max_length=200, blank=True, null=True)
    bz2 = models.CharField(max_length=200, blank=True, null=True)
    bz3 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_trans_middle'


class SysTransPoint(models.Model):
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    point_name = models.CharField(max_length=50, blank=True, null=True)
    jb = models.FloatField(blank=True, null=True)
    sjdm = models.CharField(max_length=16, blank=True, null=True)
    yzjf = models.CharField(max_length=1, blank=True, null=True)
    yxf = models.CharField(max_length=1, blank=True, null=True)
    cpu_serial = models.CharField(max_length=60, blank=True, null=True)
    dis_serial = models.CharField(max_length=60, blank=True, null=True)
    day_jcmyrs = models.IntegerField(blank=True, null=True)
    dz = models.CharField(max_length=500, blank=True, null=True)
    allname = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_trans_point'


class SysTransRecord(models.Model):
    in_factory = models.CharField(max_length=20, blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, null=True)
    oper = models.CharField(max_length=50, blank=True, null=True)
    memo = models.CharField(max_length=250, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    op_date = models.DateField(blank=True, null=True)
    record_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_trans_record'


class SysTransSfmxb(models.Model):
    id = models.CharField(max_length=500, blank=True, null=True)
    local_vid = models.CharField(max_length=30, blank=True, null=True)
    czf1 = models.IntegerField(blank=True, null=True)
    czf2 = models.IntegerField(blank=True, null=True)
    sfmxid = models.CharField(max_length=14, blank=True, null=True)
    vid = models.CharField(max_length=12, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    groupid = models.CharField(max_length=10, blank=True, null=True)
    groupname = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    standard = models.CharField(max_length=20, blank=True, null=True)
    jzf = models.CharField(max_length=1, blank=True, null=True)
    jzdhm = models.CharField(max_length=14, blank=True, null=True)
    oldprice = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    jxf = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    user_id = models.CharField(max_length=6, blank=True, null=True)
    member_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    sf_ywydm = models.CharField(max_length=6, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_trans_sfmxb'


class SysTransSfmxbVid(models.Model):
    id = models.CharField(max_length=500, blank=True, null=True)
    local_vid = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_trans_sfmxb_vid'


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


class SysUserobject(models.Model):
    moudleid = models.CharField(max_length=6, blank=True, null=True)
    pblname = models.CharField(max_length=20, blank=True, null=True)
    customername = models.CharField(max_length=50, blank=True, null=True)
    windowname = models.CharField(max_length=20, blank=True, null=True)
    dwname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_userobject'


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


class ZyTzpsResults(models.Model):
    cid = models.CharField(max_length=30, blank=True, null=True)
    vid = models.CharField(max_length=30, blank=True, null=True)
    zy_1 = models.CharField(max_length=10, blank=True, null=True)
    zy_2 = models.CharField(max_length=10, blank=True, null=True)
    zy_3 = models.CharField(max_length=10, blank=True, null=True)
    zy_4 = models.CharField(max_length=10, blank=True, null=True)
    zy_5 = models.CharField(max_length=10, blank=True, null=True)
    zy_6 = models.CharField(max_length=10, blank=True, null=True)
    zy_7 = models.CharField(max_length=10, blank=True, null=True)
    zy_8 = models.CharField(max_length=10, blank=True, null=True)
    zy_9 = models.CharField(max_length=10, blank=True, null=True)
    zy_10 = models.CharField(max_length=10, blank=True, null=True)
    zy_11 = models.CharField(max_length=10, blank=True, null=True)
    zy_12 = models.CharField(max_length=10, blank=True, null=True)
    zy_13 = models.CharField(max_length=10, blank=True, null=True)
    zy_14 = models.CharField(max_length=10, blank=True, null=True)
    zy_15 = models.CharField(max_length=10, blank=True, null=True)
    zy_16 = models.CharField(max_length=10, blank=True, null=True)
    zy_17 = models.CharField(max_length=10, blank=True, null=True)
    zy_18 = models.CharField(max_length=10, blank=True, null=True)
    zy_19 = models.CharField(max_length=10, blank=True, null=True)
    zy_20 = models.CharField(max_length=10, blank=True, null=True)
    zy_21 = models.CharField(max_length=10, blank=True, null=True)
    zy_22 = models.CharField(max_length=10, blank=True, null=True)
    zy_23 = models.CharField(max_length=10, blank=True, null=True)
    zy_24 = models.CharField(max_length=10, blank=True, null=True)
    zy_25 = models.CharField(max_length=10, blank=True, null=True)
    zy_26 = models.CharField(max_length=10, blank=True, null=True)
    zy_27 = models.CharField(max_length=10, blank=True, null=True)
    zy_28 = models.CharField(max_length=10, blank=True, null=True)
    zy_29 = models.CharField(max_length=10, blank=True, null=True)
    zy_30 = models.CharField(max_length=10, blank=True, null=True)
    zy_31 = models.CharField(max_length=10, blank=True, null=True)
    zy_32 = models.CharField(max_length=10, blank=True, null=True)
    zy_33 = models.CharField(max_length=10, blank=True, null=True)
    zy_34 = models.CharField(max_length=10, blank=True, null=True)
    zy_35 = models.CharField(max_length=10, blank=True, null=True)
    zy_36 = models.CharField(max_length=10, blank=True, null=True)
    zy_37 = models.CharField(max_length=10, blank=True, null=True)
    zy_38 = models.CharField(max_length=10, blank=True, null=True)
    zy_39 = models.CharField(max_length=10, blank=True, null=True)
    zy_40 = models.CharField(max_length=10, blank=True, null=True)
    zy_41 = models.CharField(max_length=10, blank=True, null=True)
    zy_42 = models.CharField(max_length=10, blank=True, null=True)
    zy_43 = models.CharField(max_length=10, blank=True, null=True)
    zy_44 = models.CharField(max_length=10, blank=True, null=True)
    zy_45 = models.CharField(max_length=10, blank=True, null=True)
    zy_46 = models.CharField(max_length=10, blank=True, null=True)
    zy_47 = models.CharField(max_length=10, blank=True, null=True)
    zy_48 = models.CharField(max_length=10, blank=True, null=True)
    zy_49 = models.CharField(max_length=10, blank=True, null=True)
    zy_50 = models.CharField(max_length=10, blank=True, null=True)
    zy_51 = models.CharField(max_length=10, blank=True, null=True)
    zy_52 = models.CharField(max_length=10, blank=True, null=True)
    zy_53 = models.CharField(max_length=10, blank=True, null=True)
    zy_54 = models.CharField(max_length=10, blank=True, null=True)
    zy_55 = models.CharField(max_length=10, blank=True, null=True)
    zy_56 = models.CharField(max_length=10, blank=True, null=True)
    sz_1 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    sz_2 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    sz_3 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    sz_4 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    sz_5 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    sz_6 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    sz_7 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    sz_8 = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    zycp_results = models.CharField(max_length=500, blank=True, null=True)
    trans_status = models.CharField(max_length=1, blank=True, null=True)
    op_datetime = models.DateField(blank=True, null=True)
    lr_oper = models.CharField(max_length=30, blank=True, null=True)
    lr_opername = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zy_tzps_results'


class ZybInterfaceList(models.Model):
    vid = models.CharField(max_length=20, blank=True, null=True)
    barcode = models.CharField(max_length=50, blank=True, null=True)
    bz1 = models.CharField(max_length=100, blank=True, null=True)
    bz2 = models.CharField(max_length=100, blank=True, null=True)
    bz3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zyb_interface_list'
