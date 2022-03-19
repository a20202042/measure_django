from django.db import models
import django.utils.timezone as timezone
import datetime, uuid, re
from django.db.models.signals import pre_delete  # image_delet
from django.dispatch.dispatcher import receiver  # image_delet


def path_project(instance, filename):  # 先隱藏圖片上傳
    name = str(instance.project_image)
    x = instance
    return "project/{id}/{file}".format(id=instance.project_name, file=name)  # 儲存路徑和格式


def path_measure_item(instance, filename):
    name = str(instance.image)
    x = instance
    return "project_measure_item/{id}/{file}".format(id=instance.project, file=name)  # 儲存路徑和格式


def path_work_order_measure_item(instance, filename):
    name = str(instance.image)
    return "work_order_measure_item/{id}/{file}".format(id=instance.measurement_work_order.id,
                                                        file=name)  # 儲存路徑和格式


def file_delet(instance, **kwargs):
    instance.project_image.delet(True)


class project(models.Model):
    project_name = models.CharField(max_length=200)  # 專案名稱
    project_create_date = models.DateField(default=timezone.now)  # 專案建立日期
    # https: // www.itread01.com / content / 1545908112.html
    founder_name = models.CharField(max_length=100)  # 建立人
    project_image = models.ImageField(upload_to=path_project)  # 先隱藏圖片上傳
    materials = models.CharField(max_length=100, blank=True)
    manufacturing_machine = models.CharField(max_length=100, blank=True)
    # Class = models.CharField(max_length=100, blank=True)
    remake = models.TextField(max_length=200, blank=True)  # 備註

    def __str__(self):
        return self.project_name


class measuring_tool(models.Model):
    toolname = models.CharField(max_length=50)
    tooltype = models.CharField(max_length=50)
    toolprecision = models.FloatField(max_length=50)
    tooltestdata = models.DateField(default=timezone.now)

    def __str__(self):
        return self.toolname


class measurement_work_order(models.Model):
    project_measure = models.ForeignKey(project, on_delete=models.CASCADE)
    sor_no = models.CharField(max_length=100)  # 工單
    manufacturing_order = models.CharField(max_length=100)
    edition = models.CharField(max_length=100, blank=True)  # 版次
    number_of_parts = models.CharField(max_length=100, blank=True)  # 件數
    create_time = models.DateField(default=timezone.now)
    remake = models.TextField(max_length=200, blank=True)
    measure_state = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.sor_no


class work_order_appearance_defect(models.Model):
    work_order = models.ForeignKey(measurement_work_order, on_delete=models.CASCADE)
    base64_image = models.TextField(max_length=1000000, blank=True)
    part_number = models.TextField(max_length=10)
    remake = models.CharField(max_length=200)

    def __str__(self):
        return self.remake


class work_order_measure_items(models.Model):
    tool_name = models.ForeignKey(measuring_tool, on_delete=models.CASCADE)
    measurement_work_order = models.ForeignKey(measurement_work_order, on_delete=models.CASCADE)
    unit = (('mm', 'mm'), ('in', 'in'),)
    measure_unit = models.CharField(choices=unit, max_length=5)
    measurement_items = models.CharField(max_length=50)  # 量測項目名稱
    upper_limit = models.FloatField(max_length=20)  # 量測數值上限
    lower_limit = models.FloatField(max_length=20)  # 量測數值上限
    specification_center = models.FloatField(max_length=20)  # 量測數值中心
    number = (("1", "1"), ("3", "3"), ("5", "5"), ("7", "7"))
    # measure_points = models.CharField(max_length=20)
    measure_number = models.CharField(choices=number, max_length=5)  # 量測次數
    common_difference = models.CharField(max_length=50)
    # Decimal = ((0.01, 0.01), (0.001, 0.001), (0.0001, 0.0001),)  # 浮點數問題
    # decimal_piaces = models.FloatField(choices=Decimal)  # 量測小數點位數
    image = models.ImageField(upload_to=path_work_order_measure_item)
    image_base64_data = models.TextField(blank=True)

    def __str__(self):
        return self.measurement_items


class measure_items(models.Model):
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    tool_name = models.ForeignKey(measuring_tool, on_delete=models.CASCADE)
    unit = (('mm', 'mm'), ('in', 'in'),)
    measure_unit = models.CharField(choices=unit, max_length=5)
    measurement_items = models.CharField(max_length=50)  # 量測項目名稱
    upper_limit = models.FloatField(max_length=20)  # 量測數值上限
    lower_limit = models.FloatField(max_length=20)  # 量測數值上限
    specification_center = models.FloatField(max_length=20)  # 量測數值中心
    number = (("1", "1"), ("3", "3"), ("5", "5"), ("7", "7"))
    # measure_points = models.CharField(max_length=20)
    measure_number = models.CharField(choices=number, max_length=5)  # 量測次數
    # Decimal = ((0.01, 0.01), (0.001, 0.001), (0.0001, 0.0001),)  # 浮點數問題
    # decimal_piaces = models.FloatField(choices=Decimal)  # 量測小數點位數
    image = models.ImageField(upload_to=path_measure_item)
    image_base64_data = models.TextField(max_length=100000, blank=True)

    def __str__(self):
        return self.measurement_items


class measure_values(models.Model):
    unit = (('mm', 'mm'), ('in', 'in'),)
    measure_project = models.ForeignKey(project, on_delete=models.DO_NOTHING)
    measure_work_order = models.ForeignKey(measurement_work_order, on_delete=models.CASCADE)
    measure_work_order_measure_item = models.ForeignKey(work_order_measure_items, on_delete=models.CASCADE)
    measure_man = models.CharField(max_length=10)
    measure_value = models.FloatField(max_length=20)
    measure_unit = models.CharField(choices=unit, max_length=5)
    measure_time = models.DateTimeField()
    measure_tool = models.ForeignKey(measuring_tool, on_delete=models.DO_NOTHING)
    measure_number = models.CharField(max_length=20)
    time_now = models.DateTimeField(auto_now=True)
    remake = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.measure_man)


class work_order_parts_reamke(models.Model):
    work_order = models.ForeignKey(measurement_work_order, on_delete=models.CASCADE)
    part_number = models.CharField(max_length=200)
    remake = models.TextField(max_length=500, blank=True)
    type = (('type_1', 'type_1'), ('type_2', 'type_2'), ('type_3', 'type_3'),)
    part_type = models.CharField(choices=type, max_length=10)

    def __str__(self):
        return str(self.part_number)

# class measure_image(models.Model):
#     image = models.ImageField(upload_to='measure_item/')
#     def __str__(self):
#         return str(self.measure_item)
