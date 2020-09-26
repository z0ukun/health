import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin

# 自定义默认菜单名称
from xadmin.models import Log
from .models import UserProfile
from django.contrib.auth.models import Group, Permission

# 预约管理
from basecore.models import JjYyqkb

# 前台管理
from basecore.models import BasCustInfor


# 检查管理

# 收费管理

class UserProfileAdmin(UserAdmin):
    pass


class BaseSetting(object):
    # """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True  # 支持切换主题


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    # 自定义导航顺序
    def get_site_menu(self):
        return (
            {'title': '核心业务', 'menus': (
                {'title': '预约信息', 'url': self.get_model_url(JjYyqkb, 'changelist'), 'icon': 'fa fa-user'},
                {'title': '登记信息', 'url': self.get_model_url(BasCustInfor, 'changelist'), 'icon': 'fa fa-user'},
                # {'title': '检查管理', 'url': self.get_model_url(UserProfile, 'changelist')},
                # {'title': '收费管理', 'url': self.get_model_url(UserProfile, 'changelist')},
            )},
            {'title': '系统管理', 'icon': 'fa fa-th-large', 'menus': (
                {'title': '后台用户', 'url': self.get_model_url(UserProfile, 'changelist'), 'icon': 'fa fa-user'},
                {'title': '用户分组', 'url': self.get_model_url(Group, 'changelist'), 'icon': 'fa fa-group'},
                {'title': '用户权限', 'url': self.get_model_url(Permission, 'changelist'), 'icon': 'fa fa-lock'},
                {'title': '日志记录', 'url': self.get_model_url(Log, 'changelist'), 'icon': 'fa fa-cog'},
            )},)

    # """xadmin的全局配置"""
    site_title = "后台管理系统"  # 设置站点标题
    site_footer = "湖北三好电子有限公司"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠，在左侧，默认的

    # 设置models的全局图标, UserProfile, Sports 为表名
    # global_search_models = [UserProfile]
    # global_models_icon = {
    #     UserProfile: "fa fa-user"}


# xadmin.site.register(UserAdmin, UserProfileAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)
