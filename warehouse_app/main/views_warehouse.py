from typing import Any, Dict
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from main import models, forms


class WarehouseListView(ListView):
    template_name = 'main/warehouse/list.html'
    model = models.Warehouse

    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Склад'
        context["back_url"] = '/'

        return context


class WarehouseCreateView(CreateView):
    template_name = 'main/warehouse/new.html'
    model = models.Warehouse
    form_class = forms.WarehouseCreateForm
    success_url = "/warehouse/"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Добавление склада'
        context["back_url"] = '/warehouse/'

        return context


class WarehouseEditView(UpdateView):
    template_name = 'main/warehouse/edit.html'
    model = models.Warehouse
    form_class = forms.WarehouseCreateForm
    success_url = "/warehouse/"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Склад'
        context["back_url"] = '/warehouse/'

        return context


class WarehouseDeleteView(DeleteView):
    template_name = 'main/warehouse/delete.html'
    model = models.Warehouse
    form_class = forms.WarehouseCreateForm
    success_url = "/warehouse/"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Удаление склада'
        context["back_url"] = '/warehouse/edit/%s'%self.kwargs.get('pk')

        return context
