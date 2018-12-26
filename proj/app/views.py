from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, RedirectView, DetailView
from app.models import Lecture


# Create your views here.

def home(request):
    return render(request, 'app/base.html')

class RedirectToDefaultView(RedirectView):
    pass

class LectureListView(ListView):
    model = Lecture

class LectureDeleteView(DeleteView):
    model = Lecture
    success_url = '/forelesinger'

class LectureCreateView(CreateView):
    model = Lecture
    fields = ['url','title','undertitle', 'pub_date','tags']
    #success_url = '/forelesninger'

class LectureUpdateView(UpdateView):
    model = Lecture
    fields = ['url','title','undertitle', 'pub_date','tags']

class LectureDetailView(DetailView):
    model = Lecture
