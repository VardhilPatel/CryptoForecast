# Generated by Django 3.1 on 2021-11-07 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TerraSentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('FearIndex', models.IntegerField()),
                ('Positive', models.IntegerField()),
                ('Negative', models.IntegerField()),
                ('Neutral', models.IntegerField()),
            ],
            options={
                'order_with_respect_to': 'Date',
            },
        ),
        migrations.CreateModel(
            name='SolanaSentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('FearIndex', models.IntegerField()),
                ('Positive', models.IntegerField()),
                ('Negative', models.IntegerField()),
                ('Neutral', models.IntegerField()),
            ],
            options={
                'order_with_respect_to': 'Date',
            },
        ),
        migrations.CreateModel(
            name='ShibaInuSentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('FearIndex', models.IntegerField()),
                ('Positive', models.IntegerField()),
                ('Negative', models.IntegerField()),
                ('Neutral', models.IntegerField()),
            ],
            options={
                'order_with_respect_to': 'Date',
            },
        ),
        migrations.CreateModel(
            name='PolkadotSentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('FearIndex', models.IntegerField()),
                ('Positive', models.IntegerField()),
                ('Negative', models.IntegerField()),
                ('Neutral', models.IntegerField()),
            ],
            options={
                'order_with_respect_to': 'Date',
            },
        ),
        migrations.CreateModel(
            name='LitecoinSentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('FearIndex', models.IntegerField()),
                ('Positive', models.IntegerField()),
                ('Negative', models.IntegerField()),
                ('Neutral', models.IntegerField()),
            ],
            options={
                'order_with_respect_to': 'Date',
            },
        ),
        migrations.CreateModel(
            name='EthereumSentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True)),
                ('FearIndex', models.IntegerField()),
                ('Positive', models.IntegerField()),
                ('Negative', models.IntegerField()),
                ('Neutral', models.IntegerField()),
            ],
            options={
                'order_with_respect_to': 'Date',
            },
        ),
        migrations.CreateModel(
            name='DogeCoinSentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('FearIndex', models.IntegerField()),
                ('Positive', models.IntegerField()),
                ('Negative', models.IntegerField()),
                ('Neutral', models.IntegerField()),
            ],
            options={
                'order_with_respect_to': 'Date',
            },
        ),
        migrations.CreateModel(
            name='CardanoSentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True)),
                ('FearIndex', models.IntegerField()),
                ('Positive', models.IntegerField()),
                ('Negative', models.IntegerField()),
                ('Neutral', models.IntegerField()),
            ],
            options={
                'order_with_respect_to': 'Date',
            },
        ),
        migrations.CreateModel(
            name='BitcoinSentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True)),
                ('FearIndex', models.IntegerField()),
                ('Positive', models.IntegerField()),
                ('Negative', models.IntegerField()),
                ('Neutral', models.IntegerField()),
            ],
            options={
                'order_with_respect_to': 'Date',
            },
        ),
        migrations.CreateModel(
            name='BinanceCoinSentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True)),
                ('FearIndex', models.IntegerField()),
                ('Positive', models.IntegerField()),
                ('Negative', models.IntegerField()),
                ('Neutral', models.IntegerField()),
            ],
            options={
                'order_with_respect_to': 'Date',
            },
        ),
    ]