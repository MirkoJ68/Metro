from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect
from .forms import ReclamoForm, LoginForm
from .models import Usuario, Reclamo, Tren


def solo_admin(funcion):
    def wrapper(request, *args, **kwargs):

        if request.session.get("rol") == "admin":
            return funcion(request, *args, **kwargs)

        return HttpResponseRedirect("/")

    return wrapper

def inicio(request):
    return render(request, "app_trabajo/index.html")


def login(request):

    formulario = LoginForm()
    error = None

    if request.method == "POST":

        formulario = LoginForm(request.POST)

        if formulario.is_valid():

            usuario = formulario.cleaned_data["usuario"]
            clave = formulario.cleaned_data["clave"]

            try:
                usuario_db = Usuario.objects.get(usuario=usuario, clave=clave)
                request.session["usuario_id"] = usuario_db.id
                request.session["usuario"] = usuario_db.usuario
                request.session["rol"] = usuario_db.rol
                return HttpResponseRedirect("/")

            except Usuario.DoesNotExist:
                error = "Usuario o contraseña incorrectos"

    return render(
        request,
        "app_trabajo/login.html",
        {
            "formulario": formulario,
            "error": error,
        }
    )


def logout(request):
    request.session.flush()
    return HttpResponseRedirect("/")


def horarios(request):
    return render(request, "app_trabajo/horarios.html")


def estaciones(request):
    return render(request, "app_trabajo/estaciones.html")


def servicios(request):
    return render(request, "app_trabajo/servicios.html")

@solo_admin
def trenes(request):
    lista_trenes = Tren.objects.all()

    return render(
        request,
        "app_trabajo/trenes.html",
        {
            "trenes": lista_trenes
        }
    )

def reclamos(request):

    formulario = ReclamoForm()

    if request.method == "POST":

        formulario = ReclamoForm(request.POST)

        if formulario.is_valid():

            Reclamo.objects.create(
                nombre=formulario.cleaned_data["nombre"],
                email=formulario.cleaned_data["email"],
                tipo=formulario.cleaned_data["tipo"],
                estacion=formulario.cleaned_data["estacion"],
                fecha=formulario.cleaned_data["fecha"],
                descripcion=formulario.cleaned_data["descripcion"],
            )

            return render(
                request,
                "app_trabajo/reclamo_enviado.html"
            )

    return render(
        request,
        "app_trabajo/reclamos.html",
        {
            "formulario": formulario
        }
    )