import datetime
from django.db import models

# Create your models here.
class grape(models.Model):
    title=models.CharField(max_length=50,verbose_name='Название сорта винограда',help_text='Введите сорт винограда')
    place=models.CharField(max_length=50,verbose_name='Место произрастания',help_text='Введите место произрастания сорта винограда')
    month = (
        ('Январь','Январь '),('Февраль','Февраль '), ('Март','Март '),('Апрель','Апрель '),('Май','Май '),('Июнь','Июнь '),('Июль','Июль '),
        ('Август','Август '),('Сентябрь','Сентябрь '),('Октябрь','Октябрь '),('Ноябрь','Ноябрь '),('Декабрь','Декабрь '),
    )
    date=models.CharField(verbose_name='Время сбора',choices=month,max_length=50, help_text='Введите время сбора урожая винограда')   
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Сорта винограда'
        verbose_name = 'Сорт винограда'
        ordering = ['-date']

class type_wine(models.Model):
    title=models.CharField(max_length=50,verbose_name='Тип вина')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Типы вина'
        verbose_name = 'Тип вина'   
     

class wine_sort(models.Model):
    title=models.CharField(max_length=70,verbose_name='Название вина',help_text='Введите название вина')
    # type=models.CharField(max_length=50,verbose_name='Тип')
    colors = (
        ('Розовое','Розовое '),
        ('Красное','Красное '),
        ('Белое','Белое '),
    )
    color=models.CharField(max_length=50,choices=colors,verbose_name='Цвет')
    b_year=models.IntegerField(verbose_name='Время выдержки в бочках', help_text='в годах')
    bu_month=models.IntegerField(verbose_name='Время выдержки в бутылках', help_text='в месяцах')
    s_grape=models.ForeignKey(grape,on_delete = models.DO_NOTHING,verbose_name='Сорт винограда')
    type1=models.ForeignKey('type_wine',on_delete = models.DO_NOTHING,verbose_name='Тип винограда',null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Сорта вин'

        verbose_name = 'Сорт вина'
        

class bochka(models.Model):
    mesto=models.CharField(max_length=50,verbose_name='Местоположение бочки', help_text='Введите комнату и стеллаж',default='Комната:   |   Стеллаж: ')
    date_izg=models.DateField(verbose_name='Дата изготовления бочки')   
    obyem=models.FloatField(verbose_name='Объем в литрах')
    pusto=models.BooleanField(verbose_name='Бочка заполнена',help_text='Поставьте галочку, если бочка не пуста')
    data_zapolnenya=models.DateField(verbose_name='Дата заполнения бочки',null=True,blank=True)
    sort_vina=models.ForeignKey(wine_sort,on_delete = models.DO_NOTHING,null=True,blank=True,verbose_name='Сорт вина',help_text='Выберите сорт вина')
    def __str__(self):
        return self.mesto
    class Meta:
        verbose_name_plural = 'Бочки'
        verbose_name = 'Бочка'
        ordering = ['-pusto']
        
