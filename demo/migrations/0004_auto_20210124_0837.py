# Generated by Django 3.1.5 on 2021-01-24 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20210124_0828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='movies',
            new_name='movie',
        ),
    ]
