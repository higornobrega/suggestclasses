# Generated by Django 2.1.5 on 2019-08-26 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190825_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentecurricular',
            name='requisitos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.ComponenteCurricular'),
        ),
    ]
