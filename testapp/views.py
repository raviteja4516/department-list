from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Department,Student

def home(request):
    return render(request,"testapp/home.html")

def application(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST["name"],
            email = request.POST["email"],
            department = request.POST["department"],
            mobile = request.POST["mobile"],
        )
        return HttpResponseRedirect(reverse("testapp:home"))
    return render(request, "testapp/apply.html")


def index(request):
    latest_department_list = Department.objects.order_by('-pub_date')[:5]
    context = {'latest_department_list': latest_department_list}
    return render(request, 'testapp/index.html', context)

def detail(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    return render(request, 'testapp/detail.html', {'department': department})

def detailing(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    return render(request, 'testapp/detailing.html', {'department': department})
