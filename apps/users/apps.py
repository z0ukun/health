from django.apps import AppConfig


class UsersConfig(AppConfig):
    # 设置APP图标
    app_icon = 'fa-fw fa fa-group'

    # 设置APP名称
    name = 'users'
    verbose_name = u"用户管理"
