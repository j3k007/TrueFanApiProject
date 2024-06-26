# Generated by Django 4.1.13 on 2024-05-28 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('category', models.CharField(choices=[('Frozen Food', 'Forzen Food'), ('Vegi', 'Vegi'), ('Non-Veg', 'Non-Veg'), ('Bevrages', 'Bevrages')], max_length=250)),
                ('price', models.FloatField(default=None, max_length=250)),
            ],
            options={
                'db_table': 'productApi_products',
            },
        ),
    ]
