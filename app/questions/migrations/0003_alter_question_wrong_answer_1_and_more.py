# Generated by Django 5.1.1 on 2024-09-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_alter_question_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='wrong_answer_1',
            field=models.CharField(blank=True, help_text='Digite a resposta errada 1', null=True, verbose_name='Resposta errada 1'),
        ),
        migrations.AlterField(
            model_name='question',
            name='wrong_answer_2',
            field=models.CharField(blank=True, help_text='Digite a resposta errada 2', null=True, verbose_name='Resposta errada 2'),
        ),
        migrations.AlterField(
            model_name='question',
            name='wrong_answer_3',
            field=models.CharField(blank=True, help_text='Digite a resposta errada 3', null=True, verbose_name='Resposta errada 3'),
        ),
        migrations.AlterField(
            model_name='question',
            name='wrong_answer_4',
            field=models.CharField(blank=True, help_text='Digite a resposta errada 4', null=True, verbose_name='Resposta errada 4'),
        ),
    ]
