from calculator_osago.models import Osago
from django import forms

class OsagoModelForm(forms.ModelForm):
    class Meta:
        model = Osago
        fields = ['type',
                  'territory',
                  'kbm',
                  'limitations',
                  'recordDriving',
                  'hp',
                  'trailer',
                  'terminsurance']