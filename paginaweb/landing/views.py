from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .models import Post,Users

####/-----------------Vistas-----------------/####



def paginaindex(request):
    articulos = Post.objects.all().order_by('-id')
    return render(request, 'index.html', {'articulos': articulos})


def paginausuario (request):
    return render(request,'usuario.html')

def paginanuevopost (request):
    return render(request,'nuevopost.html')




####/-----------------Register-----------------/####

def registerPage(request):
    register_form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if register_form.is_valid():
            register_form.save()
            return redirect('index')

    
    return render(request, 'users/register.html', {'register_form':register_form})

####/-----------------Login-----------------/####

def loginpage(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate (request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return render(request, 'users/login.html')



    return render(request,'users/login.html')

####/-----------------Logout-----------------/####

def logout_view(request):
    logout(request)

    return redirect('register')

####/-----------------User Modificar-----------------/####

@login_required
def user_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)
            user.save()
            update_session_auth_hash(request, user)  
            return redirect('usuario')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'user_update.html', {'form': form})

####/-----------------User Borrar-----------------/####

@login_required
def delete_account(request):
    if request.method == 'POST':
        
        user = request.user
        user.delete()
        messages.success(request, 'Tu cuenta ha sido eliminada correctamente.')
        return redirect('login')  
    return render(request, 'delete_account.html')

####/-----------------Post-----------------/####

def crear_articulo(request):
            if "user" in request.session:
                  user=request.session['user']
                  logged=True
            else:
                  logged=True
                  user= ""
            return render (request,'nuevopost.html',{'nombre':user,'logged':logged})

def guardararticuloPOST(request):
      if request.method=='POST':
            titlef=request.POST['title']
            contentntf=request.POST['content']
            publicadof=request.POST['publicado']
            post = Post( 
             titulo=titlef,
             contenido=contentntf,
             publicado=publicadof)
            post.save()
            return redirect('index')
      else:
            return HttpResponse("NO SE HA PODIDO CREAR EL ARTICULO")


def buscarTodo(request):
      if "user" in request.session:
            user=request.session['user']
            logged=True
      else:
            logged=False
            user= ""
      # articulos=Post.objects.order_by('id')[:5]
      articulos=Post.objects.all()
      return render (request,'nuevopost.html',{'articulos':articulos,'nombre':user,'logged':logged})


def borrar(request,id):
      articulo=Post.objects.get(pk=id)
      articulo.delete()
      return redirect('buscarTodo')