from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import One, Two ,Login, One

from .form import LoginForm, OneForm

from django.views.generic.list import ListView

from django.urls import reverse


from django.views.generic.edit import CreateView


from django.views.generic.base import TemplateView


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index1(request):
    objectList =  Login.objects.all()

    seconddict = {"login": objectList}

    return render(request,'demoapp/home.html',seconddict)

def login(request):

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():
            username =  form.cleaned_data['username']
            password = form.cleaned_data['password']

            login = Login()
            login.username = username
            login.password = password
            login.save()
            return HttpResponse("Added")
        else:
            return HttpResponse("Invalid")


        return HttpResponse("Form submitted")
    else:
        form =  LoginForm()
        dict = {"form" : form}
        return render(request,'demoapp/form.html',dict)

def oneform(request):

    if request.method =='POST':

        form = OneForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            dob = form.cleaned_data['dob']

            form1 = One()
            form1.name = name
            form1.age= age
            form1.dob = dob
            form1.save()
            return HttpResponse("Added")
        else:
            return HttpResponse("Invalid")

    else:
        form =  OneForm()
        dict = {"form" : form}
        return render(request,'demoapp/form.html',dict)



class Dataview(TemplateView):

    template_name = "demoapp/tempview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['values']= One.objects.all()
        return context


class OneListView(ListView):
    model = One
    paginate_by = 5
    ordering = ['dob']




class OneCreate(CreateView):
    model = One
    fields = ['name','age','dob']
    success_url = 'demoapp/listview/'




