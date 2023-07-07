from django.contrib import admin

from .models import CitasMd, Doctor, Paciente, Especialidad
# Register your models here.

admin.site.register(CitasMd)
admin.site.register(Doctor)
admin.site.register(Paciente)
admin.site.register(Especialidad)

