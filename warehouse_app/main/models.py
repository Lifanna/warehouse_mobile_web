from django.db import models
from django.contrib.auth.models import AbstractUser


class Status(models.Model):
    name = models.CharField("Наименование должности", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


class Department(models.Model):
    name = models.CharField("Наименование отдела", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"


class CustomUser(AbstractUser):
    patronymic = models.CharField("Отчество", max_length=50, null=True, blank=True)

    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Должность", null=True)

    is_admin = models.BooleanField("Администратор приложения", default=False, null=True)

    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Отдел", null=True)


class Producer(models.Model):
    name = models.CharField("Наименование производителя", max_length=255)

    address = models.CharField("Адрес", max_length=255, null=True)

    contact = models.CharField("Контактное лицо", max_length=255, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Warehouse(models.Model):
    name = models.CharField("Наименование склада", max_length=255)

    sectors = models.PositiveIntegerField("Количество секторов", null=True)

    shelves = models.PositiveIntegerField("Количество полок", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"


class Equipment(models.Model):
    name = models.CharField("Наименование оборудования", max_length=255)

    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name="Производитель")

    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name="Склад")

    sector = models.PositiveIntegerField("Номер сектора")

    shelf = models.PositiveIntegerField("Номер полки")

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, verbose_name="Пользователь", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"


class RequestStatus(models.Model):
    name = models.CharField("Наименование статуса", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус заявки"
        verbose_name_plural = "Статусы заявок"


class Request(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name="Оборудование")

    description = models.TextField("Описание")

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Отправитель (автор)")

    status = models.ForeignKey(RequestStatus, on_delete=models.CASCADE, verbose_name="Статус")

    def __str__(self):
        return "Заявка №%s от %s"%(self.pk, self.created_at.strftime('%d.%m.%Y'))

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
