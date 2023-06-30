from django.contrib import admin

from .models import CitasMd, Doctor, Paciente
# Register your models here.

admin.site.register(CitasMd)
admin.site.register(Doctor)
admin.site.register(Paciente)

