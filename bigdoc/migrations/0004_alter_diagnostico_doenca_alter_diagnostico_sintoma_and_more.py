# Generated by Django 4.0.3 on 2022-04-08 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bigdoc', '0003_diagnostico_remove_doenca_sintomas_delete_peso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnostico',
            name='doenca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnostico', to='bigdoc.doenca'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='sintoma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnostico', to='bigdoc.sintoma'),
        ),
        migrations.AlterField(
            model_name='doenca',
            name='nome',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='sintoma',
            name='nome',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
