# Generated by Django 4.2.5 on 2024-01-03 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_verification_code_user_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='ключ подтверждения'),
        ),
    ]