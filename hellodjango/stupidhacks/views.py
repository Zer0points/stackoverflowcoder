from django.shortcuts import render
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(1, os.path.realpath(os.path.pardir))

from generateStupidCode import generateStupidCode


# Create your views here.
def stupidhacks(request):
    return render(request, 'stupidhacks/stupidhacks.html', {})

def submit(request):
    info = request.POST['info']
    print(info)
    print(generateStupidCode([info]))
    return render(request, 'stupidhacks/stupidhacks.html', {})
