from rest_framework import serializers
from main import models


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Producer
        fields = "__all__"


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Warehouse
        fields = "__all__"


class EquipmentSerializer(serializers.ModelSerializer):
    producer = ProducerSerializer()
    warehouse = WarehouseSerializer()

    class Meta:
        model = models.Equipment
        fields = "__all__"


class EquipmentSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipment
        fields = ('id', 'user',)