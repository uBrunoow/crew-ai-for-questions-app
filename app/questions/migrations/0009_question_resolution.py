# Generated by Django 5.1.1 on 2024-09-23 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_alter_question_correct_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='resolution',
            field=models.TextField(blank=True, help_text='Digite a resolução da questão', null=True, verbose_name='Resolução'),
        ),
    ]