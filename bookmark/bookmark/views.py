from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from bookmark.models import Bookmark


class BookmarkList(ListView):
    model = Bookmark


class BookmarkCreate(CreateView):
    model = Bookmark
    fields = ['site_name', 'url', 'contents']
    template_name_suffix = '_create'
    success_url = '/'


class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url', 'contents']
    template_name_suffix = '_update'
    success_url = '/'

class BookmarkDelete(DeleteView):
    model = Bookmark
    template_name_suffix = '_delete'
    success_url = '/'

class BookmarkDetail(DetailView):
    model = Bookmark
    template_name_suffix = '_detail'