# Generated by Django 3.1.2 on 2022-02-13 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('light_novel', '0009_auto_20220212_1937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='character',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='move',
            options={'ordering': ['owner', 'name']},
        ),
        migrations.AlterModelOptions(
            name='outfit',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='sight',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='character',
            name='outfit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_outfit', to='light_novel.outfit'),
        ),
    ]
