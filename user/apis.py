from django.http import JsonResponse
from django.shortcuts import render

from common import error
from lib.http import render_json
from lib.sms import send_vcode, check_vcode


# API接口
# 发送验证码
from user.models import User, Profile


def submit_vcode(request):

    # 先从前端获取手机号
    phone = request.GET.get('phone')
    # 发送验证码
    result = send_vcode(phone)

    return render_json(result)


# 登入
def login(request):

    # 获取前端提交的数据
    phone = request.POST.get('phone')
    vcode = request.POST.get('vcode')

    # 检查用户的验证码是否正确
    if check_vcode(phone, vcode):
        print("登录成功！")

        user, created = User.objects.get_or_create(nickname=phone, phonenum=phone)

        request.session['uid'] = user.id

        return render_json(user.to_dict())

    else:
        print("验证码输入错误")
        return render_json("验证码错误", error.VCODE_ERROR)


# 获取用户交友配置
def get_profile(request):
    user = request.user
    return  render_json(user.profile.to_dict())






