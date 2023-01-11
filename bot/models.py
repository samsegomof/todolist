from django.core.validators import MinLengthValidator
from django.db import models

from core.models import User


class TgUser(models.Model):
    tg_chat_id = models.BigIntegerField(verbose_name='ID чата')
    tg_user_id = models.BigIntegerField(verbose_name='ID пользователя')
    tg_username = models.CharField(max_length=32, validators=[MinLengthValidator(5)])
    user = models.ForeignKey('core.User', verbose_name='Пользователь', on_delete=models.PROTECT, null=True, blank=True)
    verification_code = models.CharField(max_length=10, null=True, blank=True, verbose_name='Верификационный код')
