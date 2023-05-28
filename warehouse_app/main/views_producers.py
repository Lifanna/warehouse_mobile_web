from typing import Any, Dict
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from main import models, forms


class ProducerListView(ListView):
    template_name = 'main/producer/list.html'
    model = models.Producer

    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Производители'
        context["back_url"] = '/'

        return context


class ProducerCreateView(CreateView):
    template_name = 'main/producer/new.html'
    model = models.Producer
    form_class = forms.ProducerCreateForm
    success_url = "/producers/"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Добавление производителя'
        context["back_url"] = '/producers/'

        return context


class ProducerEditView(UpdateView):
    template_name = 'main/producer/edit.html'
    model = models.Producer
    form_class = forms.ProducerCreateForm
    success_url = "/producers/"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Производитель'
        context["back_url"] = '/producers/'

        return context


class ProducerDeleteView(DeleteView):
    template_name = 'main/producer/delete.html'
    model = models.Producer
    form_class = forms.ProducerCreateForm
    success_url = "/producers/"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Удаление производителя'
        context["back_url"] = '/producers/edit/%s'%self.kwargs.get('pk')

        return context
