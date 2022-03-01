# Generated by Django 3.1.2 on 2022-02-15 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('light_novel', '0013_auto_20220215_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='best_childhood_memory',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='best_friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='characters_best_friend', to='light_novel.character'),
        ),
        migrations.AddField(
            model_name='character',
            name='kids',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='characters_kids', to='light_novel.character'),
        ),
        migrations.AddField(
            model_name='character',
            name='likes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='characters_likes', to='light_novel.character'),
        ),
        migrations.AddField(
            model_name='character',
            name='past_action_ashamed_of',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='past_action_proud_of',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='siblings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='characters_siblings', to='light_novel.character'),
        ),
        migrations.AddField(
            model_name='character',
            name='worst_childhood_memory',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
