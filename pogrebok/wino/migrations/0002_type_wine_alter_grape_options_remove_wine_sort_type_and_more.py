# Generated by Django 4.2.7 on 2023-11-12 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wino', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='type_wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Вид вина')),
            ],
            options={
                'verbose_name': 'Тип вина',
                'verbose_name_plural': 'Типы вина',
            },
        ),
        migrations.AlterModelOptions(
            name='grape',
            options={'ordering': ['-date'], 'verbose_name': 'Сорт винограда', 'verbose_name_plural': 'Сорта винограда'},
        ),
        migrations.RemoveField(
            model_name='wine_sort',
            name='type',
        ),
        migrations.AlterField(
            model_name='bochka',
            name='pusto',
            field=models.BooleanField(verbose_name='Бочка заполнена'),
        ),
        migrations.AlterField(
            model_name='grape',
            name='date',
            field=models.DateField(help_text='Введите время сбора урожая винограда', verbose_name='Время сбора'),
        ),
        migrations.AlterField(
            model_name='grape',
            name='place',
            field=models.CharField(help_text='Введите место произрастания сорта винограда', max_length=50, verbose_name='Место произрастания'),
        ),
        migrations.AlterField(
            model_name='grape',
            name='title',
            field=models.CharField(help_text='Введите сорт винограда', max_length=50, verbose_name='Название сорта винограда'),
        ),
        migrations.AddField(
            model_name='wine_sort',
            name='type1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wino.type_wine', verbose_name='тип винограда'),
        ),
    ]
