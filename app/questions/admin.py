# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Question, Subject, University, Phases


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'question',
        'correct_answer',
        'wrong_answer_1',
        'wrong_answer_2',
        'wrong_answer_3',
        'wrong_answer_4',
        'difficulty',
        'subject',
        'year',
        'university',
        'revision',
        'image',
        'resolution',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'subject',
        'university',
        'revision',
    )
    date_hierarchy = 'created_at'


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'name',
        'color',
        'description',
    )
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'name', 'description')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Phases)
class PhasesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'name',
        'description',
        'difficulty',
        'coins',
        'subject',
        'university',
    )
    list_filter = ('created_at', 'updated_at', 'subject', 'university')
    raw_id_fields = ('questions',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'
