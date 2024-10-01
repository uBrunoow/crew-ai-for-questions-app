# Generated by Django 4.2.16 on 2024-09-23 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0013_phases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phases',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 'Muito Fácil'), (2, 'Fácil'), (3, 'Médio'), (4, 'Difícil'), (5, 'Muito Difícil')], help_text='Digite a dificuldade da fase', verbose_name='Dificuldade'),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.IntegerField(blank=True, choices=[(1, 'Muito Fácil'), (2, 'Fácil'), (3, 'Médio'), (4, 'Difícil'), (5, 'Muito Difícil')], help_text='Digite a dificuldade da questão', null=True, verbose_name='Dificuldade'),
        ),
    ]