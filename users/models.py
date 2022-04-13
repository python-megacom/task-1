from __future__ import annotations

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ggettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Почта'), unique=True)
    full_name = models.CharField(_('ФИО'), max_length=255)

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self):
        return self.full_name


class YearOfStudyChoices(models.IntegerChoices):
    FRESHMAN = 1, 'freshman'
    SOPHOMORE = 1, 'sophomore'
    JUNIOR = 1, 'junior'
    SENIOR = 1, 'senior'


class Student(models.Model):
    user = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
        related_name='student',
        primary_key=True,
        verbose_name=_('Пользователь'),
    )
    year_of_study = models.SmallIntegerField(
        _('Год обучения'),
        choices=YearOfStudyChoices.choices,
        default=YearOfStudyChoices.FRESHMAN,
    )

    class Meta:
        verbose_name = _('Студент')
        verbose_name_plural = _('Студенты')


class Teacher(models.Model):
    user = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
        related_name='teacher',
        primary_key=True,
        verbose_name=_('Пользователь'),
    )

    class Meta:
        verbose_name = _('Преподаватель')
        verbose_name_plural = _('Преподаватели')
