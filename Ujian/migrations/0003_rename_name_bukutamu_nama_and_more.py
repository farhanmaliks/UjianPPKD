# Generated by Django 5.0.3 on 2024-03-28 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ujian', '0002_remove_bukutamu_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bukutamu',
            old_name='name',
            new_name='nama',
        ),
        migrations.RenameField(
            model_name='bukutamu',
            old_name='message',
            new_name='pesan',
        ),
    ]