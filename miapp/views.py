from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from miapp.models import Estudiante

# Create your views here.
layout = """"""
def integrantes(request):
    integrantes = ['Jose Flores Chamba','Edson Alva Chanta','Miguel Angel Motta Mendoza']
    return render(request, 'integrantes.html', {
        'titulo':'Integrantes del proyecto',
        'integrantes':integrantes
    })

def saludo(request):
    return render(request, 'saludo.html', {
        'titulo':'Bienvenidos',
        'mensaje':'Proyecto para la Unidad de Competencia 04 (UC04)'
    })

def crear_estudiante(request):
    estudiante1 = Estudiante(
    codigo = "1452632145",
    dni = "75426121",
    nombre = "Juan",
    apepat = "Perez",
    apemat = "Gonzales",
    direccion = "Magdanela Av. Los incas 451",
    telefono = "965412751",
    estado = "A"
    )
    estudiante2 = Estudiante(
    codigo = "1123458676",
    dni = "76426629",
    nombre = "Pedro",
    apepat = "Rodriguez",
    apemat = "Juarez",
    direccion = "Chosica Cuadra 12",
    telefono = "999345666",
    estado = "A"
    )
    estudiante3 = Estudiante(
    codigo = "1825538689",
    dni = "75554311",
    nombre = "Leonel",
    apepat = "Ramirez",
    apemat = "Gonzales",
    direccion = "Villa María Jr. San Pedro",
    telefono = "944789344",
    estado = "A"
    )
    estudiante4 = Estudiante(
    codigo = "1822138559",
    dni = "71255610",
    nombre = "Jaime",
    apepat = "Duarte",
    apemat = "Uribe",
    direccion = "Magdanela Jr. n° 1414",
    telefono = "912366769",
    estado = "A"
    )
    estudiante5 = Estudiante(
    codigo = "1823338679",
    dni = "75554311",
    nombre = "Julian",
    apepat = "Alvarez",
    apemat = "Serna",
    direccion = "Villa El Salvador Calle 15",
    telefono = "956345993",
    estado = "A"
    )
    estudiante1.save()
    estudiante2.save()
    estudiante3.save()
    estudiante4.save()
    estudiante5.save()
    return HttpResponse (f"<h1>Estudiante registrado:</h1> "+
    f"<br> <b>Código:</b> {estudiante1.codigo} <br> <b>DNI:</b> {estudiante1.dni} <br> <b>Nombre:</b> {estudiante1.nombre} <br> "+
    f"<b>Apellido paterno:</b> {estudiante1.apepat} <br> <b>Apellido materno:</b> {estudiante1.apemat} <br><b>Dirección:</b> "+
    f" {estudiante1.direccion} <br> <b>Telefono:</b> {estudiante1.telefono} <br> <b>Estado:</b> {estudiante1.estado}")


