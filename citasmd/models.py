from django.db import models

# Create your models here.

class Paciente(models.Model):
    id_paciente = models.IntegerField(null=True)
    Pac_nomb= models.CharField(max_length=20, null=True)
    Pac_Apellido = models.CharField(max_length=20, null=True)
    Pac_edad = models.IntegerField(null=True)
    correo = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.id_paciente} {self.Pac_nomb} {self.Pac_Apellido}'

class Especialidad(models.Model):
    nom_especialidad = models.CharField(max_length=20, null=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.nom_especialidad}'
class Doctor(models.Model):
    id_doctor = models.IntegerField(null=True)
    Doc_nomb= models.CharField(max_length=20, null=True)
    Doc_Apellido = models.CharField(max_length=20, null=True)
  #  especialidad = models.CharField(max_length=20, null=True)
    Doc_direccion = models.CharField(max_length=20, null=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.id_doctor} {self.Doc_nomb} {self.Doc_Apellido}'

class CitasMd(models.Model):
    fecha_cita = models.DateField(null=True)
    activo = models.BooleanField(default=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'id: {self.fecha_cita}'