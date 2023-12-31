# Generated by Django 4.2.7 on 2023-11-12 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wino', '0002_type_wine_alter_grape_options_remove_wine_sort_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bochka',
            name='date_izg',
            field=models.DateField(verbose_name='Дата изготовления бочки'),
        ),
        migrations.AlterField(
            model_name='bochka',
            name='mesto',
            field=models.CharField(default='Комната:   |   Стеллаж: ', help_text='Введите комнату и стеллаж', max_length=50, verbose_name='Местоположение бочки'),
        ),
        migrations.AlterField(
            model_name='bochka',
            name='pusto',
            field=models.BooleanField(help_text='Поставьте галочку, если бочка не пуста', verbose_name='Бочка заполнена'),
        ),
        migrations.AlterField(
            model_name='bochka',
            name='sort_vina',
            field=models.ForeignKey(help_text='Выберите сорт вина', on_delete=django.db.models.deletion.DO_NOTHING, to='wino.wine_sort', verbose_name='Сорт вина'),
        ),
        migrations.AlterField(
            model_name='type_wine',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Тип вина'),
        ),
        migrations.AlterField(
            model_name='wine_sort',
            name='b_year',
            field=models.IntegerField(help_text='в годах', verbose_name='Время выдержки в бочках'),
        ),
        migrations.AlterField(
            model_name='wine_sort',
            name='bu_month',
            field=models.IntegerField(help_text='в месяцах', verbose_name='Время выдержки в бутылках'),
        ),
        migrations.AlterField(
            model_name='wine_sort',
            name='color',
            field=models.CharField(choices=[('Р', 'Розовое '), ('К', 'Красное '), ('Б', 'Белое ')], max_length=50, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='wine_sort',
            name='s_grape',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wino.grape', verbose_name='Сорт винограда'),
        ),
        migrations.AlterField(
            model_name='wine_sort',
            name='title',
            field=models.CharField(help_text='Введите название вина', max_length=70, verbose_name='Название вина'),
        ),
        migrations.AlterField(
            model_name='wine_sort',
            name='type1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wino.type_wine', verbose_name='Тип винограда'),
        ),
    ]
