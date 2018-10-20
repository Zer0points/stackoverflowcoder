from django.shortcuts import render
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(1, os.path.realpath(os.path.pardir))

from generateStupidCode import generateStupidCode

global gList
gList = []

# Create your views here.
def stupidhacks(request):
    return render(request, 'stupidhacks/stupidhacks.html', {})

def submit(request):

    if request.method == 'POST':
        return
        # info = request.POST['info']
        # print(info)
        # args = {'info': generateStupidCode([info])}
        # return render(request, 'stupidhacks/stupidhacks.html', args)
    else:
        info = request.GET['info']
        print(info)
        answer = generateStupidCode([info])
        gList.append(answer)
        args = {'answers': generateStupidCode([info])}
        return render(request, 'stupidhacks/stupidhacks.html', args)
