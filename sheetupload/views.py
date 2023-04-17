from tablib import Dataset
from .models import Person
from .forms import CustomUserForm
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .resources import PersonResource
from django.views.generic import View
from coursetable.models import CourseTable
import csv
import io
from django.views.decorators.csrf import csrf_exempt
import codecs
import pandas as pd


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

def xyz(request):
    return render(request,'accounts/xyz.html')

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



@csrf_exempt
def studentData(request):
    if request.method == 'POST':
        print("I am called")
        csv_file = request.FILES['file']
        with open(csv_file, ) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                print(row)
        print(csv_file)
        df = pd.read_csv(csv_file, index_col=None, header=0, engine='python' )
        print(df)
        # csv_data = pd.read_csv(
        #     io.StringIO(
        #     csv_file.read().decode("utf-8")
        #     )
        # )
        # for record in csv_data:
        #     print(record)

        # new_file = open(‘my_file.csv’, “rb”)


        # new_file = open(csv_file, 'rt')
        # content = csv.reader(new_file)

        # for row in content :

        #     print(row)

        # another_file = open(csv_file, 'rb')

        # read = csv.reader(codecs.iterdecode(another_file, ‘utf-8’))

        # for row in read :

        # print (row)

        # ifile  = open(csv_file, "rb")
        # read = csv.reader(ifile)
        # for row in read :
        #     print (row) 

        # df = pd.read_csv(csv_file, encoding = 'ISO-8859-1', error_bad_lines = False)
        # print(df)
        return  HttpResponse("Function is working Fine") 
        data = csv_file.read().decode('utf-8')
        print(data)
        # string = io.BytesIO(data)
        # next(string)
        string = data.split('\n')
        for column in csv.reader(string, delimiter = ','):
            print(column)

        return HttpResponse("Function is working Fine") 

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

