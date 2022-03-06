from django.shortcuts import redirect, render
from.models import Board, Reply
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    cate = request.GET.get("cate","")
    kw = request.GET.get('kw',"")
    
    if kw:
        if cate =='sub':
            b = Board.objects.filter(subject__startswith=kw)
        elif cate =='wri':
            try:
                from acc.models import User
                u = User.objects.get(username = kw)
                b = Board.objects.filter(writer = u)
            except:
                b = Board.objects.none()
        elif cate =='con':
            b = Board.objects.filter(cotent__contains=kw)
    else:
        b = Board.objects.all()
    b = b.order_by('-pubdate')
    page = request.GET.get("page",1)
    pag = Paginator(b,10)
    obj = pag.get_page(page)
    context = {
        "bset" : obj,
        "kw" : kw,
        "cate" : cate
    }
    return render(request,"board/index.html",context)

def detail(request, bpk):
    b = Board.objects.get(id=bpk)
    r = b.reply_set.all()
    context = {
        "b" : b,
        "rset" : r,
    }
    return render(request, 'board/detail.html', context)

def delete(request,bpk):
    b = Board.objects.get(id=bpk)
    if request.user == b.writer:
        b.delete()
    else:
        pass #내일 채워놓을곳
    return redirect ("board:index")

def create(request):
    if request.method =='POST':
        s = request.POST.get('sub')
        c = request.POST.get('con')
        if s and c:   
            Board(subject = s, cotent = c, writer=request.user, pubdate=timezone.now()).save()
            return redirect('board:index')
    return render(request,'board/create.html')

def update(request,bpk):
    b = Board.objects.get(id=bpk)
    
    if request.user != b.writer:
        #내일 채워놓을곳
        return redirect("board:index")
    
    if request.method =='POST':
        s = request.POST.get('sub')
        c = request.POST.get('con')
        b.subject = s
        b.cotent = c
        b.save()
        return redirect("board:detail", bpk)
    context = {
        "b" : b
    }
    
    return render(request,'board/update.html',context)

def creply(request, bpk):
    b = Board.objects.get(id=bpk)
    c = request.POST.get('com')
    if c:
        Reply(board=b, replyer = request.user, comment=c).save()
    return redirect("board:detail",bpk)

def dreply(request,bpk,rpk):
    r = Reply.objects.get(id=rpk)
    if request.user == r.replyer:
        r.delete()
    return redirect("board:detail",bpk)

def likey(request, bpk):
    b = Board.objects.get(id=bpk)
    b.likey.add(request.user)
    
    return redirect("board:detail",bpk)

def cancel(request, bpk):
    b = Board.objects.get(id=bpk)
    b.likey.remove(request.user)
    return redirect("board:detail",bpk)
