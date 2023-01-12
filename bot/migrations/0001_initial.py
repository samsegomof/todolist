# Generated by Django 4.1.5 on 2023-01-12 23:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.BigIntegerField(null=True, verbose_name='id чата')),
                ('user_ud', models.BigIntegerField(null=True, verbose_name='id пользователя')),
                ('tg_username', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(5)])),
                ('verification_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Код верификации')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Телеграм бот',
            },
        ),
    ]
