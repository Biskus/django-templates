from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, RedirectView, DetailView
from app.models import Lecture, Tag


# Create your views here.

def home(request):
    return render(request, 'app/base.html')


class TagCreateView(CreateView):
    current_tab = 'tags'
    model = Tag
    fields = ['name', 'label']
    all_tags = Tag.objects.all
    success_url = '/'

class TagListView(ListView):
    current_tab = 'tags'
    model = Tag

class TagUpdateView(UpdateView):
    success_url = '/forelesninger'
    current_tab = 'tags'
    model = Tag
    fields = ['name','label',]


class LectureListView(ListView):
    current_tab = 'lectures'
    model = Lecture

class LectureDeleteView(DeleteView):
    current_tab = 'lectures'
    model = Lecture
    success_url = '/forelesninger'

class LectureCreateView(CreateView):
    current_tab = 'lectures'
    model = Lecture
    fields = ['url','title','undertitle','target_audience', 'pub_date','tags','tasks']
    #success_url = '/forelesninger'

class LectureUpdateView(UpdateView):
    success_url = '/forelesninger'
    current_tab = 'lectures'
    model = Lecture
    fields = ['url','title','undertitle','target_audience', 'pub_date','tags','tasks']

class LectureDetailView(DetailView):
    current_tab = 'lectures'
    model = Lecture

class RedirectToDefaultView(RedirectView):
    pass