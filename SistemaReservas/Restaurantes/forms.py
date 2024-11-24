from django import forms
from .models import Reserva

class SolicitarReservaForm(forms.Form):
    class Meta:
        model = Reserva
        fields = ['fecha_hora', 'num_personas']

    def __init__(self, *args, **kwargs):
        super(SolicitarReservaForm, self).__init__(*args, **kwargs)

        self.fields['fecha_hora'].widget = forms.DateTimeInput(attrs= {
            'type': 'datetime-local',
            'class': 'form-control',
        })
        self.fields['num_personas'].widget = forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 1,
            'max': 15,
        })

class ModificarReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha_hora', 'num_personas']

    def __init__(self, *args, **kwargs):
        super(ModificarReservaForm, self).__init__(*args, **kwargs)

        self.fields['fecha_hora'].widget = forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control',
        })
        self.fields['num_personas'].widget = forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 1,
            'max': 15,
        })
        
    