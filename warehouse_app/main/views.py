from typing import Any, Dict
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from main import models, forms


class MainIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'main/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Начальная страница'

        if self.request.user.is_admin == True:
            context["header_text"] = 'АО "ТАЙФУН" СКЛАД'

        return context

    def get_template_names(self):
        template_names = ['main/index_user.html',]

        if self.request.user.is_admin == True:
            template_names = ['main/index.html',]

        return template_names


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name='account/login.html'

    def get_success_url(self):
        return reverse_lazy('main_index')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Вход в систему'

        return context

    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class StaffListView(ListView):
    template_name = 'main/staff/list.html'
    model = models.CustomUser

    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Список сотрудников'
        context["back_url"] = '/'

        return context


class StaffCreateView(CreateView):
    template_name = 'main/staff/new.html'
    model = models.CustomUser
    form_class = forms.CustomUserCreateForm
    success_url = "/staff/"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Добавление сотрудника'
        context["back_url"] = '/staff/'

        return context


class StaffEditView(UpdateView):
    template_name = 'main/staff/edit.html'
    model = models.CustomUser
    form_class = forms.CustomUserCreateForm
    success_url = "/staff/"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Сотрудник'
        context["back_url"] = '/staff/'

        return context


class StaffDeleteView(DeleteView):
    template_name = 'main/staff/delete.html'
    model = models.CustomUser
    form_class = forms.CustomUserCreateForm
    success_url = "/staff/"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Удаление сотрудника'
        context["back_url"] = '/staff/edit/%s'%self.kwargs.get('pk')

        return context
