# Generated by Django 5.0.6 on 2024-05-28 13:33

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
                ('category', models.CharField(max_length=250)),
                ('price', models.FloatField(default=None, max_length=250)),
            ],
        ),
    ]