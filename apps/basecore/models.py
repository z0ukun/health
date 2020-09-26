from django.db import models


# Create your models here.
# 客人预约情况表
class JjYyqkb(models.Model):
    vid = models.CharField(primary_key=True, max_length=12, blank=True, null=True, verbose_name=u"VID")
    cid = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"健检号")
    dwdm = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"单位编码")
    yysj = models.DateField(blank=True, null=True, verbose_name=u"预约时间")
    yyzh = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"预约组号")
    yydjr = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"预约登记人")
    yydjsj = models.DateField(blank=True, null=True, verbose_name=u"预约登记时间")
    jjzh = models.CharField(max_length=5, blank=True, null=True, verbose_name=u"健检组号")
    jjlsh = models.FloatField(blank=True, null=True, verbose_name=u"健检流水号")
    # 状态['0':1:]
    status = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"预约状态")
    qtdjr = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"前台登记人")
    qtdjsj = models.DateField(blank=True, null=True, verbose_name=u"前台登记时间")
    tjsj = models.DateField(blank=True, null=True, verbose_name=u"体检时间")
    tjzzsj = models.DateField(blank=True, null=True, verbose_name=u"体检终止时间")
    # 电话通知:1是0否
    tzf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"停止否")
    dwjzf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"团体体检否")
    member_type = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"会员类型")
    yydhtzr = models.CharField(max_length=25, blank=True, null=True, verbose_name=u"预约电话通知人")
    # 作为是否当天拿报告单（用)
    yyth = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"预约电话")
    zyf = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"数据转移否")
    # 报告单方式（1：自取 2：邮寄 3：送达）
    jjch = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"报告单方式")
    print_time = models.DateField(blank=True, null=True, verbose_name=u"打印时间")
    trans_status = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"传输状态")
    ywydm = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"业务员代码")
    yqhff = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"一期回访否")
    erqhff = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"二期回访否")
    sqhff = models.CharField(max_length=1, blank=True, null=True, verbose_name=u"三期回访否")
    tcbl = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True, verbose_name=u"VID")
    dwyyid = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"单位预约ID")
    cust_name = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"姓名")
    cust_xb = models.CharField(max_length=2, blank=True, null=True, verbose_name=u"性别")
    cust_csrq = models.DateField(blank=True, null=True, verbose_name=u"出生日期")
    temp_bz = models.CharField(max_length=3000, blank=True, null=True, verbose_name=u"临时备注")
    cust_zy = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"职业")
    cust_gzhy = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"工作行业")
    zzys = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"咨询医生")
    zzhs = models.CharField(max_length=6, blank=True, null=True, verbose_name=u"ZZHS")
    in_floor = models.CharField(max_length=10, blank=True, null=True, verbose_name=u"制定进入某一层")
    gzhy_dm = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"工作行业代码")
    bz_fgs = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注-分公司")
    bz_bm1 = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注-部门1")
    bz_bm2 = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注-部门2")
    bz_ygh = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注-员工号")
    bz_sfzhm = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注-身份证号码")
    bz_a = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注-A")
    bz_b = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注-B")
    bz_c = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注-C")
    bz_xj = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"备注-XJ")
    bz_gz = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"备注-GZ")
    bz_lpk = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name=u"备注-LQK")

    class Meta:
        managed = False
        db_table = 'jj_yyqkb'
        verbose_name = u"预约信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.vid


# 客人基本信息
class BasCustInfor(models.Model):
    cid = models.CharField(primary_key=True, max_length=12, blank=True, null=True, verbose_name=u"健检号")
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
        verbose_name = u"登记信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.cid
