# Generated by Django 5.0.4 on 2024-05-24 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
