# Generated by Django 3.0.4 on 2020-04-17 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volumbf', '0007_auto_20200417_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentions',
            name='sacral_objects',
            field=models.ManyToManyField(related_name='mentions', to='volumbf.Stones', verbose_name="Сакральны аб'ект"),
        ),
    ]
