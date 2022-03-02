from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'light_novel'

urlpatterns = [
    path('statistics/', views.statistics, name='statistics'),
    path('characters/', views.characters_view, name='characters_page'),
    path('moves/', views.moves_view, name='moves_page'),
    path('chapters/', views.chapters_view, name='chapters_page'),
    path('sights/', views.sights_view, name='sights_page'),
    path('outfits/', views.outfits_view, name='outfits_page'),
    path('timelines/', views.timelines_view, name='timelines_page'),
    path('scratchpads/', views.scratchpad_view, name='scratchpads_page'),
    path('characters/add/', views.CharacterAdd.as_view(), name='character_add'),
    path('moves/add/', views.MoveAdd.as_view(), name='move_add'),
    path('chapters/add/', views.ChapterAdd.as_view(), name='chapter_add'),
    path('outfits/add/', views.OutfitAdd.as_view(), name='outfit_add'),
    path('sights/add/', views.SightAdd.as_view(), name='sight_add'),
    path('timelines/add/', views.TimelineAdd.as_view(), name='timeline_add'),
    path('scratchpad/add/', views.ScratchPadAdd.as_view(), name='scratchpad_add'),
    path('<str:item>/delete/<int:pk>/', views.delete, name='delete'),
    path('edit_all/<str:item>-<int:pk>/', views.edit_all, name='edit_all'),
    path('characters/character_detail/<int:pk>/', views.char_detail, name='char_detail'),
    path('moves/move_detail/<int:pk>/', views.move_detail, name='move_detail'),
    path('chapters/chapter_detail/<int:pk>/', views.chapter_detail, name='chapter_detail'),
    path('outfits/outfit_detail/<int:pk>/', views.outfit_detail, name='outfit_detail'),
    path('sights/sight_detail/<int:pk>/', views.sight_detail, name='sight_detail'),
    path('timelines/timeline_detail/<int:pk>/', views.timeline_detail, name='timeline_detail'),
    path('scratchpad/scratchpad_detail/<int:pk>/', views.scratchpad_detail, name='scratchpad_detail'),
    path('search/<str:item>/', views.search, name='search'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
