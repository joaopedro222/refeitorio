from django.shortcuts import render,redirect
from .forms UsuarioForms

# Create your tests here.
def new_aluno(request):
    form = UsuarioForm(request.POST, request.FILES)
    if request.method == "POST":

        if form.is_valid():
            aluno=form.save()
            aluno.save()
            form = UsuarioForm()
    context = {'form': form,}
    return render(request, 'user/new_aluno.html', context)
