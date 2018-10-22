from django.db import models

# Create your models here.
# тип тс
class TypeVehicle(models.Model):
    name = models.CharField(verbose_name=u'Тип ТС:', max_length=255)
    coefficient = models.CharField(max_length=10, null=True, blank=True)
    coefficient_max = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = u'Тип ТС'
        verbose_name_plural = u'Тип ТС'

    def __str__(self):
        return self.name

# Регистрация собственника
class Territory(models.Model):
    name = models.CharField(max_length=255)
    coefficient = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = u'Прописка собственника'
        verbose_name_plural = u'Прописка собственника'

    def __str__(self):
        return self.name

# КБМ
class KBM(models.Model):
    name = models.CharField(max_length=10)
    coefficient = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = u'КБМ'
        verbose_name_plural = u'КБМ'

    def __str__(self):
        return self.name

# Сведения о ограничении колличества лиц
class Limitations(models.Model):
    name = models.CharField(max_length=255)
    coefficient = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = u'Колличество лиц'
        verbose_name_plural = u'Колличество лиц'

    def __str__(self):
        return self.name

# Стаж вождения
class RecordDriving(models.Model):
    name = models.CharField(max_length=255)
    coefficient = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = u'Стаж вождения'
        verbose_name_plural = u'Стаж вождения'

    def __str__(self):
        return self.name


# Мощность двигателя (лошадиных сил)
class HP(models.Model):
    name = models.CharField(max_length=255)
    coefficient = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = u'Мощность двигателя'
        verbose_name_plural = u'Мощность двигателя'

    def __str__(self):
        return self.name

# прицеп
class Trailer(models.Model):
    name = models.CharField(max_length=255)
    coefficient = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = u'Прицеп'
        verbose_name_plural = u'Прицеп'

    def __str__(self):
        return self.name

# Срок страхования
class TermInsurance(models.Model):
    name = models.CharField(max_length=255)
    coefficient = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = u'Период страхования'
        verbose_name_plural = u'Период страхования'

    def __str__(self):
        return self.name

class Osago(models.Model):
    type = models.ForeignKey(TypeVehicle, verbose_name=u'Тип ТС:', default='1', on_delete=models.CASCADE)
    territory = models.ForeignKey(Territory, verbose_name=u'Регион:', default='1', on_delete=models.CASCADE)
    kbm = models.ForeignKey(KBM, verbose_name=u'Стаж безаварийной езды:', default='1', on_delete=models.CASCADE)
    limitations = models.ForeignKey(Limitations, verbose_name=u'Лица, допущенные к управлению:', default='1', on_delete=models.CASCADE)
    recordDriving = models.ForeignKey(RecordDriving, verbose_name=u'Стаж вождения:', default='1', on_delete=models.CASCADE)
    hp = models.ForeignKey(HP, verbose_name=u'Мощность двигателя, л.с.:', default='1', on_delete=models.CASCADE)
    trailer = models.ForeignKey(Trailer, verbose_name=u'Наличие прицепа:', default='1', on_delete=models.CASCADE)
    terminsurance = models.ForeignKey(TermInsurance, verbose_name=u'Период страхования:', default='1', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Сводные данные'
        verbose_name_plural = u'Сводные данные'


    def __str__(self):
        return self.type