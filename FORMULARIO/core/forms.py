from django import forms
from .models import ProduccionDiaria

class ProduccionDiariaForm(forms.ModelForm):
    class Meta:
        model = ProduccionDiaria
        fields = ['producto', 'litros_producidos', 'fecha_produccion', 'turno']
