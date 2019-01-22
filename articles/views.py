from django.contrib.auth.mixins import LoginRequiredMixin  # for user authorization
# for using dispatch() to restrect users
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'


class ArticleDetailView(LoginRequiredMixin, DetailView):  # new

    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):  # new

    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):  # new

    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = "login"

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleCreateView(LoginRequiredMixin, CreateView):

    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body',)
    login_url = 'login'  # for using mixin, this is to overried the defualt mixin url

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
