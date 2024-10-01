from django.db import models
from utils.models import BaseModel
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from utils.crew.crew import (
    wrong_answers_crew,
    revision_answers_crew,
    resolutions_crew,
    wrong_answers_by_image_crew,
    difficulty_crew,
)

# Create your models here.


class Question(BaseModel):
    question = models.TextField(
        verbose_name="Questão",
        help_text="Digite a questão"
    )
    correct_answer = models.TextField(
        verbose_name="Resposta correta",
        help_text="Digite a resposta correta"
    )
    wrong_answer_1 = models.CharField(
        verbose_name="Resposta errada 1",
        help_text="Digite a resposta errada 1",
        null=True,
        blank=True,
        editable=False
    )
    wrong_answer_2 = models.CharField(
        verbose_name="Resposta errada 2",
        help_text="Digite a resposta errada 2",
        null=True,
        blank=True,
        editable=False
    )
    wrong_answer_3 = models.CharField(
        verbose_name="Resposta errada 3",
        help_text="Digite a resposta errada 3",
        null=True,
        blank=True,
        editable=False
    )
    wrong_answer_4 = models.CharField(
        verbose_name="Resposta errada 4",
        help_text="Digite a resposta errada 4",
        null=True,
        blank=True,
        editable=False
    )
    difficulty = models.IntegerField(
        verbose_name="Dificuldade",
        help_text="Digite a dificuldade da questão",
        null=True,
        blank=True,
        choices=(
            (1, "Muito Fácil"),
            (2, "Fácil"),
            (3, "Médio"),
            (4, "Difícil"),
            (5, "Muito Difícil"),
        ),
    )
    subject = models.ForeignKey(
        'Subject',
        on_delete=models.CASCADE,
        verbose_name="Matéria",
        help_text="Selecione a matéria da questão"
    )
    year = models.IntegerField(
        verbose_name="Ano",
        help_text="Digite o ano da questão"
    )
    university = models.ForeignKey(
        'University',
        on_delete=models.CASCADE,
        verbose_name="Universidade",
        help_text="Selecione a universidade da questão"
    )
    revision = models.BooleanField(
        verbose_name="Revisão",
        help_text="Marque se a questão precisa de uma revisão",
        default=False
    )
    image = models.ImageField(
        verbose_name="Imagem",
        help_text="Selecione a imagem da questão",
        upload_to="questions",
        null=True,
        blank=True
    )
    resolution = models.TextField(
        verbose_name="Resolução",
        help_text="Digite a resolução da questão",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Questão | {self.question} "

    class Meta:
        verbose_name = "Questão"
        verbose_name_plural = "Questões"
        ordering = ['-created_at']


@receiver(pre_save, sender=Question)
def question_pre_save(sender, instance, **kwargs):
    # Se tiver imagem chama a crew para analisar a imagem.
    if instance.image:
        wrong_answers_by_image = wrong_answers_by_image_crew(
            instance.question, instance.correct_answer, instance.subject.name, instance.image)
        partes = wrong_answers_by_image.split("a)")[1].split("b)")
        parte_a = partes[0].strip()
        partes = partes[1].split("c)")
        parte_b = partes[0].strip()
        partes = partes[1].split("d)")
        parte_c = partes[0].strip()
        parte_d = partes[1].strip()

        instance.wrong_answer_1 = parte_a
        instance.wrong_answer_2 = parte_b
        instance.wrong_answer_3 = parte_c
        instance.wrong_answer_4 = parte_d

        incorrect_answers = [parte_a, parte_b, parte_c, parte_d]

        # Resolução da questão gerado por IA
        resolution = resolutions_crew(
            instance.question, instance.correct_answer, instance.subject.name, incorrect_answers)
        instance.resolution = resolution

        # Nível de dificuldade da questão gerado por IA
        difficulty = difficulty_crew(
            instance.question, instance.correct_answer, instance.subject.name)
        difficulty_level = int(difficulty.split(",")[0].strip("("))
        instance.difficulty = difficulty_level

    # Se não tiver imagem analisa apenas a questão.
    else:
        # if not instance.wrong_answer_1 and not instance.wrong_answer_2 and not instance.wrong_answer_3 and not instance.wrong_answer_4:
        wrong_answers = wrong_answers_crew(
            instance.question, instance.correct_answer, instance.subject.name)
        partes = wrong_answers.split("a)")[1].split("b)")
        parte_a = partes[0].strip()
        partes = partes[1].split("c)")
        parte_b = partes[0].strip()
        partes = partes[1].split("d)")
        parte_c = partes[0].strip()
        parte_d = partes[1].strip()

        instance.wrong_answer_1 = parte_a
        instance.wrong_answer_2 = parte_b
        instance.wrong_answer_3 = parte_c
        instance.wrong_answer_4 = parte_d

        incorrect_answers = [parte_a, parte_b, parte_c, parte_d]

        # Resolução da questão gerado por IA
        resolution = resolutions_crew(
            instance.question, instance.correct_answer, instance.subject.name, incorrect_answers)
        instance.resolution = resolution

        # Nível de dificuldade da questão gerado por IA
        difficulty = difficulty_crew(
            instance.question, instance.correct_answer, instance.subject.name)
        difficulty_level = int(difficulty.split(",")[0].strip("("))
        instance.difficulty = difficulty_level


# ERRO: 2024-09-23 08:09:38,863 - 126935084566208 - __init__.py-__init__:538 - WARNING: Overriding of current TracerProvider is not allowed

# @receiver(post_save, sender=Question)
# def question_post_save(sender, instance, **kwargs):
#     print("Post save signal", instance)
#     if instance.correct_answer:
#         revisor_question = revision_answers_crew(
#             instance.question, instance.correct_answer, instance.subject.name)
#         print("Revisor question", revisor_question)

#         if "Resposta Incorreta" in revisor_question:
#             print("Resposta incorreta")
#             instance.revision = True
#             instance.save()
#         else:
#             print("Resposta correta")


class Subject(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name="Nome",
        help_text="Digite o nome da matéria"
    )
    color = ColorField(
        default='#FFFFFF',
        format="hexa",
        verbose_name="Cor",
        help_text="Digite a cor da matéria",
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name="Descrição",
        help_text="Digite a descrição da matéria",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Matéria | {self.name} "

    class Meta:
        verbose_name = "Matéria"
        verbose_name_plural = "Matérias"
        ordering = ['-created_at']


class University(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name="Nome",
        help_text="Digite o nome da universidade"
    )
    description = models.TextField(
        verbose_name="Descrição",
        help_text="Digite a descrição da universidade",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Universidade | {self.name} "

    class Meta:
        verbose_name = "Universidade"
        verbose_name_plural = "Universidades"
        ordering = ['-created_at']


class Phases(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name="Nome",
        help_text="Digite o nome da fase"
    )
    description = models.TextField(
        verbose_name="Descrição",
        help_text="Digite a descrição da fase",
        blank=True,
        null=True
    )
    difficulty = models.IntegerField(
        verbose_name="Dificuldade",
        help_text="Digite a dificuldade da fase",
        choices=(
            (1, "Muito Fácil"),
            (2, "Fácil"),
            (3, "Médio"),
            (4, "Difícil"),
            (5, "Muito Difícil"),
        ),
    )
    questions = models.ManyToManyField(
        'Question',
        verbose_name="Questões",
        help_text="Selecione as questões da fase",
        blank=True
    )
    coins = models.IntegerField(
        verbose_name="Moedas",
        help_text="Digite a quantidade de moedas da fase",
        default=0
    )
    subject = models.ForeignKey(
        'Subject',
        on_delete=models.CASCADE,
        verbose_name="Matéria",
        help_text="Selecione a matéria da fase"
    )
    university = models.ForeignKey(
        'University',
        on_delete=models.CASCADE,
        verbose_name="Universidade",
        help_text="Selecione a universidade da fase"
    )

    def __str__(self):
        return f"Fase | {self.name} "

    class Meta:
        verbose_name = "Fase"
        verbose_name_plural = "Fases"
        ordering = ['-created_at']
