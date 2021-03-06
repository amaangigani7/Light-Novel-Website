# Generated by Django 3.1.2 on 2022-02-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_novel', '0021_auto_20220227_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='element_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='appearance',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='element',
            field=models.CharField(blank=True, choices=[('Fire', 'Fire'), ('Wind', 'Wind'), ('Water', 'Water'), ('Earth', 'Earth'), ('Lightning', 'Lightning'), ('Random', 'Random'), ('None', 'None')], max_length=20, null=True),
        ),
    ]
