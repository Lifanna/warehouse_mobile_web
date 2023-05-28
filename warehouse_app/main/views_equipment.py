from typing import Any, Dict
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from main import models, forms
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from main import serializers
from rest_framework.permissions import AllowAny


class EquipmentListView(ListView):
    template_name = 'main/equipment/list.html'
    model = models.Equipment

    def get_queryset(self):
        print("ASDASDASD", self.request.user.is_admin)
        if self.request.user.is_admin == True:
            queryset = self.model.objects.all()
        else:
            queryset = self.model.objects.filter(user=self.request.user).all()

        return queryset
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Список оборудования'
        context["back_url"] = '/'

        return context


class EquipmentCreateView(CreateView):
    template_name = 'main/equipment/new.html'
    model = models.Equipment
    form_class = forms.EquipmentCreateForm
    success_url = "/equipment/"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Добавление оборудования'
        context["back_url"] = '/equipment/'

        return context


class EquipmentEditView(UpdateView):
    template_name = 'main/equipment/edit.html'
    model = models.Equipment
    form_class = forms.EquipmentCreateForm
    success_url = "/equipment/"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Оборудование'
        context["back_url"] = '/equipment/'

        return context


class EquipmentSetView(UpdateAPIView):
    queryset = models.Equipment.objects.all()
    serializer_class = serializers.EquipmentSetSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
        print("AZAZA: ", request.data)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Оборудование успешно добавлено!"})
        else:
            return Response({"message": "failed", "details": serializer.errors})


class EquipmentDeleteView(DeleteView):
    template_name = 'main/equipment/delete.html'
    model = models.Equipment
    form_class = forms.EquipmentCreateForm
    success_url = "/equipment/"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Удаление оборудования'
        context["back_url"] = '/equipment/edit/%s'%self.kwargs.get('pk')

        return context
