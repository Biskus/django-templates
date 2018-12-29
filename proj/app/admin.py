from django.contrib import admin
from app.models import Lecture, Tag

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_filter = ['name','label']
    sortable_by = ['name','label','id']
    ordering = ['-id']
    #def get_sortable_by(self, asdf):
    #    return ['name','label']

admin.site.register(Lecture)
admin.site.register(Tag, TagAdmin)