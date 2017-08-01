from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def login(request):
    error_msg = ""
    if request.method == 'POST':
         user = request.POST.get('user', None)
         pwd = request.POST.get('pwd', None)
         if user == 'root' and pwd == '123456':
             return redirect("http://www.baidu.com")
         else:
             error_msg = "用户名或密码错误"
    return render(request, "login.html", {'error_msg':error_msg})

from django.views import View

class Home(View):
    def dispatch(self, request, *args, **kwargs):
        result = super(Home, self).dispatch(request, *args, **kwargs)
        return result

    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        print(request.method)


def detail(request, nid, nid2):
    return HttpResponse(nid2)

from csdb import  models
def orm(request):
    # models.UserInfo.objects.create(
    #     username = 'root',
    #     password = '123'
    # )
    # obj = models.UserInfo(username = 'wql',password = '123')
    # obj.save()
    #result = models.UserInfo.objects.all()
    result = models.UserInfo.objects.all().delete()
    result = models.UserInfo.objects.filter(username='root',password='123')
    for item in result:
        print(item.username, item.password)
    return HttpResponse('orm')


