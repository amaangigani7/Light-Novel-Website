from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from .models import Character, Move, Chapter, Outfit, Sight, Timeline, ScratchPad
from .forms import CharacterAddForm, MoveAddForm, ChapterAddForm, OutfitAddForm, SightAddForm, TimelineAddForm, ScratchPadAddForm
from django.views.generic import CreateView, ListView, TemplateView
# from .filters import CharacterFilter
from django.contrib.auth import login, logout
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import datetime
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import random

def statistics(request):

    def gender_cal(choices):
        sizes = []
        labels = []
        path = 'F:\\udemy.django\\lightnovel\\light_novel\\static\\gender_piechart.png'
        for i in choices:
            c = Character.objects.filter(gender=str(i[0])).filter(main_side='main')
            sizes.append(len(c))
            labels.append('{}({})'.format(i[0], len(c)))
        return sizes, labels, path

    def element_cal(choices):
        sizes = []
        labels = []
        path = 'F:\\udemy.django\\lightnovel\\light_novel\\static\\elements_piechart.png'
        for i in choices:
            c = Character.objects.filter(element=str(i[0]))
            sizes.append(len(c))
            labels.append('{}({})'.format(i[0], len(c)))
        return sizes, labels, path

    for i in Character._meta.fields:
        if i.choices != None:
            if i.name == 'gender':
                sizes, labels, path = gender_cal(i.choices)
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, labels=tuple(labels), autopct='%1.1f%%', startangle=90)
                ax1.axis('equal')
                plt.savefig(path,dpi=100)
            if i.name == 'element':
                sizes, labels, path = element_cal(i.choices)
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, labels=tuple(labels), autopct='%1.1f%%', startangle=90)
                ax1.axis('equal')
                plt.savefig(path,dpi=100)
    return render(request,'statistics.html')

class CharacterAdd(LoginRequiredMixin, CreateView):
    template_name = 'character_add.html'
    redirect_field_name = 'character_add.html'
    form_class = CharacterAddForm
    model = Character

class ChapterAdd(LoginRequiredMixin, CreateView):
    template_name = 'chapter_add.html'
    redirect_field_name = 'chapter_add.html'
    form_class = ChapterAddForm
    model = Chapter

class MoveAdd(LoginRequiredMixin, CreateView):
    template_name = 'move_add.html'
    redirect_field_name = 'move_add.html'
    form_class = MoveAddForm
    model = Move

class OutfitAdd(LoginRequiredMixin, CreateView):
    template_name = 'outfit_add.html'
    redirect_field_name = 'outfit_add.html'
    form_class = OutfitAddForm
    model = Outfit

class SightAdd(LoginRequiredMixin, CreateView):
    template_name = 'sight_add.html'
    redirect_field_name = 'sight_add.html'
    form_class = SightAddForm
    model = Sight

class TimelineAdd(LoginRequiredMixin, CreateView):
    template_name = 'timeline_add.html'
    redirect_field_name = 'timeline_add.html'
    form_class = TimelineAddForm
    model = Timeline

class ScratchPadAdd(LoginRequiredMixin, CreateView):
    template_name = 'scratchpad_add.html'
    redirect_field_name = 'scratchpad_add.html'
    form_class = ScratchPadAddForm
    model = ScratchPad

# class CharacterView(ListView):
#     model = Character
#     template_name = 'characters_page.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = CharacterFilter(self.request.GET, queryset=self.get_queryset())
#         return context

@login_required
def characters_view(request):
    characters = Character.objects.all()
    return render(request, 'characters_page.html', {'characters': characters,})

@login_required
def chapters_view(request):
    chapters = Chapter.objects.all()
    return render(request, 'chapters_page.html', {'chapters': chapters})

@login_required
def scratchpad_view(request):
    scratchpads = ScratchPad.objects.all()
    return render(request, 'scratchpads_page.html', {'scratchpads': scratchpads})

@login_required
def moves_view(request):
    moves = Move.objects.all()
    return render(request, 'moves_page.html', {'moves': moves})

@login_required
def sights_view(request):
    sights = Sight.objects.all()
    return render(request, 'sights_page.html', {'sights': sights})

@login_required
def outfits_view(request):
    outfits = Outfit.objects.all()
    return render(request, 'outfits_page.html', {'outfits': outfits})

@login_required
def timelines_view(request):
    timelines = Timeline.objects.all()
    return render(request, 'timelines_page.html', {'timelines': timelines})

@login_required
def char_detail(request, pk):
    try:
        character = Character.objects.get(pk=pk)
        return render(request, 'char_detail.html', {'character': character,})
    except Character.DoesNotExist:
        raise Http404('Character not found')

@login_required
def move_detail(request, pk):
    try:
        move = Move.objects.get(pk=pk)
        return render(request, 'move_detail.html', {'move': move,})
    except Move.DoesNotExist:
        raise Http404('Move not found')

@login_required
def chapter_detail(request, pk):
    try:
        chapter = Chapter.objects.get(pk=pk)
        return render(request, 'chapter_detail.html', {'chapter': chapter,})
    except chapter.DoesNotExist:
        raise Http404('Chapter not found')

@login_required
def scratchpad_detail(request, pk):
    try:
        scratchpad = ScratchPad.objects.get(pk=pk)
        return render(request, 'scratchpad_detail.html', {'scratchpad': scratchpad,})
    except scratchpad.DoesNotExist:
        raise Http404('scratchpad not found')

@login_required
def outfit_detail(request, pk):
    try:
        outfit = Outfit.objects.get(pk=pk)
        return render(request, 'outfit_detail.html', {'outfit': outfit,})
    except outfit.DoesNotExist:
        raise Http404('Outfit not found')

@login_required
def sight_detail(request, pk):
    try:
        sight = Sight.objects.get(pk=pk)
        return render(request, 'sight_detail.html', {'sight': sight,})
    except sight.DoesNotExist:
        raise Http404('Sight not found')

@login_required
def timeline_detail(request, pk):
    try:
        timeline = Timeline.objects.get(pk=pk)
        return render(request, 'timeline_detail.html', {'timeline': timeline,})
    except timeline.DoesNotExist:
        raise Http404('Timeline not found')

@login_required
def delete(request, item, pk):
    try:
        if item == 'char':
            characters = Character.objects.all()
            character = Character.objects.get(pk=pk)
            x = character.name
            character.delete()
            note = 'Character with name {} deleted.'.format(x)
            return render(request, 'characters_page.html', {'note': note, 'characters': characters,})
        elif item == 'move':
            moves = Move.objects.all()
            move = Move.objects.get(pk=pk)
            x = move.name
            move.delete()
            note = 'Move with name "{}" deleted.'.format(x)
            return render(request, 'moves_page.html', {'note': note, 'moves': moves,})
        elif item == 'chapter':
            chapters = Chapter.objects.all()
            move = Chapter.objects.get(pk=pk)
            x = move.name
            move.delete()
            note = 'Chapter with name "{}" deleted.'.format(x)
            return render(request, 'chapters_page.html', {'note': note, 'chapters': chapters,})
        elif item == 'outfit':
            outfits = Outfit.objects.all()
            move = Outfit.objects.get(pk=pk)
            x = move.name
            move.delete()
            note = 'Outfit with name "{}" deleted.'.format(x)
            return render(request, 'outfits_page.html', {'note': note, 'outfits': outfits,})
        elif item == 'sight':
            sights = Sight.objects.all()
            move = Sight.objects.get(pk=pk)
            x = move.name
            move.delete()
            note = 'Sight with name "{}" deleted.'.format(x)
            return render(request, 'sights_page.html', {'note': note, 'sights': sights,})
        elif item == 'timeline':
            timelines = Timeline.objects.all()
            move = Timeline.objects.get(pk=pk)
            x = move.event
            move.delete()
            note = 'Timeline with event "{}..." deleted.'.format(x[:50])
            return render(request, 'timelines_page.html', {'note': note, 'timelines': timelines,})
        elif item == 'scratchpad':
            scratchpads = ScratchPad.objects.all()
            scratchpad = ScratchPad.objects.get(pk=pk)
            x = scratchpad.title
            scratchpad.delete()
            note = 'Scratch Pad with name "{}" deleted.'.format(x)
            return render(request, 'scratchpads_page.html', {'note': note, 'scratchpads': scratchpads,})
    except:
        note = 'Not found'
    return render(request, 'edit_all.html', {'note': note,})

@login_required
def edit_all(request, item, pk):
    char = None
    sight = None
    chapter = None
    outfit = None
    timeline = None
    move = None
    scratchpad = None
    note = 'Initial Data did not change'
    try:
        if item == 'char':
            char = Character.objects.get(pk=pk)
            form = CharacterAddForm(instance=char)
            if request.method == 'GET':
                filled_form = CharacterAddForm(request.GET, instance=char)
        elif item == 'move':
            move = Move.objects.get(pk=pk)
            form = MoveAddForm(instance=move)
            if request.method == 'POST':
                    filled_form = MoveAddForm(request.POST, instance=move)
        elif item == 'sight':
            sight = Sight.objects.get(pk=pk)
            form = SightAddForm(instance=sight)
            if request.method == 'POST':
                    filled_form = SightAddForm(request.POST, instance=sight)
        elif item == 'outfit':
            outfit = Outfit.objects.get(pk=pk)
            form = OutfitAddForm(instance=outfit)
            if request.method == 'POST':
                    filled_form = OutfitAddForm(request.POST, instance=outfit)
        elif item == 'timeline':
            timeline = Timeline.objects.get(pk=pk)
            form = TimelineAddForm(instance=timeline)
            if request.method == 'POST':
                    filled_form = TimelineAddForm(request.POST, instance=timeline)
        elif item == 'scratchpad':
            scratchpad = ScratchPad.objects.get(pk=pk)
            form = ScratchPadAddForm(instance=scratchpad)
            if request.method == 'POST':
                    filled_form = ScratchPadAddForm(request.POST, instance=scratchpad)
        if request.method == 'POST':
            if filled_form.is_valid():
                filled_form.save()
                form = filled_form
                note = 'Updated'
                return render(request, 'edit_all.html', {'form': form, 'char': char, 'move':move, 'sight':sight, 'outfit':outfit, 'chapter':chapter, 'timeline':timeline, 'scratchpad': scratchpad, 'note': note})
    except:
        note = 'Not found'
    note = 'Here is the data...'
    return render(request, 'edit_all.html', {'form': form, 'char': char, 'move':move, 'sight':sight, 'outfit':outfit, 'chapter':chapter, 'timeline':timeline, 'scratchpad': scratchpad, 'note': note})

@login_required
def search(request, item):
    if request.method == 'GET':
        srh =  request.GET.get('searchFor')
        if item == 'char':
            try:
                chars = Character.objects.filter(name__icontains=srh)
                return render(request,"characters_page.html", {"chars": chars,})
            except:
                note = "not found"
                return render(request,"characters_page.html", {'note': note})
        elif item == 'move':
            try:
                movs = Move.objects.filter(name__icontains=srh)
                return render(request,"moves_page.html", {"movs": movs,})
            except:
                note = "not found"
                return render(request,"moves_page.html", {'note': note})
        elif item == 'chapter':
            try:
                chps = Chapter.objects.filter(name__icontains=srh)
                return render(request,"chapters_page.html", {"chps": chps,})
            except:
                note = "not found"
                return render(request,"chapters_page.html", {'note': note})
        elif item == 'outfit':
            try:
                outfts = Outfit.objects.filter(name__icontains=srh)
                return render(request,"outfits_page.html", {"outfts": outfts,})
            except:
                note = "not found"
                return render(request,"outfits_page.html", {'note': note})
        elif item == 'sight':
            try:
                sghts = Sight.objects.filter(name__icontains=srh)
                return render(request,"sights_page.html", {"sghts": sghts,})
            except:
                note = "not found"
                return render(request,"sights_page.html", {'note': note})
        elif item == 'timeline':
            try:
                tlines = Timeline.objects.filter(event__icontains=srh)
                return render(request,"timelines_page.html", {"tlines": tlines,})
            except:
                note = "not found"
                return render(request,"timelines_page.html", {'note': note})
        elif item == 'scratchpad':
            try:
                spads = ScratchPad.objects.filter(title__icontains=srh)
                return render(request,"scratchpads_page.html", {"spads": spads,})
            except:
                note = "not found"
                return render(request,"scratchpads_page.html", {'note': note})
    else:
        p = 'its a post request'
        return render(request, 'home.html', {'p': p})
