from django.db import models

from user.models import User


class Car(models.Model):
    CAR_ITEMS=(
        (1,'普通校车'),
        (2,'教师用车'),
    )
    STATE_ITEMS=(
        (1,'正常发车'),
        (2,'人数太少不发车'),
    )

    car_num=models.CharField(verbose_name='车牌号',max_length=20)
    driver =models.CharField(verbose_name='驾驶员',max_length=10)
    driver_phone=models.CharField(verbose_name='驾驶员电话',max_length=15)
    set_num = models.IntegerField(verbose_name='座位数')
    price =models.FloatField(verbose_name='价格',max_length=10)
    notice =models.TextField(verbose_name='公告')
    car_type=models.PositiveIntegerField(choices=CAR_ITEMS,default=1,verbose_name='用车类型')
    car_state=models.PositiveIntegerField(choices=STATE_ITEMS,default=1,verbose_name='用车状态')#默认正常

    class Meta:
        verbose_name_plural = verbose_name = '校车'
    def __str__(self):
        return self.car_num

class PathType(models.Model):
    path_name=models.CharField(verbose_name='路径名',max_length=20)

    class Meta:
        verbose_name_plural=verbose_name='路线'
    def __str__(self):
        return self.path_name

class Autoshift(models.Model):


    times = models.DateTimeField(verbose_name='班车时间')  # 待考虑
    duration = models.CharField(verbose_name='时长', max_length=40)
    path = models.ForeignKey(PathType,on_delete=models.CASCADE)
    car =models.ManyToManyField(Car)
    user = models.ManyToManyField(User,through='CarAndShift')#后台有问题

    class Meta:
        verbose_name_plural = verbose_name = '汽车班次'
        ordering = ['times']

#用户和汽车班次的第三张表，添加额外信息，预约时间，人数，创建时间
class CarAndShift(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    shift=models.ForeignKey(Autoshift,on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    due_num =models.IntegerField(verbose_name='预约人数')

    class Meta:
        verbose_name_plural=verbose_name='用户约车'


