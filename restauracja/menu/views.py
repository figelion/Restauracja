# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import Http404
from django.template import loader

from .models import PeriodicMenu
from .models import Place
from .models import Comment
from .models import Dishes

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def index(request):
    place_list = Place.objects.order_by('id')
    context = {'place_list': place_list}
    return render(request, 'menu/index.html', context)

def detail(request, place_id):


    menu_list = PeriodicMenu.objects.filter(place=place_id)
    comments_list = Comment.objects.filter(place=place_id)

    context = {'menu_list': menu_list,
               'comments_list': comments_list
               }

    return render(request, 'menu/detail.html', context)

class CommentListView(ListView):
    model = Comment
    template_name = 'menu/detail.html'
    context_object_name = 'comments_list'
    ordering = ['timestamp']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['menu_list'] = PeriodicMenu.objects.filter(place=self.kwargs.get('place_id'))
        context['comments_list'] = Comment.objects.filter(place=self.kwargs.get('place_id')).order_by('-timestamp')
        return context

class CommentDetailView(DetailView):
    model = Comment

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['comment_text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.place = self.kwargs.get(['place_id'])
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['comment_text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = '/'

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False



def dishes(request, periodicMenu_id):
    # try:
    #     menu = PeriodicMenu.objects.get(pk=periodicMenu_id)
    # except PeriodicMenu.DoesNotExist:
    #     raise Http404("Menu does not exist")
    # return render(request, 'menu/detail.html', {'menu':menu})
    menu = get_object_or_404(PeriodicMenu, pk=periodicMenu_id)
    return render(request, 'menu/dishes.html', {'menu': menu})


