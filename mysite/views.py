from django.shortcuts import render
from mysite import models, forms
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
import base64, os, json, statistics, numpy
from django.shortcuts import get_object_or_404

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


# Create your views here.

def main(request):
    return render(request, 'index.html', locals())


def project_display_project(requset, x=None):
    projects = models.project.objects.all()
    return render(requset, 'project_display/project_display_project.html', locals())


def project_display_work_order(requset, x=None):
    work_order = models.measurement_work_order_create.objects.all()
    return render(requset, 'project_display/project_display_work_order.html', locals())


def project_display_tool(requset, x=None):
    tool = models.measuring_tool.objects.all()
    return render(requset, 'project_display/project_display_tool.html', locals())


def project_display_item(requset, x=None):
    item = models.measure_items.objects.all()
    return render(requset, 'project_display/project_display_item.html', locals())


def measure_item_image_show(request, id):
    image_file = models.measure_items.objects.get(id=id)
    print(image_file.image)
    data = dict()
    return JsonResponse(data)


def delet_item(request, id):
    item = models.measure_items.objects.get(id=id)
    data = dict()
    if request.method == 'POST':
        item.delete()
        data['form_is_valid'] = True
        items = models.measure_items.objects.all()
        data['html_item_list'] = render_to_string(
            'project_display/item_banner.html',
            {'item': items})
    else:
        context = {
            'project_measure': item.project_measure, 'id': item.id,
            'tool_name': item.too_name, 'measure_unit': item.measure_unit,
            'measurement_items': item.measurement_items, 'upper_limit': item.upper_limit,
            'lower_limit': item.lower_limit, 'specification_center': item.specification_center,
            'measure_points': item.measure_points, 'measure_number': item.measure_number,
            'decimal_piaces': item.decimal_piaces, 'image': item.image
        }
        data['html_form'] = render_to_string(
            'project_display/delet/delet_item.html',
            context, request=request)
    return JsonResponse(data)


def delet_tool(request, id):
    tool = models.measuring_tool.objects.get(id=id)
    data = dict()
    if request.method == "POST":
        tool.delete()
        data['form_is_valid'] = True
        tools = models.measuring_tool.objects.all()
        data['html_tool_list'] = render_to_string(
            'project_display/tool_banner.html',
            {'tool': tools})
    else:
        context = {
            'tool_name': tool.toolname, 'id': tool.id,
            'tooltype': tool.tooltype, 'toolprecision': tool.toolprecision,
            'tooltestdata': tool.tooltestdata
        }
        data['html_form'] = render_to_string(
            'project_display/delet/delet_tool.html',
            context, request=request)

    return JsonResponse(data)


# def delet_work_order(request, id):
#     work_order = models.measurement_work_order_create.objects.get(id=id)
#     data = dict()
#     if request.method == 'POST':
#         work_order.delete()
#         data['form_is_valid'] = True
#         work_orders = models.measurement_work_order_create.objects.all()
#         data['html_work_order_list'] = render_to_string(
#             'project_display/work_order_banner.html',
#             {'work_order': work_orders})
#     else:
#         context = {
#             'project': work_order.project_measure,
#             'work_order': work_order.sor_no, 'id': work_order.id,
#             'number_of_parts': work_order.part_no, 'materials': work_order.materials,
#             'manufacturing_machine': work_order.manufacturing_machine, 'batch_number': work_order.batch_number,
#             'Class': work_order.Class, 'inspector': work_order.inspector,
#             'remake': work_order.remake
#         }
#         data['html_form'] = render_to_string(
#             'project_display/delet/delet_work_order.html',
#             context, request=request)
#
#     return JsonResponse(data)


def update_work_order(request, id):
    # work_order = get_object_or_404(models.measurement_work_order_create, id=id)
    work_order = models.measurement_work_order_create.objects.get(id=id)
    data = dict()
    if request.method == 'POST':
        form = forms.Work_order(request.POST, instance=work_order)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            work_orders = models.measurement_work_order_create.objects.all()
            data['html_work_order_list'] = render_to_string(
                'project_display/work_order_banner.html',
                {'work_order': work_orders})
    else:
        form = forms.Work_order(instance=work_order)
    context = {'form': form}
    data['html_form'] = render_to_string(
        'project_display/update/update_work_order.html',
        context, request=request)
    return JsonResponse(data)


def update_tool(request, id):
    tool = get_object_or_404(models.measuring_tool, id=id)
    data = dict()
    if request.method == 'POST':
        form = forms.measure_tool(request.POST, instance=tool)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            tools = models.measuring_tool.objects.all()
            data['html_tool_list'] = render_to_string(
                'project_display/tool_banner.html',
                {'tool': tools})
    else:
        form = forms.measure_tool(instance=tool)
    context = {'form': form}
    data['html_form'] = render_to_string(
        'project_display/update/update_tool.html',
        context, request=request)
    return JsonResponse(data)


def update_item(request, id):
    item = models.measure_items.objects.get(id=id)
    data = dict()
    if request.method == 'POST':
        form = forms.measure_item(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            items = models.measure_items.objects.all()
            data['html_item_list'] = render_to_string(
                'project_display/item_banner.html',
                {'item': items}
            )
    else:
        form = forms.measure_item(instance=item)
    context = {'form': form}
    data['html_form'] = render_to_string(
        'project_display/update/update_measure.html',
        context, request=request)

    return JsonResponse(data)


# 2021 將專案修改
def project_menage(request):
    projects = models.project.objects.all()
    project_form = forms.Project()
    if request.method == 'POST':
        project_form = forms.Project(request.POST, request.FILES)
        if project_form.is_valid():
            project_form.save()
            return HttpResponseRedirect('/project_menage')
    return render(request, 'form/form_project.html', locals())


def create_measure_item(request, id):
    measure_item_from = forms.measure_item(initial={'project': str(id)})
    project_measure_items = models.measure_items.objects.filter(project=id).values()
    project = models.project.objects.get(id=id)
    if request.method == 'POST':
        measure_item_from = forms.measure_item(request.POST, request.FILES)
        if measure_item_from.is_valid():
            measure_item_from.save()
            image_url = str(measure_item_from.instance.image.file)
            print(image_url)
            with open(image_url, 'rb') as file:
                image = file.read()
                image_base64_data = base64.b64encode(image)
                image_base64_data = str(image_base64_data, 'utf-8')
                measure_id = models.measure_items.objects.latest('id').id
                measure_item = models.measure_items.objects.get(id=measure_id)
                measure_item.image_base64_data = image_base64_data
                measure_item.save()
            return HttpResponseRedirect('/project_menage/create_measure_item/' + id)
    return render(request, 'project_measure_item_create/project_id_measure_item_create.html', locals())


def project_item_delet_js(request, id):
    print("delet")
    project_item = models.measure_items.objects.get(id=id)
    data = dict()
    print(id)
    if request.method == 'POST':
        data['form_is_valid'] = True
        project_id = models.measure_items.objects.get(id=id).project_id
        print(project_id)
        project_item.delete()
        project_measure_items = models.measure_items.objects.filter(project_id=project_id).all()
        data['html_project_item_list'] = render_to_string(
            'project_measure_item_create/project_item_banner.html',
            {'project_measure_items': project_measure_items}
        )
    else:
        context = {'id': id,
                   'measure_item': project_item.measurement_items
                   }
        data['html_form'] = render_to_string(
            'project_measure_item_create/delet_project_measure_item_js.html', context,
            request=request)
    return JsonResponse(data)


def project_measure_item_update_js(request, id):
    print(id)
    measure_item = get_object_or_404(models.measure_items, id=id)
    data = dict()
    if request.method == 'POST':
        form = forms.measure_item(request.POST, instance=measure_item)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            project_id = models.measure_items.objects.get(id=id).project_id
            print(project_id)
            project_measure_items = models.measure_items.objects.filter(project_id=project_id).all()
            data['html_project_item_list'] = render_to_string('project_measure_item_create/project_item_banner.html',
                                                              {'project_measure_items': project_measure_items})
    else:
        form = forms.measure_item(instance=measure_item)
        context = {'form': form}
        data['html_form'] = render_to_string('project_measure_item_create/update_project_measure_item.html', context,
                                             request=request)
    return JsonResponse(data)


def project_create(request):
    if request.method == 'POST':
        form = forms.Project(request.POST)
    else:
        form = forms.Project()
    return save_project_form(request, form, 'project_display/partial_project_create.html')


def save_project_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            projects = models.project.objects.all()
            data['html_project_list'] = render_to_string(
                'project_display/project_banner.html',
                {'projects': projects})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def delet_project(request, id):
    project = models.project.objects.get(id=id)
    data = dict()
    if request.method == 'POST':
        print(project.project_image)
        # models.file_delet(project.project_image)
        project.delete()
        data['form_is_valid'] = True
        projects = models.project.objects.all()
        data['html_project_list'] = render_to_string(
            'project_display/project_banner.html',
            {'projects': projects})
    else:
        context = {'project': project,
                   'project_name': project.project_name,
                   'founder_name': project.founder_name,
                   'time': project.project_create_date,
                   'remake': project.remake,
                   'project_image': project.project_image}
        data['html_form'] = render_to_string(
            'project_display/delet/delet_project.html',
            context, request=request)
    return JsonResponse(data)


def update_project(request, id):
    project = get_object_or_404(models.project, id=id)
    data = dict()
    if request.method == 'POST':
        form = forms.Project(request.POST, instance=project)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            projects = models.project.objects.all()
            data['html_project_list'] = render_to_string(
                'project_display/project_banner.html',
                {'projects': projects})
    else:
        form = forms.Project(instance=project)
    context = {'form': form}
    data['html_form'] = render_to_string(
        'project_display/update/update_project.html',
        context, request=request)
    return JsonResponse(data)


def work_order_display(request):
    work_order_form = forms.Work_order()
    work_orders = models.measurement_work_order.objects.all()
    if request.method == 'POST':
        work_order_form = forms.Work_order(request.POST)
        if work_order_form.is_valid():
            work_order_form.save()
            insert_work_order = models.measurement_work_order.objects.latest('id')
            insert_work_order_id = insert_work_order.id
            insert_work_order_project = insert_work_order.project_measure_id
            measure_items = models.measure_items.objects.filter(project=insert_work_order_project).values()
            for project_measure_item in measure_items:
                work_order_measure_item = models.work_order_measure_items(
                    tool_name_id=project_measure_item['tool_name_id'],
                    measure_unit=project_measure_item['measure_unit'],
                    measurement_items=project_measure_item['measurement_items'],
                    upper_limit=project_measure_item['upper_limit'],
                    lower_limit=project_measure_item['lower_limit'],
                    specification_center=project_measure_item['specification_center'],
                    measure_number=project_measure_item['measure_number'],
                    # decimal_piaces=project_measure_item['decimal_piaces'],
                    image=project_measure_item['image'],
                    measurement_work_order_id=insert_work_order_id
                )
                work_order_measure_item.save()
                # print(project_measure_item)
            work_order_number = insert_work_order.number_of_parts
            for i in range(1, int(work_order_number) + 1):
                work_order_parts_remake = models.work_order_parts_reamke(remake='', work_order_id=insert_work_order_id,
                                                                         part_number=i)
                work_order_parts_remake.save()
            return HttpResponseRedirect('/work_order')
    return render(request, 'work_order/work_order_display.html', locals())


def work_order(request):
    work_order_form = forms.Work_order()
    if request.method == 'POST':
        work_order_form = forms.Work_order(request.POST)
        if work_order_form.is_valid():
            work_order_form.save()
            return HttpResponseRedirect('/form_measure_tool')
    return render(request, 'form/from_work_order_create.html', locals())


def work_order_delet(request, id):
    work_order = models.measurement_work_order.objects.get(id=id)
    data = dict()
    if request.method == 'POST':
        work_order.delete()
        data['form_is_valid'] = True
        work_orders = models.measurement_work_order.objects.all()
        data['html_item_list'] = render_to_string('work_order/work_order_banner.html', {'work_orders': work_orders})
    else:
        context = {'work_order': work_order}
        data['html_form'] = render_to_string('work_order/work_order_delet_js.html',
                                             context, request=request)
    return JsonResponse(data)


def work_order_update(request, id):
    work_order = get_object_or_404(models.measurement_work_order, id=id)
    data = dict()
    if request.method == 'POST':
        form = forms.Work_order(request.POST, instance=work_order)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            work_orders = models.measurement_work_order.objects.all()
            data['html_item_list'] = render_to_string('work_order/work_order_banner.html', {'work_orders': work_orders})
            work_order_parts_remake = models.work_order_parts_reamke.objects.filter(work_order_id=id)
            work_order_parts_remake.delete()
            part_number = work_order.number_of_parts
            for i in range(1, int(part_number) + 1):
                work_order_parts_remake = models.work_order_parts_reamke(remake='', work_order_id=id,
                                                                         part_number=i)
                work_order_parts_remake.save()
    else:
        form = forms.Work_order(instance=work_order)
    context = {'form': form}
    data['html_form'] = render_to_string('work_order/work_order_update.html', context, request=request)
    return JsonResponse(data)
    # print(id)


def work_measure_item_display(request, id):
    project_id = models.measurement_work_order.objects.get(id=id).project_measure_id
    project = models.project.objects.get(id=project_id)
    work_order_measure_items = models.work_order_measure_items.objects.filter(measurement_work_order_id=id).values()
    return render(request, 'work_order_item/work_order_measure_item.html', locals())


def work_order_item_delet_js(request, id):
    work_order_item = models.work_order_measure_items.objects.get(id=id)
    data = dict()
    if request.method == 'POST':
        data['form_is_valid'] = True
        work_id = models.work_order_measure_items.objects.get(id=id).measurement_work_order_id
        work_order_item.delete()
        work_order_measure_items = models.work_order_measure_items.objects.filter(
            measurement_work_order_id=work_id)
        data['html_item_list'] = render_to_string('work_order_item/work_order_measure_item_banner.html',
                                                  {'work_order_measure_items': work_order_measure_items})
    else:
        context = {'work_order_item': work_order_item}
        data['html_form'] = render_to_string('work_order_item/work_order_delet_js.html', context, request=request)
    return JsonResponse(data)


def work_order_measure_item_update(request, id):
    work_measure_item = get_object_or_404(models.work_order_measure_items, id=id)
    data = dict()
    if request.method == 'POST':
        form = forms.work_measure_item(request.POST, instance=work_measure_item)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            work_id = models.work_order_measure_items.objects.get(id=id).measurement_work_order_id
            work_order_measure_items = models.work_order_measure_items.objects.filter(
                measurement_work_order_id=work_id)
            data['html_item_list'] = render_to_string('work_order_item/work_order_measure_item_banner.html',
                                                      {"work_order_measure_items": work_order_measure_items})
    else:
        form = forms.work_measure_item(instance=work_measure_item)
    context = {"form": form}
    data['html_form'] = render_to_string('work_order_item/work_order_measure_item_update_js.html', context,
                                         request=request)
    return JsonResponse(data)


def measure_work_order_data_display(request):
    measure_value = models.measure_values.objects.all()
    # print(measure_value)
    work_order_id_all = []
    work_order_all = []
    data = {}
    for item in measure_value:  # 蒐集工單
        if item.measure_work_order_id not in work_order_id_all:
            work_order_id_all.append(item.measure_work_order_id)
            data['work_order'] = item.measure_work_order.sor_no
            data['project_name'] = item.measure_project.project_name
            data['measure_man'] = item.measure_man
            data['founder_name'] = item.measure_project.founder_name
            data['measure_time'] = item.measure_time
            data['create_time'] = item.time_now
            data['number_of_parts'] = item.measure_work_order.number_of_parts
            data['work_order_id'] = item.measure_work_order.id
            data['manufacturing_order'] = item.measure_work_order.manufacturing_order
            print(data)
            work_order_all.append(data)
            data = {}
    print(work_order_all)
    # print(item.measure_work_order_id)
    return render(request, 'measure_work_order_data_display/work_order_main.html', locals())


def save_appearance_image(file_name, base64_data):
    file_url = 'media/work_order_appearance_affect/%s.jpg' % file_name
    jiema = open(file_url, 'wb')
    base64_data = base64.b64decode(base64_data)
    jiema.write(base64_data)
    jiema.close()


def work_order_measure_data_form(request, id):
    print(id)
    project_id = models.measurement_work_order.objects.get(id=id).project_measure_id
    project = models.project.objects.get(id=project_id)
    project_image = models.project.objects.get(id=project_id).project_image
    project_name = models.project.objects.get(id=project_id).project_name
    w = models.measurement_work_order.objects.get(id=id)
    work_order_measure_items = models.work_order_measure_items.objects.filter(measurement_work_order_id=id).all()
    measure_values = models.measure_values.objects.filter(measure_work_order_id=id).all()
    measure_values_data = []
    number_of_parts = w.number_of_parts
    part_remake = models.work_order_parts_reamke.objects.filter(work_order_id=id)
    # -------------------
    # 圖片儲存
    appearance_all = models.work_order_appearance_defect.objects.filter(work_order_id=id)
    for item in appearance_all:
        save_appearance_image(item.id, item.base64_image)

    # save_appearance_image()
    # -----------------
    for item in measure_values:
        measure_man = item.measure_man
        measure_time = item.measure_time
    for item in work_order_measure_items:
        work_order_item = models.work_order_measure_items.objects.get(id=item.id)
        upper = item.upper_limit
        lower = item.lower_limit
        center = item.specification_center
        upper_tolerance, lower_tolerance = float(upper) - float(center), float(center) - float(lower)
        tolerance = "+%s/-%s" % (upper_tolerance, lower_tolerance)
        work_order_item.common_difference = tolerance
        work_order_item.save()
    all_data_or = [{'part_number': [{'item': '123', 'm': 123}, {'item': '123', 'm': 123}]},
                   {'part_number': [{'item': '123', 'm': 123}]},
                   [{'part_number': [{'item': '123', 'm': 123}]}]]
    # -----------良率
    no_go = False
    nogo_list = []
    go_list = []
    for number in range(1, int(number_of_parts) + 1):  # 件數
        no_go = False
        for value in measure_values:  # 數據
            if str(number) == list(value.measure_number)[0]:  # 判別第幾件
                measure_item = models.work_order_measure_items.objects.get(id=value.measure_work_order_measure_item_id)
                upper = measure_item.upper_limit
                lower = measure_item.lower_limit
                if value.measure_value > upper or value.measure_value < lower:
                    no_go = True
                    break
                else:
                    pass
        if no_go == True:
            nogo_list.append(no_go)
        elif no_go == False:
            go_list.append(no_go)
    # print(nogo_list)
    Yield = len(go_list) / (len(go_list) + len(nogo_list))
    no_yield = len(nogo_list) / (len(go_list) + len(nogo_list))
    number_yield = len(go_list)
    number_no_yield = len(nogo_list)
    number_all = len(go_list) + len(nogo_list)

    all_data = []
    measure_number = []
    for number in range(1, int(number_of_parts) + 1):  # 件數
        n = 1
        data = {}
        item = []
        for value in measure_values:  # 數據
            if str(number) == list(value.measure_number)[0]:  # 判別第幾件
                measure_item = models.work_order_measure_items.objects.get(id=value.measure_work_order_measure_item_id)
                up_range = float(measure_item.upper_limit)
                low_range = float(measure_item.lower_limit)
                value_range = float(value.measure_value)
                if value_range < low_range or value_range > up_range:
                    data['GO'] = 'NOGO'
                else:
                    data['GO'] = 'GO'
                if value.measure_unit == 'mm':
                    center = round(float(measure_item.specification_center), 4)
                    upper = round(float(measure_item.upper_limit), 4)
                    lower = float(measure_item.lower_limit)
                    print(round(upper - center, 4))
                    tolerance = "+%s/-%s" % (round(upper - center, 4), round(center - lower, 4))
                    data['tolerance_mm'] = tolerance
                    data['center_mm'] = measure_item.specification_center
                    data['upper_mm'] = measure_item.upper_limit
                    data['lower_mm'] = measure_item.lower_limit
                    data['measure_item_name'] = measure_item.measurement_items
                    data['value_mm'] = value.measure_value
                    data['value_in'] = round(float(value.measure_value) / 25.4, 4)
                    data['center_in'] = round(float(measure_item.specification_center) / 25.4, 4)
                    data['upper_in'] = round(float(measure_item.upper_limit) / 25.4, 4)
                    data['lower_in'] = round(float(measure_item.lower_limit) / 25.4, 4)
                    data['measure_tool'] = measure_item.tool_name
                    data['tolerance_in'] = '+%s/-%s' % (
                        round(
                            (float(measure_item.upper_limit) / 25.4 - float(measure_item.specification_center) / 25.4),
                            3),
                        round(float(measure_item.specification_center) / 25.4 - float(measure_item.lower_limit) / 25.4,
                              3))
                    measure_item_number = list(value.measure_number)[-1]
                    # data['number'] = '%s - %s' % (n, measure_item_number)
                    data['number'] = n
                elif value.measure_unit == 'in':
                    center = float(measure_item.specification_center)
                    upper = float(measure_item.upper_limit)
                    lower = float(measure_item.lower_limit)
                    tolerance = "+%s/-%s" % (round(upper - center, 3), round(center - lower, 3))
                    data['measure_tool'] = measure_item.tool_name
                    data['tolerance_in'] = tolerance
                    data['center_in'] = measure_item.specification_center
                    data['upper_in'] = measure_item.upper_limit
                    data['lower_in'] = measure_item.lower_limit
                    data['measure_item_name'] = measure_item.measurement_items
                    data['value_in'] = value.measure_value
                    data['value_mm'] = round(float(value.measure_value) * 25.4, 3)
                    data['center_mm'] = round(float(measure_item.specification_center) * 25.4, 3)
                    data['upper_mm'] = round(float(measure_item.upper_limit) * 25.4, 3)
                    data['lower_mm'] = round(float(measure_item.lower_limit) * 25.4, 3)
                    data['tolerance_mm'] = '+%s/-%s' % (
                        round(
                            (float(measure_item.upper_limit) * 25.4 - float(measure_item.specification_center) * 25.4),
                            3),
                        round(float(measure_item.specification_center) * 25.4 - float(measure_item.lower_limit) * 25.4,
                              3))
                    measure_item_number = list(value.measure_number)[-1]
                    # data['number'] = '%s - %s' % (n, measure_item_number)
                    data['number'] = n
                # print(data['appearence_image'])
                item.append(data.copy())
                n = n + 1
            # if str(number) == list(value.measure_number)[0]:

        all_data.append(
            {'part_number': item, 'number': str(number)})
    print(all_data)
    return render(request, 'measure_work_order_data_display/work_order_data_display.html', locals())


def work_order_form_update_parts_remake(request, id):
    part_remake = get_object_or_404(models.work_order_parts_reamke, id=id)
    data = dict()
    print(id)
    if request.method == 'POST':
        form = forms.work_part_remake(request.POST, instance=part_remake)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            work_id = part_remake.work_order_id
            part_remake = models.work_order_parts_reamke.objects.all()
            print(part_remake)
            data['html_remake_list'] = render_to_string(
                'measure_work_order_data_display/part_remake_banner.html',
                {'part_remake': part_remake})
            work_order_measure_data_form(request, work_id)
    else:
        form = forms.work_part_remake(instance=part_remake)
        context = {'form': form}
        data['html_form'] = render_to_string('measure_work_order_data_display/work_order_part_remake_update.html', context,
                                         request=request)
    return JsonResponse(data)


# 2021

def measure_tool(request):
    measure_tool_form = forms.measure_tool()
    if request.method == 'POST':
        measure_tool_form = forms.measure_tool(request.POST)
        if measure_tool_form.is_valid():
            measure_tool_form.save()
        return HttpResponseRedirect('/form_measure_item')
    return render(request, 'form/form_measure_tool.html', locals())


def measure_item(request):
    measure_item_form = forms.measure_item()
    # try:
    if request.method == 'POST':
        measure_item_form = forms.measure_item(request.POST, request.FILES)
        if measure_item_form.is_valid():
            measure_item_form.save()
            image_url = str(measure_item_form.instance.image.file)
            print(image_url)
            with open(image_url, "rb") as file:
                image = file.read()
                image_base64_data = base64.b64encode(image)
                image_base64_data = str(image_base64_data, "utf-8")
                measure_name = request.POST["measurement_items"]
                measure_item = models.measure_items.objects.get(measurement_items=measure_name)
                measure_item.image_base64_data = image_base64_data
                measure_item.save()
        return HttpResponseRedirect('/form_measure_item')
    # except:pass
    return render(request, 'form/form_measure_item.html', locals())


def test(requset):
    all_data = models.measure_values.objects.filter(measure_name_id=98).values('measure_number', 'measure_value')
    measure_item_data = models.measure_items.objects.get(id=62)
    x_line = []
    y_line = []
    x_exceed_data = []
    y_exceed_data = []
    upper_limit = measure_item_data.upper_limit
    lower_limit = measure_item_data.lower_limit
    for item in all_data:
        y_line.append(item['measure_value'])
        x_line.append(item['measure_number'])
        if item['measure_value'] > upper_limit or item['measure_value'] < lower_limit:
            x_exceed_data.append(item['measure_number'])
            y_exceed_data.append(item['measure_value'])
    x_max = str(x_line[-1])
    x_min = str(x_line[0])
    y_center = float(float(lower_limit) + ((float(upper_limit) - float(lower_limit)) / 2))
    upper_range = float(float(upper_limit) + ((float(upper_limit) - float(lower_limit)) / 2))
    loewr_range = float(float(lower_limit) - ((float(upper_limit) - float(lower_limit)) / 2))
    y = [1, 1.555, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    x = ['1-1', '1-2', '1-3', '2-1', '2-2', '2-3', '3-1', '3-2', '3-3', '4-1', '4-2', '4-3', '5-1', '5-2', '5-3', '6-1',
         '6-2', '6-3']
    data = {'x_data': json.dumps(x_line), 'y_data': json.dumps(y_line),
            'x_max': json.dumps(x_max), 'x_min': json.dumps(x_min), 'y_center': json.dumps(y_center),
            'upper_limit': json.dumps(upper_limit), 'lower_limit': json.dumps(lower_limit),
            'upper_range': json.dumps(upper_range), 'lower_range': json.dumps(loewr_range),
            'x_exceed_data': json.dumps(x_exceed_data), 'y_exceed_data': json.dumps(y_exceed_data)}
    # print(y_center)
    # print(upper_limit)
    # print(lower_limit)
    # print(y_line)
    # print(x_line)
    # print(x_max)
    # print(x_min)
    # ----------------------------------------------------------------rbar
    print('r')
    n = models.measure_items.objects.get(id=57).measure_number  # 量測次數
    print(n)
    d3_data = {'1': 1, '3': 0, '5': 0, '7': 0.076}
    d4_data = {'1': 1, '3': 2.575, '5': 2.115, '7': 1.924}
    r_all_data = []
    r_old_data = []
    r_r_data = []
    r_x_line = []
    # x軸座標
    r_number = int()
    r_r_cl = float()
    for item in all_data:
        r_old_data.append(item['measure_value'])
        r_number = r_number + 1
        if r_number == int(n):
            r_all_data.append(r_old_data)
            r_old_data = []
            r_number = 0
    print(r_all_data)  # 平均數data
    for item in r_all_data:
        r_r_data.append(numpy.max(item) - numpy.min(item))
    print(r_r_data)
    r_r_cl = statistics.mean(r_r_data)
    print(r_r_cl)  # 平均數
    d4 = d4_data[n]
    d3 = d3_data[n]
    r_ucl = r_r_cl * d4
    r_lcl = r_r_cl * d3
    r_upper_range = r_r_cl * d4 + (r_r_cl * d4) / 3
    r_lower_range = r_r_cl * d3 + (r_r_cl * d3) / 3
    print(r_r_cl, r_ucl, r_lcl)
    for i in range(1, len(r_r_data) + 1):
        r_x_line.append('(%s)' % i)  # x軸
    print(r_x_line)
    data.update({
        'r_x_data': json.dumps(r_x_line), 'r_y_data': json.dumps(r_r_data),
        'r_x_max': json.dumps(r_x_line[-1]), 'r_x_min': json.dumps(r_x_line[0]),
        'r_r_cl': json.dumps(r_r_cl), 'r_ucl': json.dumps(r_ucl), 'r_lcl': json.dumps(r_lcl),
        'r_upper_range': json.dumps(r_upper_range), 'r_lower_range': json.dumps(r_lower_range)})

    # ----------------------------------------------------------------xbar
    print('x')
    n = models.measure_items.objects.get(id=57).measure_number  # 量測次數
    print(all_data, n)
    A2_data = {'1': 1, '3': 1.023}
    A2 = A2_data[n]
    print(A2)
    x_all_data = []  # 所有資料
    x_x_line = []  # x軸位數
    average_data = []  # 算數平均數
    number = int()
    x_old_data = []
    for item in all_data:
        x_old_data.append(item['measure_value'])
        number = number + 1
        if number == int(n):
            number = 0
            x_all_data.append(x_old_data)
            x_old_data = []
    print(x_all_data)
    for i in range(1, len(x_all_data) + 1):
        x_x_line.append('(%s)' % i)
    print(x_x_line)  # x軸位數
    for item in x_all_data:
        average_data.append(statistics.mean(item))  # 量測平均值data
    print(average_data)
    # 計算全距 = R
    R = float()
    x_r_data = []  # R全距all_data
    for item in x_all_data:
        x_r_data.append(numpy.max(item) - numpy.min(item))
    R = statistics.mean(x_r_data)
    # 計算總平均 = 中心線 = cl
    x_cl = statistics.mean(average_data)
    x_lcl = x_cl - A2 * R
    x_ucl = x_cl + A2 * R
    print(x_cl, x_lcl, x_ucl)
    x_upper_range = x_cl + A2 * R * 2
    x_lower_range = x_cl - A2 * R * 2
    data.update({
        'x_x_data': json.dumps(x_x_line), 'x_y_data': json.dumps(average_data),
        'x_x_max': json.dumps(x_x_line[-1]), 'x_x_min': json.dumps(x_x_line[0]),
        'x_y_center': json.dumps(x_cl), 'x_ucl': json.dumps(x_ucl),
        'x_lcl': json.dumps(x_lcl), 'x_upper_range': json.dumps(x_upper_range),
        'x_lower_range': json.dumps(x_lower_range)})
    print(data)
    return render(requset, 'test.html', data)


def test_1(requset):
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    value = {'x': x, 'y': y}
    print('2')
    return JsonResponse(value)


def data_display_project(request):
    time = []
    project = []
    data = {}
    all_data = []
    value_data = []
    value_number = int()
    measure_value = models.measure_values.objects.all()
    # for i in measure_value:
    #     value_data.append(i.measure_value)
    #     value_number = len(value_data)/int(models.measure_items.objects.get(project_measure_id=i.measure_project_id).measure_number)
    # print(value_number)
    for i in measure_value:
        if i.measure_project not in project:
            measure_id = models.measure_items.objects.filter(project_measure_id=i.measure_project_id).values('id')
            data['project'] = i.measure_project.project_name
            data['project_id'] = i.measure_project.id
            data['value_update_time'] = i.time_now
            data['work_order'] = models.measurement_work_order_create.objects.get(
                project_measure_id=i.measure_project_id).sor_no
            data['number_of_parts'] = models.measurement_work_order_create.objects.get(
                project_measure_id=i.measure_project_id).number_of_parts
            data['founder_name'] = models.project.objects.get(id=i.measure_project_id).founder_name
            data['measure_man'] = i.measure_man
            data['project_create_time'] = models.project.objects.get(id=i.measure_project_id).project_create_date
            data['measure_number'] = value_number
            data['number'] = int(len(models.measure_values.objects.filter(measure_name_id=measure_id[0]['id']).values(
                'measure_value')) / int(models.measure_items.objects.get(id=measure_id[0]['id']).measure_number))
            time.append(i.time_now)
            project.append(i.measure_project)
            # print(len(models.measure_values.objects.filter(measure_project_id=i.measure_project_id))/
            #           int(models.measure_items.objects.get(project_measure_id=i.measure_project_id).measure_number))
            all_data.append(data)
            data = {}
        else:
            pass

    return render(request, 'data_display/data_display_timely.html', locals())


def measure_data_display_show(request, id):
    if request.method == 'GET':
        print('get')
    return render(request, 'data_display/data_display_main/data_display_main.html', locals())


def display_all_measure_data_chart(request, id):
    measure_item = models.measure_items.objects.filter(project_measure_id=id).values('id')
    project_name = models.project.objects.get(id=id).project_name
    man = models.project.objects.get(id=id).founder_name
    # print(man)
    create_date = models.project.objects.get(id=id).project_create_date
    remake = models.project.objects.get(id=id).remake
    project_imag_url = models.project.objects.get(id=id).project_image
    measure_value_man_id = models.measure_values.objects.filter(measure_project_id=id).values('measure_man', 'time_now')
    measure_man = measure_value_man_id[0]['measure_man']
    update_time = measure_value_man_id[0]['time_now']
    measure_count = len(models.measure_values.objects.filter(measure_project_id=id).values('measure_value')) \
                    / int(
        models.measure_items.objects.filter(project_measure_id=id).values('measure_number')[0]['measure_number'])
    # print(measure_count)
    project_data = {'project_name ': project_name, 'man': man,
                    'create_date': create_date, 'remake': remake,
                    'project_image_url': project_imag_url, 'measure_man': measure_man,
                    'update_time': update_time, 'number_of_pieces': str(measure_count)}

    # ----------------------------
    all_data = []
    item_data = []
    chart_data = []
    a2_data = {'1': 1, '3': 1.023, '5': 0.577, '7': 0.419}
    d4_data = {'1': 1, '3': 2.575, '5': 2.115, '7': 1.924}
    d3_data = {'1': 1, '3': 0, '5': 0, '7': 0.076}
    for item in measure_item:
        item_id = item['id']
        data = dict()
        item_id_x = '%s_x' % item['id']
        item_id_r = '%s_r' % item['id']
        h_name = '%s_h' % item['id']
        measure_count = models.measure_items.objects.get(id=item['id']).measure_number
        item_name = models.measure_items.objects.get(id=item['id']).measurement_items
        # print(item_name)
        x_y_data = []  # 每組資料平均值
        r_y_data = []  # 每組資料全距
        x_x_viol_data = []
        x_y_viol_data = []
        value_data = []
        all_value_data = []
        x_x_data = []
        number = int()
        measure_value_dcit = models.measure_values.objects.filter(measure_name_id=item['id']). \
            values('measure_value', 'measure_number')
        for i in measure_value_dcit:
            # print(i['measure_value'])
            value_data.append(i["measure_value"])
            number = number + 1
            if number == int(measure_count):
                number = 0
                all_value_data.append(value_data)
                value_data = []
        measure_number = int(len(measure_value_dcit) / int(measure_count))  # 多少量測次數
        for i in range(1, measure_number + 1):
            x_x_data.append(round(i, 3))
        for i in all_value_data:
            x_y_data.append(round(statistics.mean(i), 3))  # 平均值
            r_y_data.append(numpy.max(i) - numpy.min(i))
        r = statistics.mean(r_y_data)
        x = statistics.mean(x_y_data)
        # print(measure_count)
        a2 = a2_data[str(measure_count)]
        x_ucl = round(x + a2 * r, 3)  # x上限計算
        x_lcl = round(x - a2 * r, 3)  # x下限計算
        r = round(statistics.mean(r_y_data), 3)
        x = round(statistics.mean(x_y_data), 3)
        for i in x_y_data:
            if i < x_lcl or i > x_ucl:
                x_y_viol_data.append(i)
                x_x_viol_data.append(x_x_data[x_y_data.index(i)])
        x_x_cl_data = [x_x_data[0], x_x_data[-1], '', x_x_data[0], x_x_data[-1]]
        x_y_cl_data = [x_ucl, x_ucl, '', x_lcl, x_lcl]
        x_x_center_data = [x_x_data[0], x_x_data[-1]]
        x_y_center_data = [x, x]
        x_y_range = [x_lcl - (x_ucl - x_lcl) / 3, x_ucl + (x_ucl - x_lcl) / 3]
        # --------------------------------------------
        d4 = d4_data[str(measure_count)]
        d3 = d3_data[str(measure_count)]
        r_ucl = round(d4 * r, 3)
        r_lcl = round(d3 * r, 3)
        r_x_cl_data = [x_x_data[0], x_x_data[-1], '', x_x_data[0], x_x_data[-1]]
        r_y_cl_data = [r_ucl, r_ucl, '', r_lcl, r_lcl]
        r_x_viol_data = []
        r_y_viol_data = []
        r_x_center_data = [x_x_data[0], x_x_data[-1]]
        r_y_range_data = [0, r_ucl + r_ucl / 10]
        if r_lcl == 0:
            r_y_center_data = [0, 0]
        else:
            r_y_center_data = [statistics.mean(r_y_data)]
        for i in r_y_data:
            if i > r_ucl or i < r_lcl:
                r_x_viol_data.append(x_x_data[r_y_data.index(i)])
                r_y_viol_data.append(i)
        # ----------------------------------------------
        count_x_data = []
        count_y_data = []
        count_x_data = []
        count_y_data = []
        count_viol_x_data = []
        count_viol_y_data = []
        count_x_center_data = []
        count_y_center_data = []
        count_viol_x_data = []
        count_viol_y_data = []
        count_range_x = []
        item_upper = float(models.measure_items.objects.get(id=item['id']).upper_limit)
        item_lower = float(models.measure_items.objects.get(id=item['id']).lower_limit)
        item_center = float(models.measure_items.objects.get(id=item['id']).specification_center)
        count_all_data = models.measure_values.objects.filter(measure_name_id=item['id']). \
            values('measure_value', 'measure_number')
        for i in count_all_data:
            # print(item_2['measure_value'], item_2['measure_number'])
            count_x_data.append(i['measure_number'])
            count_y_data.append(i['measure_value'])
            if i['measure_value'] > item_upper or i['measure_value'] < item_lower:
                count_viol_x_data.append(i['measure_number'])
                count_viol_y_data.append(i['measure_value'])
        count_x_center_data = [count_x_data[0], count_x_data[-1]]  # 中心線1-1
        count_y_center_data = [item_center, item_center]  # 中心線數值
        count_cl_x_data = [count_x_data[0], count_x_data[-1], '', count_x_data[0], count_x_data[-1]]
        count_cl_y_data = [item_upper, item_upper, '', item_lower, item_lower]
        count_range_x = [item_lower - (item_upper - item_lower) / 6, item_upper + (item_upper - item_lower) / 6]
        item_id_c = "%s_c" % item['id']
        # -----------------------------------------------
        measure_value_data = []
        # print(measure_value_dcit)
        for i in measure_value_dcit:
            measure_value_data.append(i['measure_value'])
        # print(measure_value_data)
        # print(numpy.max(measure_value_data), numpy.min(measure_value_data))
        # print((numpy.max(measure_value_data) - numpy.min(measure_value_data))/11)
        # h_maxmin_data = [numpy.max(measure_value_data), numpy.min(measure_value_data)]
        h_max_min = numpy.linspace(numpy.min(measure_value_data), numpy.max(measure_value_data), num=12)
        h_range = []
        h_range_old_data = []
        h_all_data = []
        h_t_x_data = []
        h_t_y_data = []
        h_y_range = []
        for i in h_max_min:
            h_range_old_data.append(round(i, 4))
        for i in range(0, 11, 1):
            h_range.append([h_range_old_data[i], h_range_old_data[i + 1]])
        # print(h_range)
        data = []
        for i_2 in h_range:
            for i in measure_value_data:
                if i <= i_2[1] and i > i_2[0]:
                    data.append(i)
                elif i == i_2[0]:
                    data.insert(0, i)
            data = sorted(data)
            h_all_data.append(data)
            data = []
        # print(h_range[0][0], numpy.min(measure_value_data), h_all_data)
        # if numpy.min(measure_value_data) == h_range[0][0]:
        #     h_all_data[0][0].append(0)
        # measure_value_data.remove(data)
        # print(h_all_data)
        for i in h_range:
            h_t_x_data.append(str(round(numpy.mean(i), 4)))
        for i in h_all_data:
            h_t_y_data.append(len(i))
        h_y_range = [0, (numpy.max(h_t_y_data) + numpy.max(h_t_y_data) / 2)]
        h_chart_name = '%s_直方圖' % item_name
        # print(h_t_y_data, h_t_x_data, h_y_range)

        # -----------------------------------------------抓取圖表旁表單資料
        x_min = numpy.min(count_y_data)
        x_max = numpy.max(count_y_data)
        x_max_min = round(numpy.max(count_y_data) - numpy.min(count_y_data), 3)
        x_chart_center = x
        x_chart_lower = x_lcl
        x_chart_upper = x_ucl
        x_chart_min = numpy.min(x_y_data)
        x_chart_max = numpy.max(x_y_data)
        x_chart_min_max = x_chart_max - x_chart_min
        r_chart_avg = round(statistics.mean(r_y_data), 2)
        r_chart_max = round(numpy.max(r_y_data), 3)
        r_chart_min = round(numpy.min(r_y_data), 3)
        r_chart_max_min = round(numpy.max(r_y_data) - (numpy.min(r_y_data)), 3)
        r_chart_lower = r_lcl
        r_chart_upper = r_ucl
        h_chart_rang = {}
        h_chart_median = {}
        h_group_pitch = round(float(h_range[0][1] - h_range[0][0]), 3)
        h_full_range = round(x_max - x_min, 3)
        print(h_range)
        for i in h_range:
            print(i)
            h_chart_rang.update({str(h_range.index(i)): "%s ~ %s" % (round(i[0], 2), round(i[1], 2))})
            h_chart_median.update({str(h_range.index(i)): h_t_y_data[h_range.index(i)]})
        chart_data.append({
            'x_chart_center': x_chart_center, "x_chart_lower": x_chart_lower, "x_chart_upper": x_chart_upper,
            'x_chart_min': x_chart_min, 'x_chart_max': x_chart_max, 'x_chart_min_max': x_chart_min_max,
            'r_chart_avg': r_chart_avg, 'r_chart_lower': r_chart_lower, 'r_chart_upper': r_chart_upper,
            'r_chart_max': r_chart_max, 'r_chart_min': r_chart_min, 'r_chart_max_min': r_chart_max_min,
            'x_min': x_min, 'x_max': x_max, 'h_chart_range': h_chart_rang, 'h_chart_median': h_chart_median,
            'h_group_pitch': h_group_pitch, 'h_full_range': h_full_range, 'x_max_min': x_max_min
        })
        print(chart_data)
        # -----------------------------------------------
        data = {
            'x_name': item_id_x, 'x_title': '%sX-bar' % item_name,
            'x_x_data': x_x_data, 'x_y_data': x_y_data,
            'x_x_cl_data': x_x_cl_data, 'x_y_cl_data': x_y_cl_data,
            'x_x_viol_data': x_x_viol_data, 'x_y_viol_data': x_y_viol_data,
            'x_x_center_data': x_x_center_data, 'x_y_center_data': x_y_center_data,
            'x_y_range': x_y_range,
            'r_name': item_id_r, 'r_title': '%sR-bar' % item_name,
            'r_x_data': x_x_data, 'r_y_data': r_y_data,
            'r_x_cl_data': r_x_cl_data, 'r_y_cl_data': r_y_cl_data,
            'r_x_viol_data': r_x_viol_data, 'r_y_viol_data': r_y_viol_data,
            'r_x_center_data': r_x_center_data, 'r_y_center_data': r_y_center_data,
            'r_y_range': r_y_range_data,
            'c_name': item_id_c, 'c_title': '   %s管制圖' % item_name,
            'c_x_data': count_x_data, 'c_y_data': count_y_data,
            'c_x_viol_data': count_viol_x_data, 'c_y_viol_data': count_viol_y_data,
            'c_x_center_data': count_x_center_data, 'c_y_center_data': count_y_center_data,
            'c_x_cl_data': count_cl_x_data, 'c_y_cl_data': count_cl_y_data,
            'c_x_range': count_range_x,
            'data': '量測數值', 'cl': '規格上限/規格下限', 'center': '規格中心', 'vol': '超出',
            'h_t_x_data': h_t_x_data, 'h_t_y_data': h_t_y_data,
            'h_chart_name': h_chart_name, 'h_y_range': h_y_range, 'h_name': h_name,
            'x_chart_center': x_chart_center, "x_chart_lower": x_chart_lower, "x_chart_upper": x_chart_upper,
            'x_chart_min': x_chart_min, 'x_chart_max': x_chart_max
        }
        all_data.append(data)
    n = 0
    for item in measure_item:
        item_id = item['id']
        item_name = models.measure_items.objects.get(id=item['id']).measurement_items
        measure_tool = models.measure_items.objects.get(id=item['id']).too_name
        center = models.measure_items.objects.get(id=item['id']).specification_center
        upper_limit = models.measure_items.objects.get(id=item['id']).upper_limit
        lower_limit = models.measure_items.objects.get(id=item['id']).lower_limit
        number = models.measure_items.objects.get(id=item['id']).measure_number
        point = models.measure_items.objects.get(id=item['id']).measure_points
        unit = models.measure_items.objects.get(id=item['id']).measure_unit
        image_url = models.measure_items.objects.get(id=item['id']).image
        #     # -----------------數據計算
        #     measure_count = models.measure_items.objects.get(id=item['id']).measure_number
        #     measure_value_dcit = models.measure_values.objects.filter(measure_name_id=item['id']). \
        #         values('measure_value', 'measure_number')
        #     value_data = []
        #     all_value_data_sort = []
        #     all_value_data_avg = []
        #     number = int()
        #     for i in measure_value_dcit:
        #         # print(i['measure_value'])
        #         value_data.append(i["measure_value"])
        #         number = number + 1
        #         if number == int(measure_count):
        #             number = 0
        #             all_value_data_sort.append(value_data)
        #             value_data = []
        #     # measure_number = int(len(measure_value_dcit) / int(measure_count))  # 多少量測次數
        #     r_data = []
        #     value_data = []
        #     for i in all_value_data:
        #         for i_2 in i:
        #             value_data.append(i_2)
        #         all_value_data_avg.append(statistics.mean(i))
        #         r_data.append(numpy.max(i) - numpy.min(i))
        #     x = statistics.mean(all_value_data_avg)
        #     r = statistics.mean(r_data)
        #     a2 = a2_data[str(measure_count)]
        #     x_ucl = round(x + a2 * r, 2)  # x上限計算
        #     x_lcl = round(x - a2 * r, 2)  # x下限計算
        #     x_average = round(statistics.mean(all_value_data_avg), 2)
        #     x_max = round(numpy.max(all_value_data_avg), 2)
        #     x_min = round(numpy.min(all_value_data_avg), 2)
        #     # ------------------R計算
        #     d4 = d4_data[str(measure_count)]
        #     d3 = d3_data[str(measure_count)]
        #     r_ucl = round(d4 * r, 2)
        #     r_lcl = round(d3 * r, 2)
        #     r_max = round(numpy.max(r_data), 2)
        #     r_min = round(numpy.min(r_data), 2)
        #     r_max_min = round(numpy.max(r_data) - numpy.min(r_data), 2)
        #     r_avr = round(statistics.mean(r_data), 3)
        #     # ------------------管制圖計算
        #     avg = statistics.mean(value_data)
        #     max_ = round(numpy.max(value_data), 2)
        #     min_ = round(numpy.min(value_data), 2)
        #     max_min = round(numpy.max(value_data) - numpy.min(value_data), 2)
        #     # ------------------質方圖計算
        #     h_max_min = numpy.linspace(numpy.min(value_data), numpy.max(value_data), num=12)
        #     print(h_max_min)
        #     h_range_old_data = []
        #     h_range = []
        #     h_group_pitch = round(r / 11, 2)
        #     for i in h_max_min:
        #         h_range.append(round(i, 2))
        #     print(h_range)
        #     # ----------------字典上傳
        # print('123')
        # print(number)
        data = {'item_id': item_id, 'measurement_items': item_name,
                'tool_name': measure_tool,
                'specification_center': center,
                'upper_limit': upper_limit, 'lower_limit': lower_limit,
                'measure_number': number, 'measure_points': point,
                'measure_unit': unit, 'image': image_url}
        # print(chart_data)
        data.update(chart_data[n])
        print(data)
        n = n + 1
        # print(chart_data[number])
        item_data.append(data)
    #             'x_average': x_average, 'x_ucl': x_ucl, 'x_lcl': x_lcl, 'x_max': x_max,
    #             'x_min': x_min, 'r_avg': r_avr, 'r_ucl': r_ucl, 'r_lul': r_lcl, 'r_max': r_max,
    #             'r_min': r_min, 'r_max_min': r_max_min, 'max': max_, 'min': min_, 'max_min': max_min,
    #             'number': 11, 'h_list': h_range, 'r': round(r, 2), 'h_group_pitch': h_group_pitch}

    # i_2 = {'1':'/', '2': '//'}
    # item_name.update(i_2)
    # print(item_name)
    # print(r, x)
    # print(x_ucl, x_lcl)
    # print(x_x_center_data, x_y_center_data)
    # print(x_y_range)
    # print(r_y_data)  # 每組資料全距
    # print(m_y_data)  # 每組資料平均值
    # print(all_value_data)
    print(all_data)
    return render(request, 'data_display/detail/data_display_all_detail.html', locals())


def display_all_report(request, id):
    # ------------------------------------
    measure_item_data = models.measure_items.objects.filter(project_measure_id=id).values('id')
    print(measure_item_data[0]['id'])
    measure_item = models.measure_items.objects.filter(project_measure_id=id).values('id')
    project_name = models.project.objects.get(id=id).project_name
    man = models.project.objects.get(id=id).founder_name
    # print(man)
    create_date = models.project.objects.get(id=id).project_create_date
    remake = models.project.objects.get(id=id).remake
    project_imag_url = models.project.objects.get(id=id).project_image
    measure_value_man_id = models.measure_values.objects.filter(measure_project_id=id).values('measure_man', 'time_now')
    measure_man = measure_value_man_id[0]['measure_man']
    update_time = measure_value_man_id[0]['time_now']
    measure_count = len(
        models.measure_values.objects.filter(measure_name_id=measure_item_data[0]['id']).values('measure_value')) \
                    / int(
        models.measure_items.objects.get(id=str(measure_item_data[0]['id'])).measure_number)
    print(len(
        models.measure_values.objects.filter(measure_project_id=measure_item_data[0]['id']).values('measure_value')))
    # print(measure_count)
    project_data = {'project_name ': project_name, 'man': man,
                    'create_date': create_date, 'remake': remake,
                    'project_image_url': project_imag_url, 'measure_man': measure_man,
                    'update_time': update_time, 'number_of_pieces': str(measure_count)}
    # -----------------------------------------
    print(id)
    measure_item_data = models.measure_items.objects.filter(project_measure_id=id).values('measurement_items', 'id')
    all_data = []
    yid_data = []
    color = {
        'D': "color: whitesmoke; background-color:pink",
        'C': "color: whitesmoke; background-color:orange",
        'B': "color: whitesmoke; background-color:dodgerblue",
        'A': "color: whitesmoke; background-color:mediumseagreen",
        'A+': "color: white; background-color: seagreen;"
    }
    # print(measure_item_data)
    for item in measure_item_data:
        print(item['measurement_items'])
        # print(item['id'])
        specification_center = models.measure_items.objects.get(id=item['id']).specification_center
        upper_limit = models.measure_items.objects.get(id=item['id']).upper_limit
        lower_limit = models.measure_items.objects.get(id=item['id']).lower_limit
        t = float()
        t = upper_limit - lower_limit
        all_value = models.measure_values.objects.filter(measure_name_id=item['id']).values('measure_value')
        measure_count = models.measure_items.objects.get(id=item['id']).measure_number
        number = 0
        data = []
        measure_all_data = []
        average_data = []
        # print(measure_count)
        for i in all_value:
            number = number + 1
            data.append(i['measure_value'])
            # print(data)
            if int(measure_count) == number:
                number = 0
                measure_all_data.append(data)
                data = []
        for i in measure_all_data:
            average_data.append(statistics.mean(i))
        x = statistics.mean(average_data)
        ca = abs((x - specification_center) / (t / 2)) * 0.01
        stdev = statistics.stdev(average_data)  # 標準差
        print(upper_limit, lower_limit)
        print(average_data)
        cp = (upper_limit - lower_limit) / (6 * stdev)
        cpk = cp * (1 - ca)
        print(cpk)
        print(ca)
        print(cp)
        # --------------------------------------------顏色判別
        ca_color = str()
        cpk_color = str()
        cp_color = str()
        if abs(ca) <= float(0.125):
            ca_color = color['A+']
        elif abs(ca) > float(0.125) and abs(ca) <= float(0.25):
            ca_color = color['A']
        elif abs(ca) > float(0.25) and abs(ca) <= float(0.5):
            ca_color = color['B']
        elif abs(ca) > float(0.5):
            ca_color = color['C']

        if abs(cp) >= 1.67:
            cp_color = color['A+']
        elif abs(cp) >= 1.33 and abs(cp) < 1.67:
            cp_color = color['A']
        elif abs(cp) >= 1.0 and abs(cp) < 1.33:
            cp_color = color['B']
        elif abs(cp) >= 0.67 and abs(cp) < 1.0:
            cp_color = color['C']
        elif abs(cp) < 0.67:
            cp_color = color['D']

        if abs(cpk) >= 1.67:
            cpk_color = color['A+']
        elif abs(cpk) >= 1.33 and abs(cpk) < 1.67:
            cpk_color = color['A']
        elif abs(cpk) >= 1.0 and abs(cpk) < 1.33:
            cpk_color = color['B']
        elif abs(cpk) >= 0.67 and abs(cpk) < 1.0:
            cpk_color = color['C']
        elif abs(cpk) < 0.67:
            cpk_color = color['D']

        # ------------------------------------------
        yield_data = []
        for i in measure_all_data:
            yield_check = True
            for value in i:
                if value > upper_limit or value < lower_limit:
                    print(value)
                    yield_check = False
                else:
                    pass
            if yield_check is False:
                yield_data.append(False)
            else:
                yield_data.append(True)
        yid_data.append(yield_data)

        # ------------------------------------------
        # print(statistics.stdev(average_data))
        # print(x, stdev)
        # print(ca, cp, cpk)
        # print(measure_all_data)
        # print(cpk_color, cp_color, ca_color)
        data = {'item_name': item['measurement_items'], 'cp': round(cp, 3), 'ca': round(ca, 3),
                'cpk': round(cpk, 3), 'upper_limit': upper_limit, 'lower_limit': lower_limit,
                'stdev': round(stdev, 3), 'center': specification_center,
                'ca_color': ca_color,
                'cp_color': cp_color,
                'cpk_color': cpk_color}
        all_data.append(data)
    yid_check = True
    yid_check_data = []
    yid_number = 0
    for i in yid_data[0]:
        yid_check_data.append(True)
    for i in yid_data:
        yid_number = 0
        for i_2 in i:
            yid_number = yid_number + 1
            if i_2 is False:
                a = i.index(i_2)
                yid_check_data[yid_number - 1] = False
            elif i_2 is True:
                pass
    total = len(yid_check_data)
    good_number = int()
    broken_number = int()
    for i in yid_check_data:
        if i is True:
            good_number = good_number + 1
        elif i is False:
            broken_number = broken_number + 1
    print(good_number, broken_number)
    y = round(good_number / total, 2) * 100
    defective = round(broken_number / total, 2) * 100
    print(y, defective)
    print(yid_check_data, defective)
    yid_list = json.dumps([y, defective])
    pie_chart_name = json.dumps(str('%s 良率 / 不良率' % project_name))
    go_nogo_data = {
        'go': good_number, 'nogo': broken_number, 'all': good_number + broken_number
    }
    # ------------------------------------------
    return render(request, 'data_display/report/data_display_report.html', locals())


def display_data_timely(request, id):
    # a = [{'id': '63', 'x': [1, 2, 3, 4, 5], 'y': [10, 4, 7, 8, 8]},
    #      {'id': 'Linear Size.1', 'x': [1, 2, 3, 4, 5], 'y': [2, 4, 7, 8, 8]}]
    # b = json.dumps(['tester', 'tester_1'])
    # print(id)
    chart_id = []
    item = models.measure_items.objects.filter(project_measure_id=id).values('id')
    for i in item:
        image = models.measure_items.objects.get(id=i['id']).image
        item_name = models.measure_items.objects.get(id=i['id']).measurement_items
        chart_id.append({'id': i['id'], 'image': image, 'item_name': item_name})
    print(item[0]['id'])
    project_image_url = models.project.objects.get(id=id).project_image
    # print(image_url)
    project_data = {'project_image_url': project_image_url}
    # print(chart_id)
    # ------------------------
    all_data = []  # 放每一個專案量測項目的資料
    measure_item = models.measure_items.objects.filter(project_measure_id=id).values('measurement_items')
    for item in measure_item:
        count_x_data = []
        count_y_data = []
        count_x_data = []
        count_y_data = []
        count_viol_x_data = []
        count_viol_y_data = []
        count_x_center_data = []
        count_y_center_data = []
        count_viol_x_data = []
        count_viol_y_data = []
        count_range_x = []
        measure_item = item['measurement_items']  # 量測項目名稱
        measure_item_id = models.measure_items.objects.get(measurement_items=measure_item).id  # 量測項目id
        item_upper = float(models.measure_items.objects.get(measurement_items=measure_item).upper_limit)
        item_lower = float(models.measure_items.objects.get(measurement_items=measure_item).lower_limit)
        item_center = float(models.measure_items.objects.get(measurement_items=measure_item).specification_center)
        # print(measure_item, measure_item_id)
        data = models.measure_values.objects.filter(measure_name_id=measure_item_id).values('measure_value',
                                                                                            'measure_number')
        for item_2 in data:
            # print(item_2['measure_value'], item_2['measure_number'])
            count_x_data.append(item_2['measure_number'])
            count_y_data.append(item_2['measure_value'])
            if item_2['measure_value'] > item_upper or item_2['measure_value'] < item_lower:
                count_viol_x_data.append(item_2['measure_number'])
                count_viol_y_data.append(item_2['measure_value'])
        count_x_center_data = [count_x_data[0], count_x_data[-1]]  # 中心線1-1
        count_y_center_data = [item_center, item_center]  # 中心線數值
        count_cl_x_data = [count_x_data[0], count_x_data[-1], '', count_x_data[0], count_x_data[-1]]
        count_cl_y_data = [item_upper, item_upper, '', item_lower, item_lower]
        count_range_x = [item_lower - (item_upper - item_lower) / 6, item_upper + (item_upper - item_lower) / 6]
        name = '%s X-bar' % measure_item
        # print(count_viol_y_data, count_viol_x_data)
        # print(count_x_data, count_y_data)
        # ------------------------------------------
        # ------------------------------------------
        data = {'name': str(measure_item_id), 'count_range_x': count_range_x,
                'count_x_data': count_x_data, 'count_y_data': count_y_data,
                'count_viol_x_data': count_viol_x_data, 'count_viol_y_data': count_viol_y_data,
                'count_cl_x_data': count_cl_x_data, 'count_cl_y_data': count_cl_y_data,
                'count_x_center_data': count_x_center_data, 'count_y_center_data': count_y_center_data,
                'data': '量測數值', 'cl': '規格上限/規格下限', 'center': '規格中心', 'vol': '超出',
                'item_name': str(name)}
        all_data.append(data)
    # print(all_data)

    # count_x_data.append()
    return render(request, 'data_display/timely/data_display_timely.html', locals())
