from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from citasmd.models import CitasMd
def mostrar_citasmd(request):
    cantidad_citasmd = CitasMd.objects.count()
    pagina = loader.get_template('citasmd.html')
    lista_citasmds =  CitasMd.objects.all()
    datos = {'cantidad':cantidad_citasmd, 'citasmds':lista_citasmds}
    return HttpResponse(pagina.render(datos,request))
