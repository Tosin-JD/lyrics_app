from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from lyrics.models import Lyric, Chorus, Verse, Bridge


# Create your views here.
class SearchResult(ListView):
    """This is the page that displays the
    results that the  users make in the site"""
    model = Lyric
    paginate_by = 10
    template_name = "search/search_result.html"

    def get_queryset(self):
        """filter the item the user is searching for
        from the database"""
        search_item = self.request.GET.get('q')
        chorus = Chorus.objects.filter(Q(chorus__icontains=search_item))
        verse = Verse.objects.filter(Q(verse__icontains=search_item))
        bridge = Bridge.objects.filter(Q(bridge__icontains=search_item))

        lyric_from_chorus = Lyric.objects.filter(id__icontains=chorus.values('lyric_id'))
        lyric_from_verse = Lyric.objects.filter(id__icontains=verse.values('lyric_id'))
        lyric_from_bridge = Lyric.objects.filter(id__icontains=bridge.values('lyric_id'))

        object_list = Lyric.objects.filter(Q(title__icontains=search_item)\
            |Q(song_writer__icontains=search_item))

        object_list |= lyric_from_chorus | lyric_from_verse | lyric_from_bridge
        return object_list

