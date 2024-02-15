from django import forms
from .models import Routes

class EmployeeSelectionForm(forms.Form):
    employee_name = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'onchange': 'submitForm()'}))

    def __init__(self, *args, **kwargs):
        super(EmployeeSelectionForm, self).__init__(*args, **kwargs)
        self.fields['employee_name'].choices = [(name, name) for name in Routes.objects.values_list('name_liv', flat=True).distinct()]


class EmployeeSelectionUrlForm(forms.Form):
    employee_name = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'onchange': 'submitForm()'}))
    selected_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(EmployeeSelectionUrlForm, self).__init__(*args, **kwargs)
        self.fields['employee_name'].choices = [(name, name) for name in Routes.objects.values_list('name_liv', flat=True).distinct()]
        self.fields['selected_date'].widget.attrs.update({'onchange': 'submitForm()'})

