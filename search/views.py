from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from lyrics.models import Lyric


# Create your views here.
class SearchResult(ListView, LoginRequiredMixin):
    """This is the page that displays the
    results that the  users make in the site"""
    model = Lyric
    template_name = "search/search_result.html"

    def get_queryset(self):
        """filter the item the user is searching for
        from the database"""
        search_item = self.request.GET.get('q')
        object_list = Lyric.objects.filter(Q(title__icontains=search_item))
        return object_list

