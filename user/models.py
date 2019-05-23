from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    gender=(
        ('male','男'),
        ('female','女'),
    )

    IDENTITIES =(
        (1,'普通学生'),
        (2,'学生干部'),
        (3,'职工'),
    )
    
    nickname=models.CharField(max_length=30,verbose_name='昵称')
    sex = models.CharField(max_length=20,choices=gender,default='男',verbose_name='性别')
    userid = models.CharField(max_length=20,verbose_name='学号/工号')
    username = models.CharField(max_length=30,verbose_name='姓名',unique=True)
    grade = models.CharField(max_length=20,verbose_name='年级')
    mobile=models.CharField(max_length=20,verbose_name='手机号')
    identity=models.PositiveIntegerField(verbose_name='身份',choices=IDENTITIES,default=1)

    class Meta:
        verbose_name_plural=verbose_name='用户'
        ordering=['-id']

    def __str__(self):
        return self.username