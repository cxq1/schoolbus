from django.db import models

# Create your models here.
from car.models import Car
from user.models import User


class Comment(models.Model):

    STATUS_NORMAL =1
    STATUS_DELETE =0
    STATUS_ITEMS=(
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )

    content = models.TextField(verbose_name='评论内容')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    status =models.PositiveIntegerField(choices=STATUS_ITEMS,default=STATUS_NORMAL,verbose_name='状态')
    target = models.ForeignKey(Car,verbose_name='评论目标',on_delete=models.CASCADE)
    user =models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='评论人')

    class Meta:
        verbose_name_plural= verbose_name='评论'
        ordering=['-id']

    def __str__(self):
        return self.content