# Generated by Django 5.0.6 on 2024-05-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('Frozen Food', 'Forzen Food'), ('Vegi', 'Vegi'), ('Non-Veg', 'Non-Veg')], max_length=250),
        ),
    ]