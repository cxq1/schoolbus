from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class MyUserCreationForm (forms.Form):
    username =forms.CharField(max_length=20,label='用户名',widget=forms.TextInput(attrs={'placeholder': '用户名'}))
    password1=forms.CharField(label='密码',widget=forms.PasswordInput(attrs={'placeholder': '密码'}))
    password2 = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'placeholder': '重新输入密码'}))
    mobile=forms.CharField(label='手机号',widget=forms.TextInput(attrs={'placeholder': '手机号'}))
    sex = forms.CharField(label='性别', widget=forms.TextInput(attrs={'placeholder': '性别'}))
    userid = forms.CharField(label='id', widget=forms.TextInput(attrs={'placeholder': '学号'}))
    nickname = forms.CharField(label='昵称', widget=forms.TextInput(attrs={'placeholder': '昵称'}))
    grade = forms.CharField(label='年级', widget=forms.TextInput(attrs={'placeholder': '年级'}))
    identity = forms.CharField(label='身份', widget=forms.TextInput(attrs={'placeholder': '身份'}))

    # def clean_username(self):
    #     username=self.cleaned_data['username']
    #     if User.objects.filter(username=username).exists:
    #         raise forms.ValidationError("用户名已经存在")
    #     return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError("密码不一致")
        return password2

        # class Meta :
        #     model = User
        #     fields = ('username','password1','password2','mobile', 'sex', 'userid', 'nickname', 'grade', 'identity')
        #     widgets = {
        #         'identity':forms.widgets.TextInput(attrs={'class': 'txt tabInput', 'placeholder': '身份'}),
        #         'grade': forms.widgets.TextInput(attrs={'class': 'txt tabInput', 'placeholder': '年级'}),
        #         'nickname': forms.widgets.TextInput(attrs={'class': 'txt tabInput', 'placeholder': '昵称'}),
        #         'userid':forms.widgets.TextInput(attrs={'class': 'txt tabInput', 'placeholder': '学号/工号'}),
        #         'sex': forms.widgets.TextInput(attrs={'class': 'txt tabInput', 'placeholder': '性别'}),
        #         'mobile': forms.widgets.TextInput(attrs={'class': 'txt tabInput', 'placeholder': '手机号'}),
        #         'username': forms.widgets.TextInput(attrs={'class': 'txt tabInput', 'placeholder': '姓名'}),
        #     }