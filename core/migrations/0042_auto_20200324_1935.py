# Generated by Django 3.0.2 on 2020-03-24 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_auto_20200324_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='docente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Docente'),
        ),
    ]
