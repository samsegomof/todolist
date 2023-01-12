from django.core.validators import MinLengthValidator
from django.db import models

from core.models import User


# class TgUser(models.Model):
#     tg_chat_id = models.BigIntegerField(verbose_name='ID чата')
#     tg_user_id = models.BigIntegerField(verbose_name='ID пользователя')
#     tg_username = models.CharField(max_length=32, validators=[MinLengthValidator(5)])
#     user = models.ForeignKey('core.User', verbose_name='Пользователь', on_delete=models.PROTECT, null=True, blank=True)
#     verification_code = models.CharField(max_length=10, null=True, blank=True, verbose_name='Верификационный код')

class TgUser(models.Model):
    chat_id = models.BigIntegerField(verbose_name='id чата')
    user_ud = models.BigIntegerField(verbose_name='id пользователя')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT, null=True, blank=True)
    verification_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='Код верификации')

