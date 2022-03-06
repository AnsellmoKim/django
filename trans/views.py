from fnmatch import translate
from multiprocessing import context
from django.shortcuts import render
from googletrans import Translator
# Create your views here.
def index(request):
    context = {}
    if request.method=="POST":
        t = request.POST.get("to")
        b = request.POST.get('bf')
        f = request.POST.get('fr')
        translator = Translator()
        af = translator.translate(b , src = f, dest = t)
        context.update({
            'af' : af.text,
            "bf" : b,
            "fr" : f,
            "to" : t
         })
    return render(request,"trans/index.html",context)