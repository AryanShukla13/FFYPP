from django.shortcuts import render
from .models import Person
from .resources import PersonResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse


from django.views.generic import View
from coursetable.models import CourseTable
from .forms import CustomUserForm
# from django.views.generic import TemplateView

def home(request):
    return render(request, 'accounts\dashboard.html')

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']

        if not new_person.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'upload.html')

        imported_data = dataset.load(new_person.read(),format ='xlsx')
        for data in imported_data:
            value = Person(
                data[0],
                data[1],
                data[2],
                data[3]
                )
            value.save()
    return render(request,'upload.html')

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


def course(request):
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

