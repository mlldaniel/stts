# Generated by Django 3.1.14 on 2022-02-27 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speech_results', '0002_auto_20220226_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechresults',
            name='result',
            field=models.JSONField(verbose_name='Result from Speech Api'),
        ),
    ]
