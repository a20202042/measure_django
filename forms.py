from django import forms
from mysite import models

class projectfrom(forms.ModelForm):
    class Meta:
        model = models.project
        fields = ['project_name', 'founder_name', 'remake']

    def __init__(self, *args, **kwargs):
        super(projectfrom, self).__init__(*args, **kwargs)
        self.fields['project_name'].label = '專案名稱'
        self.fields['founder_name'].label = '建立人'
        self.fields['remake'].label = '備註'

