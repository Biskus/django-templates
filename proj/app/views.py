from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, RedirectView, DetailView
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

from app.models import Lecture, Tag
from app.forms import TagForm



# Create your views here.

def home(request):
    return render(request, 'app/base.html')


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class TagCreateView(CreateView):
    current_tab = 'tags'
    model = Tag
    form_class = TagForm
    #fields = ['name', 'label']
    all_tags = Tag.objects.all
    success_url = '/'

class TagListView(ListView):
    current_tab = 'tags'
    model = Tag

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class TagUpdateView(UpdateView):
    success_url = '/forelesninger'
    current_tab = 'tags'
    model = Tag
    fields = ['name','label',]


class LectureListView(ListView):
    current_tab = 'lectures'
    model = Lecture
    
    def get_queryset(self):
        queryset = self.model.objects.filter(title__icontains=self.request.GET.get('search',''))
        return queryset

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class LectureDeleteView(DeleteView):
    current_tab = 'lectures'
    model = Lecture
    success_url = '/forelesninger'

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class LectureCreateView(CreateView):
    current_tab = 'lectures'
    model = Lecture
    fields = ['url','title','undertitle','target_audience', 'pub_date','tags','tasks']
    #success_url = '/forelesninger'

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
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