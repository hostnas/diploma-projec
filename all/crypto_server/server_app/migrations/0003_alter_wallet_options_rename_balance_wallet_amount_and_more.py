# Generated by Django 4.1.3 on 2022-12-17 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0002_alter_wallet_options_remove_transactions_amount_plus_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wallet',
            options={},
        ),
        migrations.RenameField(
            model_name='wallet',
            old_name='balance',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='binance_coin',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='bitcoin',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='cardano',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='ethereum',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='litecoin',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='overall_balance',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='solana',
        ),
        migrations.AddField(
            model_name='wallet',
            name='currency',
            field=models.CharField(blank=True, choices=[('USD', 'dollar'), ('BTC', 'bitcoin'), ('ETH', 'ethereum'), ('LIT', 'litecoin'), ('BNB', 'binance_coin'), ('CRD', 'cardano'), ('SOL', 'solana')], max_length=3, null=True),
        ),
    ]
