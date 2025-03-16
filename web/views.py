from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, '404.html')
def admin_home(request):
    return render (request, 'admin_404.html')
def about(request):
    return render (request, 'about.html')
def table(request):
    return render (request, 'table.html')
def team(request):
    return render (request, 'team.html')
def widget(request):
    return render (request, 'widget.html')
def blank(request):
    return render (request, 'blank.html')
def button(request):
    return render (request, 'button.html')
def chart(request):
    return render (request, 'chart.html')
def contact(request):
    return render (request, 'contact.html')
def courses(request):
    return render (request, 'courses.html')
def element(request):
    return render (request, 'element.html')
def form(request):
    return render (request, 'form.html')
def index(request):
    return render (request, 'index.html')
def signin(request):
    return render (request, 'signin.html')
def signup(request):
    return render (request, 'signup.html')
def testimonial(request):
    return render (request, 'testimonial.html')
def typography(request):
    return render (request, 'typography.html')