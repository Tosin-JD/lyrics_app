from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Lyric, Chorus, Verse, Bridge
from .forms import LyricForm

# Create your views here.
class HomePage(generic.TemplateView):
    model = Lyric
    template_name = 'index.html'


class AboutPage(generic.TemplateView):
    template_name = 'about.html'


class CreateLyric(generic.CreateView):
    model = Lyric
    template_name = 'lyrics/lyric_form.html'
    form_class = LyricForm


class SecondCreateLyric(generic.UpdateView):
    """Also does the  function 
    of editing the lyric"""
    model = Lyric
    template_name = 'lyrics/lyric_complete_form.html'
    form_class = LyricForm
    

class LyricList(generic.ListView):
    paginate_by = 10
    model = Lyric
    template_name = 'lyrics/lyric_list.html'


class LyricDetail(generic.DetailView):
    model = Lyric
    template_name = 'lyrics/lyric_details.html'
    

class DeleteLyric(generic.DeleteView):
    model = Lyric
    template_name = 'lyrics/lyric_delete.html'
    

def lyric_json(request):
    data = {'result': list(Lyric.objects.all())}
    return JsonResponse(data)


class CreateChorus(generic.CreateView):
    model = Chorus
    fields = ('chorus',)

    def form_valid(self, form):
        self.lyric = get_object_or_404(Lyric, slug=self.kwargs['slug'])
        form.instance.lyric = self.lyric
        return super().form_valid(form)


class CreateVerse(generic.CreateView):
    model = Verse
    fields = ('verse',)

    def form_valid(self, form):
        self.lyric = get_object_or_404(Lyric, slug=self.kwargs['slug'])
        form.instance.lyric = self.lyric
        return super().form_valid(form)


class CreateBridge(generic.CreateView):
    model = Bridge
    fields = ('bridge',)

    def form_valid(self, form):
        self.lyric = get_object_or_404(Lyric, slug=self.kwargs['slug'])
        form.instance.lyric = self.lyric
        return super().form_valid(form)


class UpdateChorus(generic.UpdateView):
    model = Chorus
    fields = ('chorus',)
    template_name = 'lyrics/sub_update.html'


class UpdateVerse(generic.UpdateView):
    model = Verse
    fields = ('verse',)
    template_name = 'lyrics/sub_update.html'


class UpdateBridge(generic.UpdateView):
    model = Bridge
    fields = ('bridge',)
    template_name = 'lyrics/sub_update.html'


class DeleteChorus(generic.DeleteView):
    model = Chorus
    fields = ('chorus',)
    template_name = 'lyrics/sub_delete.html'


class DeleteVerse(generic.DeleteView):
    model = Verse
    fields = ('verse',)
    template_name = 'lyrics/sub_delete.html'


class DeleteBridge(generic.DeleteView):
    model = Bridge
    fields = ('bridge',)
    template_name = 'lyrics/sub_delete.html'

