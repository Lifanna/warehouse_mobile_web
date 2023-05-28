from typing import Any, Dict
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from main import models, forms
from django.http import JsonResponse
from rest_framework.generics import RetrieveAPIView
from main.serializers import EquipmentSerializer
from rest_framework.response import Response


class QrScanView(TemplateView):
    template_name = 'main/qr/new.html'
    model = models.Warehouse

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["header_text"] = 'Сканирование QR-кода'
        context["qr_page"] = True
        context["back_url"] = '/'

        return context


class EquipmentListAPIView(RetrieveAPIView):
    lookup_field = "pk"
    serializer_class = EquipmentSerializer
    queryset = models.Equipment.objects.all()

    # def retrieve(self, request, *args, **kwargs):
    #     pk = self.kwargs['pk']
    #     queryset = self.model.objects.get(pk=pk)

    #     self.serializer = self.serializer_class(queryset)

    #     return self.serializer.data
