from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, PermissionsMixin
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model

class User(User, PermissionsMixin):
    user_name = models.CharField(name='user_name', max_length=100, blank=True, null=True, unique=True)
    email_id = models.EmailField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.user_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Sight(models.Model):
    name = models.CharField(max_length=200)
    first_seen = models.CharField(max_length=20)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("light_novel:sight_add", args={})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Outfit(models.Model):
    name = models.CharField(max_length=100)
    worn_by = models.CharField(max_length=100)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("light_novel:outfit_add", args={})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Character(models.Model):
    gender_choices = (("M", "M"), ("F", "F"))
    element_choices = (("Fire", "Fire"), ('Wind','Wind'), ('Water','Water'), ('Earth','Earth'), ('Lightning', 'Lightning'), ('Random', 'Random'), ('None', 'None'))
    hair_choices = (('black', 'black'), ('brown', 'brown'), ('blond', 'blond'), ('red', 'red'), ('grey', 'grey'))
    hair_length_choices = (('Short', 'Short'),('Medium', 'Medium'),('Long', 'Long'))
    eye_colour_choices = (('black', 'black'), ('brown', 'brown'), ('blue', 'blue'), ('grey', 'grey'), ('green', 'green'))
    main_side_choices = (('main', 'main'), ('side', 'side'))
    height_choices = (('short', 'short'), ('medium', 'medium'), ('tall', 'tall'))
    skin_choices = (('Fair', 'Fair'), ('Brown', 'Brown'), ('Black', 'Black'), ('Light', 'Light'))
    opti_pesi_choices = (('Optimistic', 'Optimistic'), ('Pessimistic', 'Pessimistic'))
    intro_extro_choices = (('Introvert', 'Introvert'), ('Extrovert', 'Extrovert'))
    bool_choices = ((True, 'Yes'), (False, 'No'))
    finance_choices = (('Rich', 'Rich'), ('Middle', 'Middle'), ('Poor', 'Poor'))
    raised_choices = (('Nurtured', 'Nurtured'), ('Neglected', 'Neglected'))
    relationship_choices = (('Single', 'Single'), ('With Someone', 'With Someone'))

    name = models.CharField(max_length=200, unique=True)
    gender = models.CharField(max_length=10, choices=gender_choices, blank=True, null=True)
    element = models.CharField(max_length=20, choices=element_choices, blank=True, null=True)
    element_description = models.TextField(null=True, blank=True)
    height = models.CharField(max_length=20, choices=height_choices, blank=True, null=True)
    hair = models.CharField(max_length=20, choices=hair_choices, blank=True, null=True)
    hair_length = models.CharField(max_length=20, choices=hair_length_choices, blank=True, null=True)
    eye_colour = models.CharField(max_length=20, choices=eye_colour_choices, blank=True, null=True)
    date_of_birth = models.DateField(max_length=100, null=True, blank=True)
    place_of_birth = models.CharField(max_length=200, null=True, blank=True)
    main_side = models.CharField(max_length=20, choices=main_side_choices, blank=True, null=True)
    current_post = models.CharField(max_length=100, null=True, blank=True)
    appearance = models.TextField(null=True, blank=True)
    outfit = models.ForeignKey(Outfit, null=True, blank=True, related_name='character_outfit', on_delete=models.CASCADE)
    skin = models.CharField(max_length=20, choices=skin_choices, blank=True, null=True)
    opti_pesi = models.CharField(max_length=20, choices=opti_pesi_choices, blank=True, null=True)
    intro_extro = models.CharField(max_length=20, choices=intro_extro_choices, blank=True, null=True)
    superiority_complex = models.BooleanField(null=True, blank=True, choices=bool_choices)
    strongest_trait = models.CharField(max_length=100, null=True, blank=True)
    weakest_trait = models.CharField(max_length=100, null=True, blank=True)
    way_to_display_affection = models.CharField(max_length=100, null=True, blank=True)
    greatest_fear = models.CharField(max_length=100, null=True, blank=True)
    philosophy_of_life = models.CharField(max_length=200, null=True, blank=True)
    goal = models.CharField(max_length=100, null=True, blank=True)
    kids = models.ForeignKey('self', null=True, blank=True, related_name="characters_kids", on_delete=models.CASCADE)
    siblings = models.ForeignKey('self', null=True, blank=True, related_name="characters_siblings", on_delete=models.CASCADE)
    best_friend = models.ForeignKey('self', null=True, blank=True, related_name="characters_best_friend", on_delete=models.CASCADE)
    likes = models.ForeignKey('self', null=True, blank=True, related_name="characters_likes", on_delete=models.CASCADE)
    best_childhood_memory = models.CharField(max_length=200, null=True, blank=True)
    worst_childhood_memory = models.CharField(max_length=200, null=True, blank=True)
    past_action_proud_of = models.CharField(max_length=200, null=True, blank=True)
    past_action_ashamed_of = models.CharField(max_length=200, null=True, blank=True)
    saved_by = models.ForeignKey('self', null=True, blank=True, related_name="characters_saved_by", on_delete=models.CASCADE)
    finance_as_child = models.CharField(max_length=20, choices=finance_choices, blank=True, null=True)
    raised = models.CharField(max_length=20, choices=raised_choices, blank=True, null=True)
    crushed_with_disappointment = models.CharField(max_length=300, null=True, blank=True)
    relationship_status = models.CharField(max_length=20, choices=relationship_choices, blank=True, null=True)
    comedy_trait = models.CharField(max_length=200, null=True, blank=True)
    weapon_or_choice = models.CharField(max_length=100, null=True, blank=True)
    despised_one = models.CharField(max_length=100, null=True, blank=True)
    peaceful_place = models.CharField(max_length=100, null=True, blank=True)
    # _list_of_moves = models.CharField(max_length)

    def get_absolute_url(self):
        return reverse("light_novel:character_add", args={})

    # def get_all_moves(self):


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Move(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(unique=True)
    owner = models.ForeignKey(Character, null=True, related_name='character_name', on_delete=models.CASCADE)
    first_seen = models.CharField(max_length=100, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("light_novel:move_add", args={})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['owner', 'name']


class Chapter(models.Model):
    number = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=300)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("light_novel:chapter_add", args={})

    def chapter_length(self):
        return len(content)

    def __str__(self):
        return self.number + ' ' + self.name

    class Meta:
        ordering = ['number']

class Timeline(models.Model):
    date_field = models.DateField(null=True, blank=True)
    event = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("light_novel:timeline_add", args={})

    def __str__(self):
        return self.event

    class Meta:
        ordering = ['date_field']

class ScratchPad(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("light_novel:scratchpad_add", args={})

    def __str__(self):
        return self.title
