# Generated by Django 4.2 on 2024-07-03 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published'], 'verbose_name': 'Artículo', 'verbose_name_plural': 'Artículos'},
        ),
    ]
