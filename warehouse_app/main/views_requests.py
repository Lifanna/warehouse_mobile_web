from typing import Any, Dict
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View, ListView, CreateView, DetailView, UpdateView, DeleteView
from main import models, forms


class RequestListView(ListView):
    template_name = 'main/request/list.html'
    model = models.Request

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Список заявок'
        context["back_url"] = '/'

        return context


class RequestCreateView(CreateView):
    template_name = 'main/request/new.html'
    model = models.Request
    form_class = forms.RequestCreateForm
    success_url = "/"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Формирование заявки'
        context["back_url"] = '/'

        return context


class RequestEditView(DetailView):
    template_name = 'main/request/edit.html'
    model = models.Request
    success_url = "/requests/"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Заявка №%s от %s'%(self.kwargs.get('pk'), self.get_object().created_at.strftime('%d.%m.%Y'))
        context["back_url"] = '/requests/'

        return context


# надо переделать
class RequestDeclineView(DeleteView):
    model = models.Request

    def get(self, request):
        request = self.model.objects.get(pk=request.GET.get('id'))

        request.status = models.RequestStatus.objects.get(name='отклонена')
        request.save()

        return redirect('/requests/')


class RequestAcceptView(View):
    model = models.Request

    def get(self, request):
        request = self.model.objects.get(pk=request.GET.get('id'))

        request.status = models.RequestStatus.objects.get(name='обработана')
        request.save()

        return redirect('/requests/')
