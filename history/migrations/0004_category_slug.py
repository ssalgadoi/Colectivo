# Generated by Django 4.2 on 2024-07-11 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0003_alter_post_options_remove_category_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]