# Generated by Django 4.2.7 on 2023-11-11 13:15

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
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Вид вина')),
            ],
            options={
                'verbose_name': 'Тип вина',
                'verbose_name_plural': 'Типы вина',
            },
        ),
        migrations.RemoveField(
            model_name='wine_sort',
            name='type',
        ),
        migrations.DeleteModel(
            name='bochka',
        ),
        migrations.AddField(
            model_name='wine_sort',
            name='type1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wino.type_wine', verbose_name='тип винограда'),
        ),
    ]