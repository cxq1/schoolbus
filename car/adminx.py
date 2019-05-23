import xadmin
from xadmin.layout import Main,Row,Fieldset
from .models import Car,CarAndShift,Autoshift,PathType

class CarAdmin(object):

    # def show_cars(self,obj):
    #     return [a.car_num for a in obj.shift.all()]

    list_display=['car_num','driver','driver_phone','set_num','price','notice','car_type','car_state']
    search_fields=['car_num','car_type']
    list_filter=['car_type']

    form_layout=(
        Main(
            Fieldset(
                '驾驶员信息',
                Row('driver','driver_phone')
            ),
            Fieldset(
                '汽车相关信息',
                'car_num','set_num','price','car_type','car_state'
            ),
            Fieldset(
                '其他信息',
                'notice',
            )
        )
    )

class AutoshiftAdmin(object):
    #为了解决user字段无法显示,还是不行..
    def show_user(self,obj):
        return [a.username for a in obj.user.all()]

    list_display=['times','duration','path','car','show_user']
    search_fields=['path','car','user']
    list_filter=['path','car','user']

class CarAndShiftAdmin(object):
    list_display=['user','shift','created_time','due_num']
    search_fields=['user','shift','created_time']
    list_filter=['user','shift','created_time']


class PathTypeAdmin(object):
    list_display=['path_name']
    search_fields=['path_name']
    list_filter=['path_name']


xadmin.site.register(Car,CarAdmin)
xadmin.site.register(Autoshift,AutoshiftAdmin)
xadmin.site.register(CarAndShift,CarAndShiftAdmin)
xadmin.site.register(PathType,PathTypeAdmin)
