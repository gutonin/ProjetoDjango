from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
#Decorator que Não funciona
#from django.contrib.auth.decorators import login_required

#from clientes.models import Pessoa
#from clientes.forms import FormPessoa

#@login_required
def home(request):
    return render(request, 'home.html')

def my_logout(request):
    return redirect('home')