from django.shortcuts import redirect

from django.utils.deprecation import MiddlewareMixin
import uuid


def process_request(request):
    # 0.排除那些不需要登录就能访问的页面
    # request.path_info 获取当前用户请求的URL /login/
    if request.path_info in ['/home/login/', '/home/code/']:
        return
    # 1.读取当前访问的用户的session信息，如果能读到，说明已登录过，就可以继续向后走。
    info_dict = request.session.get('info')
    if info_dict:
        return
    # 2.没有登录过，重新回到登录页面
    return redirect('/home/login/')


def is_valid_uuid(val):
    try:
        uuid_object = uuid.UUID(val)
        return str(uuid_object) == val
    except ValueError:
        return False


class AuthMiddleware(MiddlewareMixin):
    pass
