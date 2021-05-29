from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Pessoa
from .forms import FormPessoa

#@login_required
def lista_pessoa(resquest):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa.html', {'pessoas': pessoas})

#@login_required
def nova_pessoa(request, id):
    form = FormPessoa(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_pessoa')
    return render(request, 'form_pessoa.html', {'form': form})

#@login_required
def atualiza_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    form = FormPessoa(request.POST or None, request.FILES or None, instance=pessoa)
    if form.is_valid():
        form.save()
        return redirect('lista_pessoa')
    return render(request, 'form_pessoa.html', {'form': form})

#@login_required
def deleta_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('lista_pessoa')
    return render(render, 'confirma_deleta_pessoa.html')