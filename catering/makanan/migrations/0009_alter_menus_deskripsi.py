# Generated by Django 5.0.6 on 2024-05-30 10:12

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makanan', '0008_alter_menus_deskripsi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menus',
            name='deskripsi',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
