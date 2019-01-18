from django.utils.deprecation import MiddlewareMixin

from common import error
from lib.http import render_json
from user.models import User


class AuthMiddleware(MiddlewareMixin):

    URL_WHITE_LIST = [
        '/api/user/submit/vcode/',
        '/api/user/submit/login/',
    ]

    def process_requeset(self, request):
        path = request.path
        print('paht:', path)

        if path in self.URL_WHITE_LIST:
            return

        # 检测用户是否存在
        uid = request.session.get('uid')
        print('AuthMiddleware: uid', uid)
        if uid:
            try:
                request.user = User.objects.get(id=uid)
            except Exception as e:

                return render_json('不存在该用户', error.SUER_NOTEXIST)
        else:
            return render_json('用户未登录', error.LOGIN_REQUIRED)


