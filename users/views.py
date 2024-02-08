from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

#Gera a página de registro e os formulários necessários além da lógica presente no processo de registro
def register(request):
    
    #Cria a condicional para caso um formulário seja enviado, confere se ele é válido
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #Se ele for válido, salva o formulário informa o usuário, e redireciona para o login
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'A conta foi criada com sucesso!')
            return redirect('login')
        
    #Do contrário mostra ao usuário a página de registro.        
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html', {'form': form})

#Cria a página de perfil que so pode ser acessada caso o usuário esteja logado
@login_required
def profile(request):
    if request.method =="POST":
        #puxa os formulários de update de foto e update de informações de perfil do forms.py e permite o usuário postar modificações
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        #salva as alterações caso as mesmas sejam válidas
        if u_form.is_valid():
            u_form.save()
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'A conta foi atualizada com sucesso!')
            return redirect('profile')
    
    else:
        
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    #gera o contexto com os formulários e passa para o profile.html
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'users/profile.html', context)