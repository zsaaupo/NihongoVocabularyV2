# Generated by Django 4.2.1 on 2023-05-17 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('N4', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vocabulary',
        ),
        migrations.DeleteModel(
            name='VocabularyList',
        ),
    ]