# Generated by Django 4.2 on 2024-07-13 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0003_alter_post_options_remove_category_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=1, upload_to='blog', verbose_name='Imagen'),
            preserve_default=False,
        ),
    ]