from django.contrib import admin
from .models import measurement_work_order, project, measuring_tool, measure_items, measure_values, \
    work_order_measure_items, work_order_appearance_defect \
    , work_order_parts_reamke


class value(admin.ModelAdmin):
    list_display = ('id', 'measure_work_order', 'measure_work_order_measure_item', 'measure_number', 'measure_value')


admin.site.register(measurement_work_order)
admin.site.register(project)
admin.site.register(measuring_tool)
admin.site.register(measure_items)
admin.site.register(measure_values, value)
admin.site.register(work_order_measure_items)
admin.site.register(work_order_appearance_defect)
admin.site.register(work_order_parts_reamke)
# admin.site.register(measure_image)
# admin.site.register(measure_image)
# Register your models here.
