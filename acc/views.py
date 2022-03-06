from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .models import User
# Create your views here.
def index(request):
    return render(request, "acc/index.html")

def login_user(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        up = request.POST.get('upass')
        user = authenticate(username = un, password = up)
        if user:
            login(request, user)
            return redirect('acc:index')
    return render(request, "acc/login.html")

def logout_user(request):
    logout(request)
    return redirect('acc:index')

def signup(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        up = request.POST.get('upass')
        uc = request.POST.get('ucomm')
        uf = request.FILES.get('upic')
        User.objects.create_user(username = un, password = up, comment = uc, pic =uf)
        return redirect('acc:login')
    return render(request,'acc/signup.html')

def profile(request):
    return render(request,"acc/profile.html")

def delete(request):
    request.user.delete()
    return redirect('acc:index')

def user_update(request):
    if request.method == "POST":
        u = request.user
        up = request.POST.get('upass')
        ue = request.POST.get('umail')
        uc = request.POST.get('ucomm')
        uf = request.FILES.get('upic')
        if up:
            u.set_password(up)
        u.comment = uc
        u.email = ue
        if uf:
            u.pic.delete()
            u.pic = uf
        u.save()
        login(request,u)     
        return redirect('acc:profile')
    return render(request,'acc/update.html')