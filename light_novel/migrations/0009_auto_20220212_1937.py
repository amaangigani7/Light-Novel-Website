# Generated by Django 3.1.2 on 2022-02-12 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('light_novel', '0008_auto_20220212_1936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timeline',
            old_name='data_time',
            new_name='date_time',
        ),
    ]
