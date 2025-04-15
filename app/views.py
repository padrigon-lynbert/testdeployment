from django.shortcuts import render

# Create your views here.
def render_app(request):
    return render(request, 'showpage.html')
