"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# -*- coding: utf-8 -*-
from django.urls import path
from main import views, views_equipment, views_warehouse, views_producers, views_requests, views_qr


urlpatterns = [
    path('', views.MainIndexView.as_view(), name="main_index"),

    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),

    path('staff/', views.StaffListView.as_view(), name='staff'),
    path('staff/add', views.StaffCreateView.as_view(), name='staff_add'),
    path('staff/edit/<int:pk>', views.StaffEditView.as_view(), name='staff_edit'),
    path('staff/delete/<int:pk>', views.StaffDeleteView.as_view(), name='staff_delete'),

    path('equipment/', views_equipment.EquipmentListView.as_view(), name='equipment'),
    path('equipment/add', views_equipment.EquipmentCreateView.as_view(), name='equipment_add'),
    path('equipment/edit/<int:pk>', views_equipment.EquipmentEditView.as_view(), name='equipment_edit'),
    path('equipment/delete/<int:pk>', views_equipment.EquipmentDeleteView.as_view(), name='equipment_delete'),
    path('equipment/set/<int:pk>', views_equipment.EquipmentSetView.as_view(), name='equipment_set'),

    path('warehouse/', views_warehouse.WarehouseListView.as_view(), name='warehouse'),
    path('warehouse/add', views_warehouse.WarehouseCreateView.as_view(), name='warehouse_add'),
    path('warehouse/edit/<int:pk>', views_warehouse.WarehouseEditView.as_view(), name='warehouse_edit'),
    path('warehouse/delete/<int:pk>', views_warehouse.WarehouseDeleteView.as_view(), name='warehouse_delete'),

    path('producers/', views_producers.ProducerListView.as_view(), name='producers'),
    path('producers/add', views_producers.ProducerCreateView.as_view(), name='producers_add'),
    path('producers/edit/<int:pk>', views_producers.ProducerEditView.as_view(), name='producers_edit'),
    path('producers/delete/<int:pk>', views_producers.ProducerDeleteView.as_view(), name='producers_delete'),

    path('requests/', views_requests.RequestListView.as_view(), name='requests'),
    path('requests/add', views_requests.RequestCreateView.as_view(), name='requests_add'),
    path('requests/edit/<int:pk>', views_requests.RequestEditView.as_view(), name='requests_edit'),
    path('requests/accept', views_requests.RequestAcceptView.as_view(), name='requests_accept'),
    path('requests/decline', views_requests.RequestDeclineView.as_view(), name='requests_decline'),

    path('qr/scan_product/<int:pk>', views_qr.EquipmentListAPIView.as_view(), name='qr_scan_product'),
    path('qr/scan', views_qr.QrScanView.as_view(), name='qr_scan'),
    # path('qr/decline', views_requests.RequestDeclineView.as_view(), name='requests_decline'),
]
