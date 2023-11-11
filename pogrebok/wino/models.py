import datetime
from django.db import models

# Create your models here.
class grape(models.Model):
    title=models.CharField(max_length=50,verbose_name='Название сорта винограда')
    place=models.CharField(max_length=50,null=True, blank=True,verbose_name='Место произрастания')
    date=models.DateField(verbose_name='Время сбора',help_text='place')   
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Сорта винограда'
        verbose_name = 'Сорт винограда'
        ordering = ['-title']

class type_wine(models.Model):
    title=models.CharField(max_length=50,verbose_name='Вид вина')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Типы вина'
        verbose_name = 'Тип вина'   
     

class wine_sort(models.Model):
    title=models.CharField(max_length=50,verbose_name='Название вина')
    
    # type=models.CharField(max_length=50,verbose_name='Тип')
    color=models.CharField(max_length=50,verbose_name='Цвет')
    b_year=models.DurationField(verbose_name='Время выдержки в бочках', help_text='в годах')
    bu_month=models.DurationField(verbose_name='Время выдержки в бутылках', help_text='в месяцах')
    s_grape=models.ForeignKey(grape,on_delete = models.CASCADE,verbose_name='Сорт винограда')
    type1=models.ForeignKey('type_wine',on_delete = models.CASCADE,verbose_name='тип винограда',blank=True, null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Сорта вин'
        verbose_name = 'Сорт вина'
        ordering = ['-title']

class bochka(models.Model):
    mesto=models.CharField(max_length=50,verbose_name='')
    date_izg=models.DateField(verbose_name='Дата изготовления')   
    obyem=models.FloatField(verbose_name='Объем')
    pusto=models.BooleanField(verbose_name='Пустота')
    data_zapolnenya=models.DateField(verbose_name='Дата заполнения бочки')
    sort_vina=models.ForeignKey(wine_sort,on_delete = models.CASCADE,verbose_name='Сорт вина')
    def __str__(self):
        return self.mesto
    class Meta:
        verbose_name_plural = 'Бочки'
        verbose_name = 'Бочка'
        ordering = ['-data_zapolnenya']
