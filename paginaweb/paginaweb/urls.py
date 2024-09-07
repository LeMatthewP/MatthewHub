from django.contrib import admin
from django.urls import path
from landing import views
from landing.views import logout_view
from django.contrib.auth.views import LoginView
from landing.views import user_update
from landing.views import delete_account
from landing.views import guardararticuloPOST
from landing.views import crear_articulo



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.paginaindex, name='register'),
    path('index/',views.paginaindex, name='index'),
    path('usuario/',views.paginausuario, name='usuario'),
    path('nuevopost/',views.paginanuevopost, name='nuevopost'),
    path('register/',views.registerPage, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', views.loginpage, name='login'),
    path('update/', user_update, name='user_update'),
    path('delete/', delete_account, name='delete_account'),
    path('guardar-articuloP/', guardararticuloPOST ,name="guardararticuloP"),
    path('crear-articulo/', crear_articulo,name="creararticulo"),
]
