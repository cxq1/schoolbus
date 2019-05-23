import xadmin
from xadmin import views

from .models import User

class UserAdmin(object):
    list_display=['username','sex','userid','grade','identity','mobile','nickname']
    search_fields=['username','userid','grade','identity']
    list_filter=['grade','identity','sex']

xadmin.site.unregister(User)
xadmin.site.register(User,UserAdmin)

class GlobalSetting(object):
    site_title ="校车管理系统 V1.0_beta"
    site_footer ="2019 "
xadmin.site.register(views.CommAdminView, GlobalSetting)