from django.shortcuts import render,redirect

from .models import *
# Create your views here.


def add_show(request):
    if request.method== "POST":


        data=request.POST
        Name=data.get('Name')
        Gender=data.get('Gender')
        Designation=data.get('Designation')
        

        user.objects.create(
            Name= Name,
            Gender=Gender,
            Designation=Designation,
      

            )
        return redirect('/add')
        
            
    queryset= user.objects.all()
    context={'User':queryset}
       
    return render(request,'addandshow.html',context)


def delete_employee(request, id):
    employee = user.objects.get(id=id)
    employee.delete()
    return redirect('/add')


def update_employee(request, id):
    employee = user.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        employee.Name = data.get('Name')
        employee.Gender = data.get('Gender')
        employee.Designation = data.get('Designation')
        employee.save()
        return redirect('/add')

    context = {'employee': employee}
    return render(request, 'update.html', context)

