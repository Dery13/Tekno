# Generated by Django 5.0.6 on 2024-05-29 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makanan', '0003_remove_menus_nama'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Kategori',
            new_name='Kategory',
        ),
        migrations.AlterModelOptions(
            name='kategory',
            options={'verbose_name_plural': 'Kategory'},
        ),
    ]
