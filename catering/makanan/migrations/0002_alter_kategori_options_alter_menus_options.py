# Generated by Django 5.0.6 on 2024-05-28 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makanan', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategori',
            options={'verbose_name_plural': 'Kategori'},
        ),
        migrations.AlterModelOptions(
            name='menus',
            options={'verbose_name_plural': 'Menus'},
        ),
    ]
