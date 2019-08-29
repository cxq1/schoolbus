from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse


from .models import *
from django.db.models import Q
from django.contrib import messages, auth
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from .form import MyUserCreationForm


def home(request):
    return render(request, 'center.html')


def loginView(request):
    if request.method == "POST":
        userid = request.POST.get("UserId", '')
        username = request.POST.get("UserName", '')

        password = request.POST.get("Password", '')

        # user = auth.authenticate(username=username, password=password)
        # print(user)
        user = User.objects.get(userid=userid)
        pwd = user.password
        # print(pwd)
        if check_password(password, pwd):
            login(request, user)
            print(1)

            return redirect('home')
        else:
            print("1")
            return redirect('login')

        # print(user)
        # if user is None:
        #     print("1")
        #     redirect('login')
        # else:
        #     auth.login(request, user)
        #     return redirect('home')
        # try:
        #     user = User.objects.get(userid=userid)
        #     print(user.password)
        #     if user.password == Password:
        #         request.session['userid'] = UserId
        #         return redirect('home')
        #     else:
        #
        #         messages.success(request, "密码不正确")
        # except:
        #
        #     messages.success(request, "学号不正确")
        # return render(request, "user/login.html", {"data": UserId})
    else:

        return render(request, "user/login.html")
    return render(request, "user/login.html")


def registeredView(request):
    if request.method == 'POST':

        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            userid = form.cleaned_data['userid']
            password = form.cleaned_data['password1']
            username = form.cleaned_data['username']
            mobile = form.cleaned_data['mobile']
            nickname = form.cleaned_data['nickname']
            grade = form.cleaned_data['grade']
            sex = form.cleaned_data['sex']
            identity = form.cleaned_data['identity']

            user = User.objects.filter(userid=userid)

            print(user)
            if user:
                messages.success(request, "用户名已被注册")
                return render(request, 'user/registered.html', locals())

            else:

                user = User.objects.create_user\
                    (userid=userid, password=password, username=username, nickname=nickname, mobile=mobile, sex=sex,
                     identity=identity)
                user.save()

                print("3")

                return redirect('login')


    else:
        form = MyUserCreationForm()
    return render(request, 'user/registered.html', locals())


def logoutView(request):
        logout(request)
        return redirect('/')

    # user = MyUserCreationForm()
    # if request.method == 'POST':
    #     if request.POST.get('UserId', ''):
    #         UserId = request.POST.get('UserId', '')
    #         Password = request.POST.get('Password', '')
    #         if User.objects.filter(Q(userid=UserId) ):
    #             user = \
    #                 User.objects.filter(Q(userid=UserId).first())
    #             if check_password(Password, user.password):
    #                 login(request, user)
    #                 return redirect('/user/home.html')
    #             else:
    #                 tips = '密码错误'
    #         else:
    #             tips = '用户不存在'
    #     else:
    #         user = MyUserCreationForm(request.POST)
    #         if user.is_valid():
    #             user.save()
    #             tips = '注册成功'
    #         else:
    #             if user.errors.get('UserId', ''):
    #                 tips = user.errors.get('UserId', '注册失败')
    #             elif user.errors.get('UserName', ''):
    #                 tips = user.errors.get('UserName', '注册失败')
    #             elif user.errors.get('NickName', ''):
    #                 tips = user.errors.get('NickName', '注册失败')
    #             elif user.errors.get('Sex', ''):
    #                 tips = user.errors.get('Sex', '注册失败')
    #             elif user.errors.get('UserName', ''):
    #                 tips = user.errors.get('MajorGrade', '注册失败')
    #             elif user.errors.get('Tel', ''):
    #                 tips = user.errors.get('Tel', '注册失败')
    #             elif user.errors.get('Identity', ''):
    #                 tips = user.errors.get('Identity', '注册失败')
    # return render(request, 'login.html', locals())