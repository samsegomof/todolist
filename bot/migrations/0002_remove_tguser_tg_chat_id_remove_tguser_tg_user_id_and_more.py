# Generated by Django 4.1.5 on 2023-01-12 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tguser',
            name='tg_chat_id',
        ),
        migrations.RemoveField(
            model_name='tguser',
            name='tg_user_id',
        ),
        migrations.RemoveField(
            model_name='tguser',
            name='tg_username',
        ),
        migrations.AddField(
            model_name='tguser',
            name='chat_id',
            field=models.BigIntegerField(null=True, verbose_name='id чата'),
        ),
        migrations.AddField(
            model_name='tguser',
            name='user_ud',
            field=models.BigIntegerField(null=True, verbose_name='id пользователя'),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='verification_code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Код верификации'),
        ),
    ]
