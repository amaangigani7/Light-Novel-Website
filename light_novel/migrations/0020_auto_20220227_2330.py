# Generated by Django 3.1.2 on 2022-02-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_novel', '0019_auto_20220226_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='superiority_complex',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, null=True),
        ),
    ]
