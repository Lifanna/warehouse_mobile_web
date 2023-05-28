from django.contrib import admin
from main import models


admin.site.register(models.CustomUser)
admin.site.register(models.Status)
admin.site.register(models.Department)

admin.site.register(models.Equipment)
admin.site.register(models.Warehouse)
admin.site.register(models.Producer)
admin.site.register(models.Request)
admin.site.register(models.RequestStatus)
