from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.crypto import get_random_string


class TgUser(models.Model):
    chat_id = models.BigIntegerField(verbose_name='id чата', null=True)
    user_ud = models.BigIntegerField(verbose_name='id пользователя', null=True)
    tg_username = models.CharField(max_length=32, validators=[MinLengthValidator(5)])
    user = models.ForeignKey('core.User', verbose_name='Пользователь', on_delete=models.PROTECT, null=True, blank=True)
    verification_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='Код верификации')

    def generate_verification_code(self) -> str:
        self.verification_code = get_random_string(10)
        self.save()
        return self.verification_code

    class Meta:
        verbose_name = 'Телеграм бот'
