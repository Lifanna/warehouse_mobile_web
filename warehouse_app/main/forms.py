from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from main import models
from django.contrib.auth.password_validation import validate_password
import os
from uuid import uuid4
from django.core.files import File


class CustomUserCreateForm(UserCreationForm):
    department = forms.ModelChoiceField(label="", queryset=models.Department.objects.all(), empty_label="Выберите отдел")

    status = forms.ModelChoiceField(label="", queryset=models.Status.objects.all(), empty_label="Выберите должность")

    is_admin = forms.BooleanField(label="Администратор приложения", required=False)

    class Meta:
        model = models.CustomUser
        fields = (
            'first_name',
            'last_name',
            'patronymic',
            'status',
            'department',
            'username',
            'password1',
            'password2',
            'is_admin',
        )


class EquipmentCreateForm(forms.ModelForm):
    producer = forms.ModelChoiceField(label="", queryset=models.Producer.objects.all(), empty_label="Выберите производителя")

    warehouse = forms.ModelChoiceField(label="", queryset=models.Warehouse.objects.all(), empty_label="Выберите склад")

    class Meta:
        model = models.Equipment
        fields = '__all__'
        exclude = ('user',)


class WarehouseCreateForm(forms.ModelForm):
    class Meta:
        model = models.Warehouse
        fields = '__all__'


class ProducerCreateForm(forms.ModelForm):
    class Meta:
        model = models.Producer
        fields = '__all__'


class RequestCreateForm(forms.ModelForm):
    equipment = forms.ModelChoiceField(label="", queryset=models.Equipment.objects.all(), empty_label="Выберите оборудование")

    class Meta:
        model = models.Request
        fields = '__all__'
        exclude = ('created_at', 'updated_at',)
