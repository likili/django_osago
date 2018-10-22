from django.shortcuts import render
from django.contrib import messages
from calculator_osago.forms import OsagoModelForm
from calculator_osago.models import *

# Create your views here.


# подсчет стоимости полиса
def osago_apply(request):
    print(request)
    if request.method == "POST":
        form = OsagoModelForm(request.POST)
        if form.is_valid():
            tb = int(TypeVehicle.objects.get(name=form.clean()['type']).coefficient)
            kt = int(Territory.objects.get(name=form.clean()['territory']).coefficient)
            kbm = int(KBM.objects.get(name=form.clean()['kbm']).coefficient)
            ko = int(Limitations.objects.get(name=form.clean()['limitations']).coefficient)
            kvc = int(RecordDriving.objects.get(name=form.clean()['recordDriving']).coefficient)
            km = int(HP.objects.get(name=form.clean()['hp']).coefficient)
            kpr = int(Trailer.objects.get(name=form.clean()['trailer']).coefficient)
            ks = int(TermInsurance.objects.get(name=form.clean()['terminsurance']).coefficient)
            print(form.clean())
            messages.success(request, "Стоимость страховаого полиса составит: {}".format(tb*kt*kbm*ko*kvc*km*kpr*ks))
            return render(request, 'osago/list.html', {'form': form})
    else:
        form = OsagoModelForm()
    return render(request, 'osago/list.html', {'forms': form})

def index(request):
    return render(request, 'index.html')