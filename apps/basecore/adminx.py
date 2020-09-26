import xadmin
from .models import JjYyqkb, BasCustInfor


class JjYyqkbAdmin(object):
    list_display = ['vid', 'cid', 'dwdm', 'yysj', 'tjzzsj', 'ywydm', 'status', 'trans_status', 'print_time', 'jjch']
    list_filter = ['cust_name']
    search_fields = ['cust_name']
    # list_filter = ['vid', 'cid', 'dwdm', 'yysj', 'yyzh', 'yydjr', 'yydjsj', 'jjzh', 'jjlsh', 'status', 'qtdjr',
    #                'qtdjsj', 'tjsj', 'tjzzsj', 'tzf', 'dwjzf', 'member_type', 'yydhtzr', 'yyth', 'zyf', 'jjch',
    #                'print_time', 'trans_status', 'ywydm', 'yqhff', 'erqhff', 'sqhff', 'tcbl', 'dwyyid', 'cust_name',
    #                'cust_xb', 'cust_csrq', 'temp_bz', 'cust_zy', 'cust_gzhy', 'zzys', 'zzhs', 'in_floor', 'gzhy_dm']
    # search_fields = ['vid', 'cid', 'dwdm', 'yysj', 'yyzh', 'yydjr', 'yydjsj', 'jjzh', 'jjlsh', 'status', 'qtdjr',
    #                  'qtdjsj', 'tjsj', 'tjzzsj', 'tzf', 'dwjzf', 'member_type', 'yydhtzr', 'yyth', 'zyf', 'jjch',
    #                  'print_time', 'trans_status', 'ywydm', 'yqhff', 'erqhff', 'sqhff', 'tcbl', 'dwyyid', 'cust_name',
    #                  'cust_xb', 'cust_csrq', 'temp_bz', 'cust_zy', 'cust_gzhy', 'zzys', 'zzhs', 'in_floor', 'gzhy_dm']


class BasCustInforAdmin(object):
    list_display = ['cid', 'xm', 'xb', 'csrq', 'sfzhm']
    list_filter = ['xm', 'xb']
    search_fields = ['xm', 'xb']
    # search_fields = ['xm']
    # list_filter = ['course', 'name', 'add_time', 'download']
    # search_fields = ['course', 'name', 'download']


xadmin.site.register(JjYyqkb, JjYyqkbAdmin)
xadmin.site.register(BasCustInfor, BasCustInforAdmin)
