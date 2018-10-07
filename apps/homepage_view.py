from django.http import HttpResponse
from django.views import View


class HomepageView(View):
    def get(self, request, *args, **kwargs):
        """
        首页
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return HttpResponse('<div>欢迎使用loonflow<br><a href="/admin">管理后台<br><a href="https://github.com/blackholll/loonflow">使用文档</a></div>')