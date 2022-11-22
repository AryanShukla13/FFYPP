from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .forms import CustomUserForm

# Create your views here.
def home(request):
    return render(request, 'accounts\dashboard.html')

def course(request):
    return render(request, 'accounts\course.html')

def contact(request):
    return HttpResponse('contact')

class SignUpView(View):

    def get(self, request):
        form = CustomUserForm()
        return render(request, "accounts/signup.html", {'form' : form})

    def post(self, request):
        form = CustomUserForm(request.POST or None)

        if form.is_valid():
            user = form.save()
            print(user)
            return render(request, 'accounts\dashboard.html')
        
        return render(request, "accounts/signup.html", {'form' : form})

def login(request):
    return render(request, "accounts/login.html")

def signout(request):
    pass

