from django.contrib import admin
from calculator_osago.models import *

# Register your models here.

class TypeVehicleAdmin(admin.ModelAdmin):
    list_display = ["name", "coefficient", "coefficient_max"]


# Регистрация собственника
class TerritoryAdmin(admin.ModelAdmin):
    list_display = ["name", "coefficient"]

# КБМ
class KBMAdmin(admin.ModelAdmin):
    list_display = ["name", "coefficient"]


# Сведения о ограничении колличества лиц
class LimitationsAdmin(admin.ModelAdmin):
    list_display = ["name", "coefficient"]


# Стаж вождения
class RecordDrivingAdmin(admin.ModelAdmin):
    list_display = ["name", "coefficient"]



# Мощность двигателя (лошадиных сил)
class HPAdmin(admin.ModelAdmin):
    list_display = ["name", "coefficient"]


# прицеп
class TrailerAdmin(admin.ModelAdmin):
    list_display = ["name", "coefficient"]


# Срок страхования
class TermInsuranceAdmin(admin.ModelAdmin):
    list_display = ["name", "coefficient"]



admin.site.register(TypeVehicle, TypeVehicleAdmin)
admin.site.register(Territory, TerritoryAdmin)
admin.site.register(KBM, KBMAdmin)
admin.site.register(Limitations, LimitationsAdmin)
admin.site.register(RecordDriving, RecordDrivingAdmin)
admin.site.register(HP, HPAdmin)
admin.site.register(Trailer, TrailerAdmin)
admin.site.register(TermInsurance, TermInsuranceAdmin)