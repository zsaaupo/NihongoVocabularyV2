# Generated by Django 4.2.1 on 2023-05-17 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('N4', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabularylistn4',
            name='list_number',
            field=models.CharField(max_length=2, unique=True),
        ),
    ]