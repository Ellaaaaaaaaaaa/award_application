from django.shortcuts import render


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def home(request):
    """
    首页
    """
    return render(request, 'award_declaration/index_home.html')


def organization(request):
    """
    组织管理首页
    """
    return render(request, 'award_declaration/organization/index.html')


def award(request):
    """
    奖项管理首页
    """
    return render(request, 'award_declaration/award/index.html')


def batch_copy(request):
    """
    批量克隆首页
    """
    return render(request, 'award_declaration/award/copy.html')