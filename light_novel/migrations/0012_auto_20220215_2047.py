# Generated by Django 3.1.2 on 2022-02-15 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('light_novel', '0011_auto_20220215_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='goal',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='greatest_fear',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='intro_extro',
            field=models.CharField(blank=True, choices=[('Introvert', 'Introvert'), ('Extrovert', 'Extrovert')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='opti_pesi',
            field=models.CharField(blank=True, choices=[('Optimistic', 'Optimistic'), ('Pessimistic', 'Pessimistic')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='outfit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_outfit', to='light_novel.outfit'),
        ),
        migrations.AddField(
            model_name='character',
            name='philosophy_of_life',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='skin',
            field=models.CharField(blank=True, choices=[('Fair', 'Fair'), ('Brown', 'Brown'), ('Black', 'Black'), ('Light', 'Light')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='strongest_trait',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='superiority_complex',
            field=models.BooleanField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='way_to_display_affection',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='weakest_trait',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]