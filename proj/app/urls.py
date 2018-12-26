
from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path(r'', RedirectView.as_view(url='/forelesinger')),
    path(r'forelesinger/ny', views.LectureCreateView.as_view(), name='lecture_create'),
    path(r'forelesinger/<int:pk>', views.LectureDetailView.as_view(), name='lecture_detail'),
    path(r'forelesinger/rediger/<int:pk>', views.LectureUpdateView.as_view(), name='lecture_update'),
    path(r'forelesinger/slett/<int:pk>', views.LectureDeleteView.as_view(), name='lecture_delete'),
    path(r'forelesinger', views.LectureListView.as_view(), name='lecture_list'),
]