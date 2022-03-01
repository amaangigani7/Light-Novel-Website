# Generated by Django 3.1.2 on 2022-02-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_novel', '0004_auto_20220205_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]