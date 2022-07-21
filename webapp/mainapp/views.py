from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contacts
from .forms import ContactsForm
from django.views.generic import DetailView,UpdateView,DeleteView

# Create your views here.
class DetailViewTest(DetailView):
    model=Contacts
    template_name = 'mainapp/details_view.html'
    context_object_name = 'contact'

class DetailUpdateViewTest(UpdateView):
    model = Contacts
    template_name = 'mainapp/create.html'

    form_class = ContactsForm

class DetailDeleteViewTest(DeleteView):
    model = Contacts
    success_url = '/'
    template_name = 'mainapp/delete.html'


def index(request):
    con = Contacts.objects.all()
    return render(request,'mainapp/index.html',{'Contact': con })

def about(request):
    return render(request,'mainapp/about.html')

def create(request):
    error =' '
    if request.method =='POST':
        form=ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='Не верная форма'

    form = ContactsForm()
    date={
        'form':form,
        'error': error
    }


    return render(request,'mainapp/create.html',date)
