
from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path(r'', RedirectView.as_view(url='/forelesninger')),
    path(r'forelesninger/ny', views.LectureCreateView.as_view(), name='lecture_create'),
    path(r'forelesninger/<int:pk>', views.LectureDetailView.as_view(), name='lecture_detail'),
    path(r'forelesninger/rediger/<int:pk>', views.LectureUpdateView.as_view(), name='lecture_update'),
    path(r'forelesninger/slett/<int:pk>', views.LectureDeleteView.as_view(), name='lecture_delete'),
    path(r'forelesninger', views.LectureListView.as_view(), name='lecture_list'),
    path(r'tag/ny', views.TagCreateView.as_view(), name='tag_create'),
    path(r'tag/rediger/<int:pk>', views.TagUpdateView.as_view(), name='tag_update'),
]