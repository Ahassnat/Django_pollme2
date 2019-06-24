from django.shortcuts import render

# Create your views here.
def poll_list(request):
    return render(request, 'polls/list.html')

def about(request):
    return render(request,'polls/about.html')
