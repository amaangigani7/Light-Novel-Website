import datetime
from django import forms
from .models import Character, Move, Chapter, Outfit, Sight, Timeline, ScratchPad
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from lightnovel import settings


class CharacterAddForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('name', 'gender', 'element', 'height',
        'hair', 'hair_length', 'eye_colour', 'date_of_birth', 'place_of_birth', 'main_side',
        'appearance', 'outfit', 'skin', 'opti_pesi', 'intro_extro', 'superiority_complex',
        'strongest_trait', 'weakest_trait', 'way_to_display_affection', 'greatest_fear',
        'philosophy_of_life', 'goal', 'kids', 'siblings', 'best_friend', 'likes', 'best_childhood_memory',
        'worst_childhood_memory', 'past_action_proud_of', 'past_action_ashamed_of', 'saved_by',
        'finance_as_child', 'raised', 'crushed_with_disappointment', 'relationship_status',
        'comedy_trait', 'weapon_or_choice', 'despised_one', 'peaceful_place')


class MoveAddForm(forms.ModelForm):
    class Meta:
        model = Move
        fields = ('name', 'description', 'owner')

class ChapterAddForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ('name', 'content')

class OutfitAddForm(forms.ModelForm):
    class Meta:
        model = Outfit
        fields = ('name', 'worn_by', 'description')

class SightAddForm(forms.ModelForm):
    class Meta:
        model = Sight
        fields = ('name', 'first_seen', 'description')

class DateInput(forms.DateInput):
    input_type = 'date'

class TimelineAddForm(forms.ModelForm):

    class Meta:
        model = Timeline
        fields = ('event', 'date_field')
        widgets = {
            'date_field': DateInput(),
        }

class ScratchPadAddForm(forms.ModelForm):
    class Meta:
        model = ScratchPad
        fields = ('title', 'content')
