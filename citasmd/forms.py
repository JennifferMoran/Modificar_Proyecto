from django.forms import ModelForm, EmailInput
from citasmd.models import CitasMd

class CitasMdFormulario(ModelForm):
    class Meta:
        model = CitasMd
        fields = ('fecha_cita', 'activo', 'doctor', 'paciente')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }
