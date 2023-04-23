from django.shortcuts import redirect, render
from .models import Student
# Create your views here.


def index(request):
    data = Student.objects.all()
    print(data)
    context = {'data': data}
    return render(request, 'index.html', context)


def insertData(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        
        print(name, email, age, gender)
        query = Student(name=name, email=email, age=age, gender=gender)
        query.save()
        return redirect("/")
    return render(request, 'index.html')
