from django.shortcuts import render

# Create your views here.
def stupidhacks(request):
    return render(request, 'stupidhacks/stupidhacks.html', {})

def submit(request):
    info = request.POST['info']
    print(info)
    return
