from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Servidor
from .forms import ServidorForm, ValidForm
from django.core.paginator import Paginator

# Create your views here.
def inicio(request):
    return render(request, 'index.html')   

def cadastrar(request):
    if request.method == 'GET':
        user = Servidor.objects.all()
        form = ValidForm()
        context = {
            'form': form,
            'user': user,
        }
        return render(request, 'cadastro.html', context=context)
    
    else:
        form2 = ServidorForm(request.POST, request.FILES)
        form = ValidForm(request.POST, request.FILES)
        if form2.is_valid():    
            form = ValidForm()
            form2.save()
            return redirect('lista')
        else: 
            user = Servidor.objects.all()
            context = {
                'form': form,
                'user': user,
                'form2': form2,
            }
            return render(request, 'cadastro.html', context = context)

def listar(request):
    server = Servidor.objects.all()
    search = request.GET.get('search')
    if search:
        server = Servidor.objects.filter(cpf_icontains=search)
        context = {'server': server}
        return render(request, 'lista.html', context)
    context ={
        'server': server
    }
    return render(request, 'lista.html', context)

