from multiprocessing import context
from django.shortcuts import render,redirect
from.models import Book
# Create your views here.
def index(request):
    b = request.user.book_set.all()
    context = {
        'bset' : b
    }
    return render(request,'book/index.html',context)

def create(request):
    if request.method == "POST":
        im = bool(request.POST.get('im'))
        sn = request.POST.get('sn')
        su = request.POST.get('su')
        Book(user = request.user , site_name = sn, site_url = su, impo = im).save()
        return redirect("book:index")
    return render(request,"book/create.html")