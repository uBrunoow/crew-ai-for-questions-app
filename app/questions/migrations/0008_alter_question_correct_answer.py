# Generated by Django 5.1.1 on 2024-09-23 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.TextField(help_text='Digite a resposta correta', verbose_name='Resposta correta'),
        ),
    ]
