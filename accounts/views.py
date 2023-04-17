from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from coursetable.models import CourseTable
from .forms import CustomUserForm
from django.views.generic import TemplateView
# from django.core.files.storage import FilesSystemStorage

# from django.template import loader
# from django.urls import reverse
# from .models import Accounts

# Create your views here.
def home(request):
    return render(request, 'accounts\dashboard.html')

def edit(request):
    return render(request, 'accounts\edit.html')

# def sheet(request):
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         # fs = FilesSystemStorage()
#         # name = fs.save(uploaded_file.name, uploaded_file)
#         # url = fs.url(name)
#         # print(url)
#     return render(request, 'accounts\sheet.html')

def courseadd(request):
    return render(request, 'accounts\courseadd.html')

def xyz(request):
    return render(request, 'accounts/xyz.html')

def course(request):
    print('file is here')
    courseTableData = CourseTable.objects.all()
    data = {
        "courseTableData" : courseTableData
    }
    return render(request, 'accounts\course.html', data)
    

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

