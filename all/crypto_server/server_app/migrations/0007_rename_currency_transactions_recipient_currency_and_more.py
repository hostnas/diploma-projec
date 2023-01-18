# Generated by Django 4.1.3 on 2022-12-23 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0006_alter_users_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='currency',
            new_name='recipient_currency',
        ),
        migrations.AddField(
            model_name='transactions',
            name='sender_currency',
            field=models.CharField(blank=True, choices=[('USD', 'dollar'), ('BTC', 'bitcoin'), ('ETH', 'ethereum'), ('LIT', 'litecoin'), ('BNB', 'binance_coin'), ('CRD', 'cardano'), ('SOL', 'solana')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='amount_minus',
            field=models.TextField(verbose_name='Сумма перевода'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='currency',
            field=models.CharField(blank=True, choices=[('USD', 'dollar'), ('BTC', 'bitcoin'), ('ETH', 'ethereum'), ('LIT', 'litecoin'), ('BNB', 'binance_coin'), ('SOL', 'solana')], max_length=3, null=True),
        ),
    ]
