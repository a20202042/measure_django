from django.test import TestCase
from mysite import models
from django import forms


class Project(forms.ModelForm):
    class Meta:
        model = models.project
        fields = ['project_name', 'project_create_date', 'founder_name', 'materials', 'manufacturing_machine',
                   'remake', 'project_image']
        file = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(Project, self).__init__(*args, **kwargs)
        self.fields['project_name'].label = '專案名稱'
        self.fields['project_create_date'].label = '創建日期'
        self.fields['founder_name'].label = '建立者'
        self.fields['remake'].label = '備註'
        self.fields['materials'].label = '材料'
        self.fields['manufacturing_machine'].label = '機台'
        self.fields['project_image'].label = '零件圖'
    # def clean_project_create_date(self):
    #     project_create_date = self.cleaned_data.get('project_create_date')
    #     if project_create_date != '中文':
    #         raise forms.ValidationError('不得使用中文')
    #     return project_create_date


class Work_order(forms.ModelForm):
    class Meta:
        model = models.measurement_work_order
        fields = ['project_measure', 'sor_no', 'manufacturing_order', 'number_of_parts', 'remake', 'create_time']

    def __init__(self, *args, **kwargs):
        super(Work_order, self).__init__(*args, **kwargs)
        self.fields['project_measure'].label = '專案名稱'
        self.fields['sor_no'].label = "工單"
        self.fields['manufacturing_order'].label = "版次"
        self.fields['number_of_parts'].label = '件數'
        self.fields['remake'].label = '備註'
        self.fields['create_time'].label = '建立時間'

        # self.fields['remake'].request = False


class measure_tool(forms.ModelForm):
    class Meta:
        model = models.measuring_tool
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(measure_tool, self).__init__(*args, **kwargs)
        self.fields['toolname'].label = '量具名稱'
        self.fields['tooltype'].label = '量具類型'
        self.fields['toolprecision'].label = '量具精度'
        self.fields['tooltestdata'].label = '量具檢測日期'


class measure_item(forms.ModelForm):
    class Meta:
        model = models.measure_items
        fields = ['project', 'tool_name', 'measurement_items', 'upper_limit', 'lower_limit',
                  'specification_center', "measure_number", 'measure_unit', 'image']

    def __init__(self, *args, **kwargs):
        super(measure_item, self).__init__(*args, **kwargs)
        self.fields['measurement_items'].label = '量測項目名稱'
        self.fields['project'].label = '專案'
        self.fields['tool_name'].label = '量具名稱'
        self.fields['measure_unit'].label = "量測單位"
        self.fields['upper_limit'].label = '量測數值上限'
        self.fields['lower_limit'].label = '量測數值下限'
        self.fields['specification_center'].label = '量測數值中心'
        self.fields["measure_number"].label = "次數"
        # self.fields['decimal_piaces'].label = '小數點位數'
        self.fields['image'].label = '部位'


class work_measure_item(forms.ModelForm):
    class Meta:
        model = models.measure_items
        fields = ['tool_name', 'measurement_items', 'upper_limit', 'lower_limit',
                  'specification_center', "measure_number", 'measure_unit']

    def __init__(self, *args, **kwargs):
        super(work_measure_item, self).__init__(*args, **kwargs)
        self.fields['measurement_items'].label = '量測項目名稱'
        self.fields['tool_name'].label = '量具名稱'
        self.fields['measure_unit'].label = "量測單位"
        self.fields['upper_limit'].label = '量測數值上限'
        self.fields['lower_limit'].label = '量測數值下限'
        self.fields['specification_center'].label = '量測數值中心'
        self.fields["measure_number"].label = "次數"
        # self.fields['decimal_piaces'].label = '小數點位數'


class work_part_remake(forms.ModelForm):
    class Meta:
        model = models.work_order_parts_reamke
        fields = [ 'remake']

    def __init__(self, *args, **kwargs):
        super(work_part_remake, self).__init__(*args, **kwargs)
        # self.fields['work_order'].label = '工單'
        # self.fields['part_number'].label = '件號'
        self.fields['remake'].label = '備註'
