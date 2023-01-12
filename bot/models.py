from django.core.validators import MinLengthValidator
from django.db import models

from core.models import User


class TgUser(models.Model):
    chat_id = models.BigIntegerField(verbose_name='id чата', null=True)
    user_ud = models.BigIntegerField(verbose_name='id пользователя', null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT, null=True, blank=True)
    verification_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='Код верификации')

