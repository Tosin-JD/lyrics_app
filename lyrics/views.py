from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Lyric
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
    

class LyricList(generic.ListView):
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

