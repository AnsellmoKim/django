from multiprocessing import context
from django.shortcuts import render,redirect
from.models import Choice, Topic
# Create your views here.
def index(request):
    t = Topic.objects.all()
    context ={
        'tset' : t
    }
    return render(request,'vote/index.html',context)

def detail(request,tpk):
    t = Topic.objects.get(id=tpk)
    c = t.choice_set.all()
    
    context ={
        't' : t,
        'cset' : c
    }
    return render(request,'vote/detail.html',context)

def vote(request, tpk):
    t = Topic.objects.get(id=tpk)
    if not request.user in t.voter.all():
        t.voter.add(request.user)
        cpk = request.POST.get("ch")
        c = Choice.objects.get(id=cpk)
        c.chnum += 1
        c.save()
    return redirect('vote:detail',tpk)