from django import __version__, forms
from .models import Ruta

class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ['nombre', 'origen', 'destino', 'hora_salida', 'precio_pasaje', 'unidad_asignada']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'w-full px-4 py-2.5 rounded-xl border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-900 outline-none transition'}),
            'origen': forms.TextInput(attrs={'class': 'w-full px-4 py-2.5 rounded-xl border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-900 outline-none transition'}),
            'destino': forms.TextInput(attrs={'class': 'w-full px-4 py-2.5 rounded-xl border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-900 outline-none transition'}),
            'hora_salida': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full px-4 py-2.5 rounded-xl border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-900 outline-none transition'}),
            'precio_pasaje': forms.NumberInput(attrs={'step': '0.01', 'class': 'w-full px-4 py-2.5 rounded-xl border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-900 outline-none transition'}),
            'unidad_asignada': forms.Select(attrs={'class': 'w-full px-4 py-2.5 rounded-xl border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-900 outline-none transition'}),
        }