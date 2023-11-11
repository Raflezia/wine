import datetime
from django.db import models

# Create your models here.
class grape(models.Model):
    title=models.CharField(max_length=50,verbose_name='Название')
    place=models.CharField(max_length=50,help_text='place',null=True, blank=True, )
    date=models.DateField()   
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Сорта винограда'
        verbose_name = 'Сорт винограда'
        ordering = ['-title']
class wine_sort(models.Model):
    title=models.CharField(max_length=50,verbose_name='hfghfg')
    type=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    b_year=models.DurationField()
    bu_month=models.DurationField()
    s_grape=models.ForeignKey(grape,on_delete = models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Сорта вин'
        verbose_name = 'Сорт вина'
        ordering = ['-title']
class bochka(models.Model):
    mesto=models.CharField(max_length=50,verbose_name='hfghfg')
    date_izg=models.DateField()   
    obyem=models.FloatField()
    pusto=models.BooleanField()
    data_zapolnenya=models.DateField()
    sort_vina=models.ForeignKey(wine_sort,on_delete = models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Бочки'
        verbose_name = 'Бочка'
        ordering = ['-data_zapolnenya']