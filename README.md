##我要上车
1.在一个目录下创建虚拟环境 安装 pip3 install virtualenv
 创建虚拟环境 virtualenv  env_django
 激活该虚拟环境：
    -windows进到目录里，的Script文件夹输入：activate
    cd env_django
    Scripts\activate
2.在最初的根目录下打开git
git clone https://github.com/cxq1/schoolbus.git  [解决git 下载慢](https://blog.csdn.net/weixin_45122120/article/details/91872691)

3.进入项目目录 执行 pip install -r packages.txt [解决pip下载慢](https://blog.csdn.net/qq_16481211/article/details/81081996)
安装xadmin pip install https://codeload.github.com/sshwsfc/xadmin/zip/django2
在 schoolbus目录下 python manage.py migrate
创建超级管理员用户 python manage.py createsuperuser
启动项目：python manage.py runserver
后台页面：http://127.0.0.1:8000/admin/
注册的时候年级和身份填 【1-3】